from django.shortcuts import render,render_to_response
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
            mensajes = m.Mensajes.objects.filter(idAsesorCliente=asesorCliente[0]).order_by('fecha')
        except:
            mensajes = "No hay mensajes"

        return render(request,'mensajes/mensajes_asesor.html')

    elif request.user.persona.idRol.idRole == 1: #Tipo 2 el manda el cliente manda el mensaje
        if request.is_ajax() and request.method == 'POST':
            print('hola')
            pass
        asesorCliente = mc.AsesorCliente.objects.filter(idCliente=request.user.persona)
        try:
            mensajes = m.Mensajes.objects.filter(idAsesorCliente=asesorCliente[0]).order_by('fecha')
        except:
            mensajes = "No hay mensajes"

        context = {
            'mensajes':mensajes,
            'asesorCliente':asesorCliente
        }

        return render(request,'mensajes/mensajes_cliente.html',context)

    else:
        return render(request,'error/404.html')


def mandar_mensaje(request,idAsesorCliente):

    pass
