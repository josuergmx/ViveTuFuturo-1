# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import(
    CatPais,
    CatEstados,
    Localidad,
    InstitucionFinanciera,
    Departamento,
    Servicio
)

class PaisAdmin(admin.ModelAdmin):
    list_display=('nombre',)

class EstadoAdmin(admin.ModelAdmin):
    list_display=('idPais','nombre')

class LocalidadAdmin(admin.ModelAdmin):
    list_display=('CatPais','CatEstados','nombre')

class InstitucionAdmin(admin.ModelAdmin):
    list_display=('nombre','calle','colonia','cp','num_int','num_ext')

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=('idInstitucion','nombre','ubicacion','telefono','extension')

class ServicioAdmin(admin.ModelAdmin):
    list_display=('idDepartamento','nombrePlan','descripcion')

admin.site.register(CatPais,PaisAdmin)
admin.site.register(CatEstados, EstadoAdmin)
admin.site.register(Localidad, LocalidadAdmin)
admin.site.register(InstitucionFinanciera, InstitucionAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Servicio, ServicioAdmin)
