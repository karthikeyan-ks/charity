from django.db import models

class Donations(models.Model):
    rid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    resource = models.ForeignKey('Organization.Resource',on_delete=models.CASCADE,related_name="request_donor")
    quantity = models.IntegerField(blank=False)
    created_by = models.ForeignKey('auth_app.CustomUser',on_delete=models.CASCADE,related_name="created_by_user")
    donated_to = models.ForeignKey('Organization.RequestResource',on_delete=models.CASCADE, related_name="donated_to_request",blank=True,null=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    