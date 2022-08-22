from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
    Material,
    MaterialUsage,
    MeasurementMethod,
)

from .serializers import (
    MaterialSerializer,
    MaterialUsageSerializer,
)


@api_view(['GET'])
def get_all_materials(request):
    materials = Material.objects.prefetch_related('mesurements').all()
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_material_usage(request):
    serializer = MaterialUsageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def get_all_material_usage(request):
    materials_usage = MaterialUsage.objects.all()
    serializer = MaterialUsageSerializer(materials_usage, many=True)
    return Response(serializer.data)