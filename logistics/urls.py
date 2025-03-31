from django.urls import path
from .views import logisticDashboard,update_status,status
urlpatterns = [
    path('dashboard/',logisticDashboard,name="logistic_dashboard"),
    path('update-status/<int:request_id>/<str:status>/', update_status, name='update_status'),
    path('status/<int:did>/',status,name="logistic_status")
]
