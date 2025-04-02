from django.contrib import admin
from .models import CustomUser, UserTypes, Donor, Organization, LogisticPartner

admin.site.register(CustomUser)
admin.site.register(UserTypes)
admin.site.register(Donor)
admin.site.register(Organization)
admin.site.register(LogisticPartner)

admin.site.site_header = "Unite to Uplift "
admin.site.site_title = "My Site Admin"
admin.site.index_title = "Welcome to Admin Panel"

# Register your models here.
