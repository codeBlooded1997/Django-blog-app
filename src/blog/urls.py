from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          doncument_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          doncument_root=settings.STATIC_ROOT)
