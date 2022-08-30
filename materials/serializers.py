from rest_framework import serializers
from .models import (
    Material,
    MaterialUsage,
    MeasurementMethod,
)


class MeasurementMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementMethod
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    mesurements = MeasurementMethodSerializer(many=True)
    class Meta:
        model = Material
        fields = "__all__"

class MaterialUsageSerializer(serializers.ModelSerializer):
    measurement_method=MeasurementMethodSerializer()
    material=MaterialSerializer()
    class Meta:
        model = MaterialUsage
        fields = "__all__"

class AddMaterialUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialUsage
        fields = "__all__"


class MeasurementMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementMethod
        fields = "__all__"


# {
# "measurement_method":4,
# "quantity":1,
# "price":3600000,
# "material":2
# }