from django.contrib import admin

# Register your models here.

from .models import (
    RecomendadoCliente,
    AsesorCliente,
    OrigenRecomendacion,
    Estatus
)
admin.site.register(RecomendadoCliente)
admin.site.register(AsesorCliente)
admin.site.register(OrigenRecomendacion)
admin.site.register(Estatus)
