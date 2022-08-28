from django_filters import rest_framework as filters
from django.db.models import Q
from .models import (
    Worker,
    DailyWork,
)

class WorkerFilterSet(filters.FilterSet):
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

class DailyAttendanceFilterSet(filters.FilterSet):
    class Meta:
        model = DailyWork
        fields = {
            'added_date': ['iexact'],
            # 'username': ['iexact']
        }