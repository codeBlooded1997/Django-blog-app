from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', PostListView.as_view(), name='list'),
    path('<slug>/', PostDetailView.as_view(), name='detail'),
    path('<slug>/update', PostUpdateView.as_view(), name='update'),
    path('<slug>/delete', PostDeleteView.as_view(), name='delete'),
    path('create', PostCreateView.as_view(), name='create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          doncument_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          doncument_root=settings.STATIC_ROOT)
