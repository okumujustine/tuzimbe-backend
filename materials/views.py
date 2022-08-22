from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import (
    Material,
    MeasurementMethod,
)

from .serializers import (
    MaterialSerializer,
)


@api_view(['GET'])
def get_all_materials(request):
    materials = Material.objects.prefetch_related('mesurements').all()
    serializer = MaterialSerializer(materials, many=True)
    return Response(serializer.data)
