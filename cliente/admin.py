from django.contrib import admin

# Register your models here.

from .models import (
    RecomendadoCliente,
    AsesorCliente,
    OrigenRecomendacion,
    Estatus
)
admin.site.register(RecomendadoCliente)

class AsesorClienteAdmin(admin.ModelAdmin):
    def asesor(self, instance):
        return instance.idAsesor.first_name

    def cliente(self, instance):
        return instance.idCliente.user.last_name

        
    list_display=('asesor','cliente','Estatus','fechaActualizacion')

admin.site.register(AsesorCliente,AsesorClienteAdmin)

admin.site.register(OrigenRecomendacion)
admin.site.register(Estatus)
