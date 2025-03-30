from django.urls import path  
from .views import Dashboard

urlpatterns = [
    path("dashboard/",Dashboard,name="donation_dashboard")
]
