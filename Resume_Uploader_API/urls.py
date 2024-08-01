from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app1.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# This part added to show the media files when clicked on the link in admin pannel
# static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)