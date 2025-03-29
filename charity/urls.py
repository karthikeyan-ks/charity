from django.contrib import admin
from django.urls import path
from django.urls import path, include  
from auth_app.views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',home, name="home"),
    path('admin/', admin.site.urls),
    path('auth/', include('auth_app.urls')),
    path('organization/',include('Organization.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)