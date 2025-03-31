from django.db import models
from django.utils import timezone

# Create your models here.
class DeliveryRequest(models.Model):
    did = models.AutoField(primary_key=True)
    logistic_partner = models.ForeignKey('auth_app.LogisticPartner',on_delete=models.CASCADE,related_name="request_logistic_partner")
    delivered_by = models.ForeignKey('auth_app.CustomUser',on_delete=models.CASCADE,related_name="request_delivered_by")
    delivered_to = models.ForeignKey('auth_app.CustomUser',on_delete=models.CASCADE,related_name="request_delivered_to")
    donation = models.ForeignKey('donations.Donations',on_delete=models.CASCADE,related_name="request_donation")
    request = models.ForeignKey('Organization.RequestResource',on_delete=models.CASCADE,related_name="request_organization")
    date = models.DateField(default=timezone.now)
    accept = models.BooleanField(default=False)
    finished = models.BooleanField(default=False)
    
    def __str__(self):
        return self.logistic_partner.user.username