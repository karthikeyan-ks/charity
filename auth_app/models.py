from django.contrib.auth.models import AbstractUser
from django.db import models

class UserTypes(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    # Add custom fields
    user_type = models.ForeignKey(UserTypes,on_delete=models.CASCADE,related_name="user_type",default=3)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.username
    
class Donor(models.Model):
    did = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="user_donor")
    address = models.TextField(default="address 1")
    pincode = models.CharField(max_length=6,default="123456")
    
    def __str__(self):
        return self.user.email
    
class LogisticPartner(models.Model):
    lid = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="user_logistic")
    license = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    noe = models.IntegerField(default=1)#number of employee
    available_employee = models.IntegerField(default=1)
    
    
    def __str__(self):
        return self.user.username
    

class Organization(models.Model):
    oid = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="user_organization")
    license = models.CharField(max_length=100)
    address = models.TextField()
    pincode = models.CharField(max_length=6)
    logisticPartner = models.ForeignKey(LogisticPartner,on_delete=models.CASCADE,related_name="organization_logistic_partner",default=1)
    
    def __str__(self):
        return self.user.email
    