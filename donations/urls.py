from django.urls import path  
from .views import Dashboard,newDonation,searchRequest,donation_success,donation_delete,donation_update,similar_donation,acceptDonation

urlpatterns = [
    path("dashboard/",Dashboard,name="donation_dashboard"),
    path('newDonation/',newDonation,name="new_donation"),
    path('searchRequest/',searchRequest,name="search_requests"),
    path("donation-success/", donation_success, name="donation_success"),
    path('donation-delete/<int:did>/',donation_delete,name="donation_delete"),
    path('donation-update/<int:did>/',donation_update,name="donation_update"),
    path('similar-donations/<int:id>',similar_donation,name="similar_donations"),
    path('accept-donation/<int:did>/',acceptDonation,name="accept_donation")
]
