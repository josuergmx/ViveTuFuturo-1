from django.contrib import admin

# Register your models here.
from .models import CatPais, CatEstados, Localidades, Institucionfinanciera, Departamento, Servicios, EstadoCivil, Persona, PlanesConcretados, Roles

class CatPaisAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nombre"]
    search_fields = ["nombre"] #Campo para realizar busquedas
    list_filter = ["nombre"] #Se filtran las busquedas por precio
    list_editable = ["nombre"] #El campo sale_price se vuelve editable
    class Meta:
        model = CatPais

class CatEstadosAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nombre"]
    search_fields = ["nombre"] #Campo para realizar busquedas
    list_filter = ["nombre"] #Se filtran las busquedas por precio
    list_editable = ["nombre"] #El campo sale_price se vuelve editable
    class Meta:
        model = CatEstados

class LocalidadesAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nombre"]
    search_fields = ["nombre"] #Campo para realizar busquedas
    list_filter = ["nombre"] #Se filtran las busquedas por precio
    list_editable = ["nombre"] #El campo sale_price se vuelve editable
    class Meta:
        model = Localidades

class InstitucionfinancieraAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nombre", "calle", "coloniaMunicipio","cp", "numExterior", "numeroInterior"]
    search_fields = ["nombre", "cp", "coloniaMunicipio"] #Campo para realizar busquedas
    list_filter = ["nombre", "coloniaMunicipio", "cp"] #Se filtran las busquedas por precio
    list_editable = ["numExterior", "numeroInterior"] #El campo sale_price se vuelve editable
    class Meta:
        model = Institucionfinanciera

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nombre", "ubicacion", "telefono","extension"]
    search_fields = ["nombre", "telefono"] #Campo para realizar busquedas
    list_filter = ["nombre"] #Se filtran las busquedas por precio
    list_editable = ["telefono"] #El campo sale_price se vuelve editable
    class Meta:
        model = Departamento

class ServiciosAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nombrePlan", "descripcion"]
    search_fields = ["nombrePlan"] #Campo para realizar busquedas
    list_filter = ["nombrePlan"] #Se filtran las busquedas por precio
    class Meta:
        model = Departamento

class PersonaAdmin(admin.ModelAdmin):
    def user_email(self, instance):
        return instance.user.email

    def user_last(self, instance):
        return instance.user.last_name
    list_display=['user','user_last','idRol','estadoCivil','user_email']
    list_editable = ["estadoCivil"]

class EstadoCivilAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nombre"]
    search_fields = ["nombre"] #Campo para realizar busquedas
    list_filter = ["nombre"] #Se filtran las busquedas por precio
    class Meta:
        model = EstadoCivil

class RolesAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nombre", "descripcion"]
    search_fields = ["nombre"] #Campo para realizar busquedas
    list_filter = ["nombre"] #Se filtran las busquedas por precio
    class Meta:
        model = Roles

class PlanesConcretadosAdmin(admin.ModelAdmin):
    list_display = ["__str__", "idPlan", "idAsesor", "idCliente", "idServicio", "fechaContratacion"]
    search_fields = ["idPlan","fechaContratacion"] #Campo para realizar busquedas
    list_filter = ["idPlan","fechaContratacion"] #Se filtran las busquedas por precio
    class Meta:
        model = PlanesConcretados


admin.site.register(CatPais, CatPaisAdmin),
admin.site.register(CatEstados, CatEstadosAdmin),
admin.site.register(Localidades, LocalidadesAdmin),
admin.site.register(Institucionfinanciera, InstitucionfinancieraAdmin),
admin.site.register(Departamento, DepartamentoAdmin),
admin.site.register(Servicios, ServiciosAdmin),
admin.site.register(EstadoCivil, EstadoCivilAdmin),
admin.site.register(Persona, PersonaAdmin),
admin.site.register(PlanesConcretados, PlanesConcretadosAdmin),
admin.site.register(Roles, RolesAdmin),
