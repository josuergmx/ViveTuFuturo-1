from django.shortcuts import render
from . import models as m

# Create your views here.


def mensajes(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        pass
    elif request.user.persona.idRol.idRole == 1:
        
        return render(request,'mensajes/mensajes_cliente.html')
    else:
        return render(request,'error/404.html')
