from rest_framework import serializers
from .models import Worker

class WokerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = "__all__"