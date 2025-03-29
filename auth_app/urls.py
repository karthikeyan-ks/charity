from django.urls import path
from .views import login,signup

urlpatterns = [
    path('login/',login,name='auth_login'),
    path('signup/',signup,name='auth_signup')
]
