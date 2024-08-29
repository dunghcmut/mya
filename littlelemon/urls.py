from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # Maps the admin interface to /admin/
    path(
        "api/", include("restaurant.urls")
    ),  # Includes URLs from the restaurant app
]
