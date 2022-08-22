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
    class Meta:
        model = MaterialUsage
        fields = "__all__"