from rest_framework import serializers
from .models import (
    Material,
    MaterialUsage,
    MeasurementMethod,
)


class MeasurementMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementMethod
        fields = ('name',)


class MaterialSerializer(serializers.ModelSerializer):
    mesurements = MeasurementMethodSerializer(many=True, read_only=True)
    class Meta:
        model = Material
        fields = ('name', 'created_at', 'mesurements',)

class MaterialUsageSerializer(serializers.ModelSerializer):
    measurement_method=MeasurementMethodSerializer(read_only=True)
    material=MaterialSerializer(read_only=True)
    class Meta:
        model = MaterialUsage
        fields = "__all__"

class AddMaterialUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialUsage
        fields = "__all__"

# {
# "measurement_method":2,
# "quantity":2,
# "price":36000,
# "material":3
# }