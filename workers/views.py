from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

from .models import (
    Worker,
    DailyWork,
)
from .serializers import (
    WorkerSerializer,
    DailyWorkSerializer,
)
from.filter import (
    WorkerFilterSet,
)


@api_view(['GET'])
def get_all_workers(request):
    workers = Worker.objects.all()
    serializerd_workers = WorkerSerializer(workers, many=True)
    return Response(serializerd_workers.data)


@api_view(['POST'])
def add_worker(request):
    serializer = WorkerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def get_daily_works(request):
    daily_works = DailyWork.objects.all()
    serializer_daily_works = DailyWorkSerializer(daily_works, many=True)
    return Response(serializer_daily_works.data)


class WorkerFilter(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = WorkerFilterSet

