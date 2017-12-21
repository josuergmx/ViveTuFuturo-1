from django.contrib import admin

# Register your models here.
from .models import (
    CatEstatuscita,
    CatTipocita,
    Cita,
)
admin.site.register(CatEstatuscita)
admin.site.register(CatTipocita)

class CitaAdmin(admin.ModelAdmin):
    def Cliente(self, instance):
        return instance.idAsesorCliente.idCliente
    def Asesor(self, instance):
        return instance.idAsesorCliente.idAsesor
    list_display=('Asesor','Cliente','idTipoCita','idEstatus','fecha','direccionCita')

admin.site.register(Cita,CitaAdmin)
