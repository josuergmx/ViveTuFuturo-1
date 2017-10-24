from django.contrib import admin

# Register your models here.

from .models import (
    Asesor,
    ReporteActividad,
)
admin.site.register(Asesor)
admin.site.register(ReporteActividad)
