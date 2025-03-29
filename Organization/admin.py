from django.contrib import admin
from .models import RequestResource, Resource, AvailableDays

# Register your models here.
admin.site.register(RequestResource)
admin.site.register(Resource)
admin.site.register(AvailableDays)