from django.contrib import admin
from .models import CustomUser, UserTypes, Donor, Organization

admin.site.register(CustomUser)
admin.site.register(UserTypes)
admin.site.register(Donor)
admin.site.register(Organization)

# Register your models here.
