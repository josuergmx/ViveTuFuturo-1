from __future__ import unicode_literals
from django.contrib import admin
from .models import(
    PlanesConcretados,
    PlazoPagos
)

class PlanesConcretadosAdmin(admin.ModelAdmin):
    list_display=('formaPago','fechaContratacion', 'numeroPoliza', 'primaNetaAnual', 'plazoAnos', 'valorPlan')

class PlazoPagosAdmin(admin.ModelAdmin):
    list_display=('nombrePlazo',)

# Register your models here.
admin.site.register(PlanesConcretados, PlanesConcretadosAdmin)
admin.site.register(PlazoPagos, PlazoPagosAdmin)
