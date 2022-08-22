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


# @api_view(['POST'])
# def add_material_usage_(request):
#     measurement_method = request.POST["measurement_method"] #fk
#     quantity = request.POST["quantity"] #not fk
#     price = request.POST["price"] #not fk
#     material = request.POST["material"] #fk

#     material_usage = MaterialUsage.objects.create(
#         measurement_method=measurement_method,
#         quantity=quantity,
#         price=price,
#         material=material,
#     )
#     serializer = MaterialUsageSerializer(materials, many=True)
#     return Response(serializer.data)