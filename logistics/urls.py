from django.urls import path
from .views import logisticDashboard
urlpatterns = [
    path('dashboard',logisticDashboard,name="logistic_dashboard")
]
