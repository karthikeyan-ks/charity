from django.db import models

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

class Donations(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    resource = models.ForeignKey('Organization.Resource',on_delete=models.CASCADE,related_name="request_donor")
    quantity = models.IntegerField(blank=False)
    created_by = models.ForeignKey('auth_app.CustomUser',on_delete=models.CASCADE,related_name="created_by_user")
    available_days = models.ManyToManyField('Organization.AvailableDays',blank=True)
    
    def __str__(self):
        return self.name
    