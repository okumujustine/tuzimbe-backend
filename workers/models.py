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


class DailyWork(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField()
    departure_time = models.DateTimeField()
    daily_rate = models.IntegerField()
    daily_rate_currency = models.CharField(max_length=10, default="UGX")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created_at} {self.worker.first_name} {self.worker.last_name}"