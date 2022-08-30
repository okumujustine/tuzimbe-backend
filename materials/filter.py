from django_filters import rest_framework as filters
from django.db.models import Sum
from .models import (
    Material,
    MaterialUsage,
)

class MaterialFilterSet(filters.FilterSet):

    class Meta:
        model = Material
        fields= {
            "name":["icontains"],
        }


class MaterialUsageFilterSet(filters.FilterSet):
    class Meta:
        model = MaterialUsage
        fields=[]
        # fields = {
        #     'added_date': ['iexact'],
        # }

    @property
    def qs(self):
        parent = super().qs
        print(parent.annotate(sum=Sum("price")))
        return parent