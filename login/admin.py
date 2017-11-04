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

class PersonaAdmin(admin.ModelAdmin):
    def user_email(self, instance):
        return instance.user.email

    def user_last(self, instance):
        return instance.user.last_name
    list_display=('user','user_last','idRol','estadoCivil','user_email')

admin.site.register(Persona,PersonaAdmin)

class DireccionAdmin(admin.ModelAdmin):
     list_display=('idpersona','idtipodireccion','calle','colonia')


admin.site.register(Direccion,DireccionAdmin)

class ContactoAdmin(admin.ModelAdmin):
     list_display=('idpersona','celular')

admin.site.register(Contacto,ContactoAdmin)


admin.site.register(Roles)
admin.site.register(EstadoCivil)
admin.site.register(CatTipodireccion)
