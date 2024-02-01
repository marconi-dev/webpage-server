from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/", include("studies.urls")),
    path("v1/", include("articles.urls")),
    path("v1/", include("projects.urls")),
    path("v1/", include("my_profile.urls")),
    path("v1/", include("links.urls")),
]

if settings.DEBUG:
    urlpatterns += static(prefix=settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
