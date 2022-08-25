from django_filters import rest_framework as filters
from django.db.models import Q
from .models import (
    Worker,
    # DailyWork,
)

class WorkerFilterSet(filters.FilterSet):
    # first_name = filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Worker
        fields=[]

    @property
    def qs(self):
        parent = super().qs
        name = self.request.query_params.get('name')

        return parent.filter(
            Q(last_name__icontains=name)
            | Q(first_name__icontains=name)
        )
