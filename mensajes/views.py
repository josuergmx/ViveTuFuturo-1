from django.shortcuts import render
from . import models as m
from cliente import models as mc
# Create your views here.
def mensajes(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3: #El cliente manda el mensaje
        try:
            asesorCliente = mc.AsesorCliente.objects.filter(idAsesor=request.user)
        except:
            asesorCliente = "No tienes clientes"
        try:
            mensajes = {}
        except:
            mensajes = "No hay mensajes"

        return render(request,'mensajes/mensajes_asesor.html')

    elif request.user.persona.idRol.idRole == 1: #Tipo 2 el manda el cliente manda el mensaje
        try:
            asesorCliente = mc.AsesorCliente.objects.filter(idCliente=request.user.persona)
        except:
            asesorcliente = "No tienes clientes"
        mensajes = {}
        j = 0
        print(asesorCliente[0].idAsesor.username)
        for i in asesorCliente:
            try:
                mensajes[j] = m.Mensajes.objects.filter(idAsesorCliente=asesorCliente[i]).order_by('fecha')
            except:
                mensajes[j] = "No hay mensajes"
            j = j + 1
        print(mensajes)
        context = {
            'mensajes':mensajes,
            'asesorCliente':asesorCliente
        }
        return render(request,'mensajes/mensajes_cliente.html',context)
    else:
        return render(request,'error/404.html')


def mandar_mensaje(request):
    pass
