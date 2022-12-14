from django.db import models




class MeasurementMethod(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=100)
    mesurements = models.ManyToManyField(MeasurementMethod, related_name="material_mesurement_methods")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MaterialUsage(models.Model):
    measurement_method = models.ForeignKey(MeasurementMethod, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    price_currency = models.CharField(max_length=10, default='UGX')
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    added_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.material}: {self.quantity}"

