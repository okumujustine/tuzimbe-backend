
from django.urls import path
from . import views


urlpatterns = [
    path("all/", views.get_all_materials, name="get_all_materials"),
    path("add_usage/", views.add_material_usage, name="add_material_usage"),
    path("all_material_usage/", views.get_all_material_usage, name="get_all_material_usage"),
    path("filter/", views.MaterialFilter.as_view(), name="filter_materials"),
    path("material_usage", views.MaterialUsageView.as_view(), name="material_usage"),
    path("material_usage_filter/", views.material_usage_filter, name="material_usage_filter"),
    path("add_material/", views.add_material, name="add_material"),
    path("get_all_measurement_methods/", views.get_all_measurement_methods, name="get_all_measurement_methods")
]
