from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include

from CoopJob import settings

urlpatterns = [
    re_path('', include('main.urls')),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
