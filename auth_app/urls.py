from django.urls import path
from .views import user_login,signupDonor,signupOrganization,user_logout

urlpatterns = [
    path('login/',user_login,name='auth_login'),
    path('signup/donor/',signupDonor,name='auth_signup_donor'),
    path('signup/organization/',signupOrganization,name='auth_signup_organization'),
    path('logout/',user_logout,name="logout")
]
