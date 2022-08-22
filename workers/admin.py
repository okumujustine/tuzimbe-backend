from django.contrib import admin
from .models import (
    Worker,
    DailyWork,
)

admin.site.register(Worker)
admin.site.register(DailyWork)