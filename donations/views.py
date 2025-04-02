from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Donations
from auth_app.models import Donor,LogisticPartner,Organization
from logistics.models import DeliveryRequest
from Organization.models import Resource, AvailableDays, RequestResource
import logging
from django.db.models import Q
logger = logging.getLogger(__name__)

@login_required
def Dashboard(request):
    # Initialize the base queryset
    donations = Donations.objects.filter(created_by=request.user,active = True)
    
    sort_by = request.GET.get('sort', '')  # Get the sort option (default is empty string)
    if sort_by:
        if sort_by == 'name':
            donations = donations.order_by('name')  # Sort by name
        elif sort_by == 'resource':
            donations = donations.order_by('resource')  # Sort by resource
        elif sort_by == 'quantity':
            donations = donations.order_by('quantity')  # Sort by quantity

    # Handle filtering
    filter_type = request.GET.get('filter_type', '')  # Get the filter type
    filter_value = request.GET.get('filter_value', '').strip()  # Get the filter value
    if filter_type and filter_value:
        if filter_type == 'name':
            donations = donations.filter(name__icontains=filter_value)  # Filter by name
        elif filter_type == 'resource':
            donations = donations.filter(resource__icontains=filter_value)  # Filter by resource
        elif filter_type == 'quantity':
            # Assuming quantity is an integer, you can adjust the filter condition as needed
            donations = donations.filter(quantity__icontains=filter_value)  # Filter by quantity

    return render(request, 'donations/dashboard.html', {
        'donations': donations,
    })
    
def newDonation(request):
    resources = Resource.objects.all()
    available_days = AvailableDays.objects.all()
    print(resources,available_days)
    
    return render(request,'donations/new_donation.html',{
        'resources':resources,
        'available_days': available_days
    })
 
@login_required  
def searchRequest(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        resource_id = request.POST.get("resource")
        quantity = request.POST.get("quantity")
        selected_request_id = request.POST.get("selected_request", None)  # Optional field

        # Validate form data
        print("Selected id:",selected_request_id)
        if not name or not description :
            messages.error(request, "Please fill in all required fields.")
            return redirect("new_donation")
        if not selected_request_id and not quantity or not selected_request_id and not resource_id:
            messages.error(request, "Please fill in all required fields.")
            return redirect("new_donation")
        try:
            req = RequestResource.objects.filter(rid = selected_request_id).first()
            if not resource_id:
                resource_id = req.resource.rid
            resource = Resource.objects.get(rid=int(resource_id))
            if not quantity:
                quantity = req.quantity
            quantity = int(quantity)
            print(quantity,resource_id)
            # Create the donation
            donation = Donations.objects.create(
                name=name,
                description=description,
                resource=resource,
                quantity=quantity,
                created_by=request.user,  # Assuming logged-in user
                donated_to=req,
                active = True
            )
            donor = Donor.objects.filter(user= request.user).first()
            print(donor,request.user)
            if selected_request_id:
                organization = Organization.objects.filter(user = req.created_by.user).first()
                req.logistic_partner = organization.logisticPartner
                req.donated = donor
                req.is_donated = True
                req.save()
                DeliveryRequest.objects.create(
                    logistic_partner=organization.logisticPartner,
                    delivered_by=donor.user,
                    delivered_to = organization.user if selected_request_id else None,
                    donation = donation,
                    request = req,
                    accept = True
                )
            messages.success(request, "Donation successfully created!")
            return redirect("donation_success")  # Redirect to form again or success page

        except Resource.DoesNotExist:
            messages.error(request, "Invalid resource selection.")
            return redirect("search_requests")

        except ValueError as e:
            logger.error(f"ValueError occurred: {str(e)}", exc_info=True)
            messages.error(request, e.__str__)
            return redirect("search_requests")
        
    resources = Resource.objects.all()
    available_days = AvailableDays.objects.all()
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'name')  # Default to searching by name
    results = []
    if category == 'name':
        results = RequestResource.objects.filter(name__icontains=query, active=True).exclude(donated__isnull=False)
    elif category == 'resource':
        results = RequestResource.objects.filter(resource__name__icontains=query,active = True).exclude(donated__isnull=False)
    elif category == 'quantity':
        results = RequestResource.objects.filter(quantity__icontains=query,active = True).exclude(donated__isnull=False)
    return render(request, 'donations/new_donation.html', {'results': results, 'query': query,'resources':resources,'available_days': available_days,'category':category})




def donation_success(request):
    donation = request.session.pop("donation_success", None)  # Remove after use
    return render(request, "donations/success.html", {"donation": donation})


@login_required
def donation_delete(request,did):
    print(did)
    donation = Donations.objects.filter(rid = did).first()
    donation.active =False
    donation.save()
    return redirect('donation_dashboard')

def donation_update(request, did):
    # Fetch the donation request by ID
    donation = get_object_or_404(Donations, rid=did)
    print(did)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        resource_id = request.POST.get("resource")
        quantity = request.POST.get("quantity")
        pic = request.FILES.get("pic")

        # Ensure required fields are present
        if not all([name, description, resource_id, quantity]):
            messages.error(request, "All fields are required.")
            return redirect("donation_update", did=did)

        # Update fields
        donation.name = name
        donation.description = description
        donation.resource = get_object_or_404(Resource, rid=resource_id)
        donation.quantity = int(quantity)
        
        # Update image if a new one is uploaded
        
        donation.save()
        messages.success(request, "Donation request updated successfully.")
        return redirect("donation_dashboard")  # Redirect to the donation dashboard

    # If GET request, render the update form
    resources = Resource.objects.all()
    print(resources)
    return render(request, "donations/update_donation.html", {"req": donation, "resources": resources})

@login_required
def similar_donation(request,id):
    req = RequestResource.objects.filter(rid = id).first()
    donation_similar_resource = Donations.objects.filter(resource = req.resource,active=True).exclude(donated_to__isnull=False)
    print(donation_similar_resource)
    return render(request,'donations/see_similar_request.html',{
        'donation':donation_similar_resource
    })
    
@login_required
def acceptDonation(request, did):
    # Fetch the organization for the logged-in user
    organization = Organization.objects.filter(user=request.user).first()
    
    # Get the donation based on 'did' and make sure it's valid
    donation = get_object_or_404(Donations, rid=did)
    
    # Get the donor based on the 'created_by' user in the donation
    donor = get_object_or_404(Donor, user=donation.created_by)
    
    
    # Create a new RequestResource based on the donation
    req = RequestResource.objects.create(
        name=donation.name,
        created_by=organization,
        quantity=donation.quantity,
        active=True,
        logistic_partner=organization.logisticPartner,  # Corrected to 'logistic_partner'
        donated=donor,
        description=donation.description,
        resource=donation.resource
    )
    donation.donated_to = req
    donation.save()
    
    # Create a new DeliveryRequest linked to the created RequestResource
    deliver = DeliveryRequest.objects.create(
        logistic_partner=organization.logisticPartner,
        delivered_by=donor.user,
        delivered_to=organization.user,
        donation=donation,
        request=req,
    )
    print(deliver)
    
    # After processing, redirect the user to a page (either the similar donation page or dashboard)
    return redirect('organization_dashboard')  #

def updateDonation(request,did):
    donation = Donations.objects.filter(rid = did).first()
    return render(request,'donations/update_donation.html',{
        'req':donation
    })