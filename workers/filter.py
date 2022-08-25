from django_filters import rest_framework as filters
from .models import (
    Worker,
    # DailyWork,
)

class WorkerFilterSet(filters.FilterSet):
    # first_name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
         # fields = ('first_name',)
        model = Worker
        fields= {
            "first_name":["icontains"],
            "last_name":["icontains"]
        }