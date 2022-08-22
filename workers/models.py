from django.db import models

# Create your models here.
class Worker(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    main_daily_rate = models.IntegerField()
    main_rate_currency = models.CharField(max_length=10, default="UGX")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"