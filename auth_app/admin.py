from django.contrib import admin
from .models import CustomUser, UserTypes, Donor, Organization, LogisticPartner

admin.site.register(CustomUser)
admin.site.register(UserTypes)
admin.site.register(Donor)
admin.site.register(Organization)
admin.site.register(LogisticPartner)

# Register your models here.
