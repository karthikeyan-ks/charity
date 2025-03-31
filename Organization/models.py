from django.db import models
from django.utils import timezone

# Create your models here.
class Resource(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class AvailableDays(models.Model):
    aid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class RequestResource(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    resource = models.ForeignKey(Resource,on_delete=models.CASCADE,related_name="request_resource")
    quantity = models.IntegerField(blank=False)
    created_by = models.ForeignKey('auth_app.Organization',on_delete=models.CASCADE,related_name="created_by_organization")
    available_days = models.ManyToManyField(AvailableDays,blank=True)
    pic = models.ImageField(upload_to="organization/",blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    pick_up_available = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    