
from django.urls import path
from . import views


urlpatterns = [
    path("all/", views.get_all_workers, name="all_workers"),
    path("add/", views.add_worker, name="add_worker")
]
