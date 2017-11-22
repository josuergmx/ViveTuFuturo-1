from django.shortcuts import render
from . import forms as f
# Create your views here.

def agenda(request,idAsesorCliente):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        if request.method == "POST":
            agenda = f.agendaForm(request.POST)
            cliente = m.AsesorCliente.objects.get(idAsesorCliente=idAsesorCliente)

            clientec.save()
            contacto.save()
        else:
            cita = f.agendaForm()
            context = {
                "cita":cita,
            }
            return render(request,"agenda/agenda.html",context)
    else:
        return render(request,'error/404.html')

def contactos(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        asesorClientes = m.AsesorCliente.objects.filter(idAsesor=request.user.id)
        context = {
            "clientes":asesorClientes,
        }
        return render(request,"cliente/contactos.html",context)
    else:
        return render(request,'error/404.html')

def calendario(request):
    cita = f.agendaForm()
    context = {
        "cita":cita,
    }
    return render(request,"agenda/calendario.html",context)
