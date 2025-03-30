from django.urls import path  
from .views import Dashboard,newRequest,deleteRequest,updateRequest

urlpatterns = [
    path("dashboard/",Dashboard,name="organization_dashboard"),
    path('new-resource-request/',newRequest,name="new_resource_request"),
    path('delete/<int:rid>/',deleteRequest,name="request_delete"),
    path('update/<int:rid>/',updateRequest,name="request_update")
]
