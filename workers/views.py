from django.shortcuts import render
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status

from .models import (
    Worker,
    DailyWork,
)
from .serializers import (
    WorkerSerializer,
    DailyWorkSerializer,
)
from .filter import (
    WorkerFilterSet,
    DailyAttendanceFilterSet,
)


@api_view(['POST'])
def add_daily_worker(request):
    obj = DailyWork.objects.filter(
        worker_id=request.data["worker"],
        added_date=request.data["added_date"]
    ).first()

    if obj:
        return Response("User already added to attendance list",status=status.HTTP_400_BAD_REQUEST)

    try:
        d_w = DailyWork.objects.create(
            worker_id=request.data["worker"],
            arrival_time=request.data["arrival_time"],
            daily_rate=request.data["daily_rate"]
        )
        serializer = DailyWorkSerializer(d_w)
        return Response(serializer.data)
    except:
          return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

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

@api_view(['POST'])
def set_departure_time(request):
    departure_time = request.data["departure_time"]
    attendence_pk = request.data["attendence_pk"]
    att = DailyWork.objects.get(pk=attendence_pk)
    att.departure_time = departure_time
    att.save()
    return Response({"set":"true"})


class WorkerFilter(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
    filterset_class = WorkerFilterSet



class DailyAttendance(generics.ListAPIView):
    queryset = DailyWork.objects.all()
    serializer_class = DailyWorkSerializer
    filterset_class = DailyAttendanceFilterSet

