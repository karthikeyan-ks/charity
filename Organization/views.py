from django.shortcuts import render,redirect
from .models import RequestResource,Resource,AvailableDays
from auth_app.models import Organization,Donor,LogisticPartner
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import FieldDoesNotExist

# Create your views here.
@login_required
def Dashboard(request):
    organization = Organization.objects.filter(user=request.user).first()
    logisticPartner = LogisticPartner.objects.filter(user = request.user).first()
    print("Logistic",logisticPartner)
    # Handle sorting
    if not organization:
        messages.error(request,'User is not a organization enlisted in our site')
        return redirect('auth_login')
    print(organization)
    requests = RequestResource.objects.filter(created_by = organization,active = True)
    if request.method == "GET":
        sort_by = request.GET.get('sort', None)  
        filter_type = request.GET.get('filter_type', None)
        filter_value = request.GET.get('filter_value', None)
        print("Values are:",sort_by,filter_type,filter_value)
        if sort_by:
            try:
                RequestResource._meta.get_field(sort_by)
                requests.order_by(sort_by)
                print("Field exists!")
                requests = requests.order_by(sort_by)
            except FieldDoesNotExist:
                messages.error(request,'Sort feild does not exists')
                print("Field does not exist!")
        if filter_type == 'name':
            requests = requests.filter(name__startswith = filter_value)
        elif filter_type == 'resource':
            requests = requests.filter(resource__startswith = filter_value)
        elif filter_type == 'quantity':
            requests = requests.filter(quantity__startswith = int(filter_value))
        else:
            messages.error(request,'Filter type is not known')
        print(sort_by,requests)
    return render(request,'Organization/dashboard.html',{
        'requests':requests,
        'user':request.user,
        'logisticPartner':logisticPartner
        })
    
 
@login_required
def newRequest(request):
    organization = Organization.objects.filter(user=request.user).first()
    if not organization:
        messages.error(request, 'User is not an organization enlisted in our site')
        return redirect('auth_login')

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        resource_id = request.POST.get("resource")
        quantity = request.POST.get("quantity")
        available_days_ids = request.POST.getlist("available_days") 
        pic = request.FILES.get("pic")

        print("Datas in server :",resource_id,name,description,quantity,available_days_ids)
        resource = Resource.objects.get(rid=int(resource_id))

        request_resource = RequestResource.objects.create(
            name=name,
            description=description,
            resource=resource,
            quantity=quantity,
            created_by=organization,
            pic=pic
        )

        # Add the selected available days to the ManyToManyField
        request_resource.available_days.set(available_days_ids)

        messages.success(request, "Request added successfully!")
        return redirect("organization_dashboard")

    # Fetch available resources and available days for the form
    resources = Resource.objects.all()
    available_days = AvailableDays.objects.all()
    
    return render(request, "Organization/add_new_request.html", {
        "resources": resources,
        "available_days": available_days,
        'user':request.user
    })
    
    
@login_required
def updateRequest(request,rid):
    req = RequestResource.objects.filter(rid=rid).first()
    resource = Resource.objects.all()
    available_days = AvailableDays.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        resource_id = request.POST.get("resource")
        quantity = request.POST.get("quantity")
        available_days_ids = request.POST.getlist("available_days") 
        pic = request.FILES.get("pic")
        request_resource = RequestResource.objects.get(rid=rid)
        print(name,description,resource_id,quantity,available_days_ids,pic)
        if pic:      
            request_resource.pic = pic
        request_resource.name=name
        request_resource.description=description
        request_resource.quantity=quantity
        request_resource.available_days.set(available_days_ids)
        request_resource.save()
        return redirect("organization_dashboard")
    return render(request,'Organization/update_request.html',{
        'req':req,
        'resources':resource,
        'available_days':available_days
    })
    
@login_required
def deleteRequest(request,rid):
    req = RequestResource.objects.filter(rid = rid).first()
    req.active = False
    req.save()
    return redirect('organization_dashboard')