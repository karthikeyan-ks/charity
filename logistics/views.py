from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DeliveryRequest
from auth_app.models import LogisticPartner
# Create your views here.
@login_required
def logisticDashboard(request):
    logisticPartner = LogisticPartner.objects.filter(user = request.user).first()
    delivery_request = DeliveryRequest.objects.filter(logistic_partner = logisticPartner)
    delivery_request = delivery_request.order_by('-accept')
    return render(request,'logistics/dashboard.html',{
        'delivery_request':delivery_request
    })