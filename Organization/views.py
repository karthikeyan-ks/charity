from django.shortcuts import render
from .models import RequestResource,Resource,AvailableDays
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Dashboard(request):
    requests = RequestResource.objects.filter(created_by = request.user)
    return render(request,'')