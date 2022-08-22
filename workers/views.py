from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
    Worker,
    DailyWork,
)
from .serializers import (
    WorkerSerializer,
    DailyWorkSerializer,
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

