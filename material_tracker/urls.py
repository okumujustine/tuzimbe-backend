
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("worker/", include("workers.urls"), name="workers"),
    path("material/", include("materials.urls"), name="materials"),
]
