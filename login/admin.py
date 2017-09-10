from django.contrib import admin

# Register your models here.

from .models import (
    Direccion,
    Roles,
    EstadoCivil,
    CatTipodireccion,
    Persona,
    Contacto
)
admin.site.register(Direccion)
admin.site.register(Roles)
admin.site.register(EstadoCivil)
admin.site.register(CatTipodireccion)
admin.site.register(Persona)
admin.site.register(Contacto)
