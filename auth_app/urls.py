from django.urls import path
from .views import user_login,signupDonor,signupOrganization,user_logout,signupLogisticPartner,edit_profile

urlpatterns = [
    path('login/',user_login,name='auth_login'),
    path('signup/donor/',signupDonor,name='auth_signup_donor'),
    path('signup/organization/',signupOrganization,name='auth_signup_organization'),
    path('signup/logistic/',signupLogisticPartner,name="auth_signup_logistic"),
    path('logout/',user_logout,name="logout"),
    path('edit-profile/', edit_profile, name='edit_profile'),
]
