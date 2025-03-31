from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DeliveryRequest
from auth_app.models import LogisticPartner,Organization
from django.http import JsonResponse
from Organization.models import RequestResource
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DeliveryRequest

@login_required
def logisticDashboard(request):
    organization = Organization.objects.filter(user=request.user).first()
    logistic_partner = LogisticPartner.objects.filter(user=request.user).first()
    
    # Get all delivery requests
    delivery_request = DeliveryRequest.objects.filter(logistic_partner=logistic_partner)

    # Handle sorting
    sort_by = request.GET.get('sort', None)
    if sort_by in ['name', 'resource', 'quantity']:
        if sort_by == 'name':
            delivery_request = delivery_request.order_by('delivered_to__username')
        elif sort_by == 'resource':
            delivery_request = delivery_request.order_by('donation__resource')
        elif sort_by == 'quantity':
            delivery_request = delivery_request.order_by('donation__quantity')

    # Handle filtering
    filter_type = request.GET.get('filter_type', None)
    filter_value = request.GET.get('filter_value', '').strip()
    if filter_type and filter_value:
        if filter_type == 'name':
            delivery_request = delivery_request.filter(delivered_to__username__icontains=filter_value)
        elif filter_type == 'resource':
            delivery_request = delivery_request.filter(donation__resource__icontains=filter_value)
        elif filter_type == 'quantity' and filter_value.isdigit():
            delivery_request = delivery_request.filter(donation__quantity=int(filter_value))

    return render(request, 'logistics/dashboard.html', {
        'delivery_request': delivery_request,
        'organization': organization
    })

    
@login_required
def status(request,did):
    req = RequestResource.objects.filter(rid = did).first()
    delivery_request = DeliveryRequest.objects.filter(request=req).first()
    print(req,delivery_request)
    return render(request,'Organization/status.html',{
        'request':delivery_request
    })
    
@login_required
@csrf_exempt
def update_status(request, request_id, status):
    print(request_id,status)
    if request.method == "POST":
        print("Post request is made..")
        try:
            # Fetch the request object
            delivery_request = DeliveryRequest.objects.get(did=request_id)

            # Update status based on the action
            if status == 'accept' and not delivery_request.accept:
                delivery_request.accept = True
            elif status == 'pickup' and delivery_request.accept and not delivery_request.pickup:
                delivery_request.pickup = True
            elif status == 'finish' and delivery_request.pickup and not delivery_request.finished:
                delivery_request.finished = True
                req = delivery_request.request
                req.active = False
                req.save()
            delivery_request.save()

            return JsonResponse({'success': True})

        except DeliveryRequest.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Request not found'})