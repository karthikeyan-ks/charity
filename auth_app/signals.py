from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser ,Organization,Donor,UserTypes # Import the related model

        