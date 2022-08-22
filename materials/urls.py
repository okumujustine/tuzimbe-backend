
from django.urls import path
from . import views


urlpatterns = [
    path("all/", views.get_all_materials, name="get_all_materials"),
    path("add_usage/", views.add_material_usage, name="add_material_usage"),
    path("all_material_usage/", views.get_all_material_usage, name="get_all_material_usage"),
]
