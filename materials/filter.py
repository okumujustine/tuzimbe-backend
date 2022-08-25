from django_filters import rest_framework as filters
from .models import (
    Material,
)

class MaterialFilterSet(filters.FilterSet):

    class Meta:
        model = Material
        fields= {
            "name":["icontains"],
        }