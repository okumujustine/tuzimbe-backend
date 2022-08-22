from django.contrib import admin

from .models import (
    Material,
    MeasurementMethod,
)

admin.site.register(Material)
admin.site.register(MeasurementMethod)