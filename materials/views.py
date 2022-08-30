from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters import rest_framework as filters
from rest_framework import generics
from django.db.models import Sum

from .models import (
    Material,
    MaterialUsage,
    MeasurementMethod,
)

from .serializers import (
    MaterialSerializer,
    MaterialUsageSerializer,
    AddMaterialUsageSerializer,
    MeasurementMethodSerializer,
)

from .filter import (
    MaterialFilterSet,
    MaterialUsageFilterSet,
)


@api_view(['GET'])
def get_all_materials(request):
    materials = Material.objects.prefetch_related('mesurements').all()
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add_material_usage(request):
    serializer = AddMaterialUsageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        print(serializer.errors)

    return Response(serializer.data)


@api_view(['GET'])
def get_all_measurement_methods(request):
    measurement_method = MeasurementMethod.objects.all()
    serializer = MeasurementMethodSerializer(measurement_method, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_material_usage(request):
    materials_usage = MaterialUsage.objects.all()
    serializer = MaterialUsageSerializer(materials_usage, many=True)
    return Response(serializer.data)


class MaterialFilter(generics.ListAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    filterset_class = MaterialFilterSet

class MaterialUsageView(generics.ListAPIView):
    queryset = MaterialUsage.objects.all()
    serializer_class = MaterialUsageSerializer
    filterset_class = MaterialUsageFilterSet

@api_view(['GET'])
def material_usage_filter(request):
    cc = MaterialUsage.objects.filter(
        added_date="2022-08-29"
        ).values(
            'material',
            'measurement_method',
            'measurement_method__name',
            'material__name'
        ).order_by().annotate(total_price=Sum('price'))
    summations = [sums for sums in cc]
    return Response(summations)

@api_view(['POST'])
def add_material(request):
    material = Material.objects.create(
        name=request.data["name"]
    )
    measurement_method = MeasurementMethod.objects.get(pk=request.data["measurement_method"])
    material.mesurements.add(measurement_method)

    return Response(request.data)