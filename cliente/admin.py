from django.contrib import admin

# Register your models here.

from .models import (
    Estatus,
    OrigenRecomendacion,
    AsesorCliente,
    RecomendadoCliente
)
admin.site.register(AsesorCliente)
admin.site.register(OrigenRecomendacion)
admin.site.register(Estatus)
admin.site.register(RecomendadoCliente)
