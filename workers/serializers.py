from rest_framework import serializers
from .models import (
    Worker,
    DailyWork,
)

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"

class DailyWorkSerializer(serializers.ModelSerializer):
    worker = WorkerSerializer(read_only=True)
    class Meta:
        model = DailyWork
        fields = "__all__"