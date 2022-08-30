from django.contrib import admin

from .models import (
    Material,
    MeasurementMethod,
    MaterialUsage,
)

admin.site.register(Material)
admin.site.register(MeasurementMethod)
admin.site.register(MaterialUsage)