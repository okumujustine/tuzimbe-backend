from django.db import models




class MeasurementMethod(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class Material(models.Model):
    name = models.CharField(max_length=100)
    mesurements = models.ManyToManyField(MeasurementMethod, related_name="material_mesurement_methods")
    created_at = models.DateTimeField(auto_now_add=True)
