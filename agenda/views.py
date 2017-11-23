from django.shortcuts import render
from . import forms as f
import cliente.models as m
from . import models as mCita
# Create your views here.

def agenda(request,idAsesorCliente):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        if request.method == "POST":
            agenda = f.agendaForm(request.POST)
            if agenda.is_valid():
                tipoCita = request.POST.get("idTipoCita",None)
                estado = request.POST.get("id_idEstatus",None)
                mes = request.POST.get("fecha_month",None)
                dia = request.POST.get("fecha_day",None)
                año = request.POST.get("fecha_year",None)
                direccion = request.POST.get("id_direccionCita",None)
                descripcion = request.POST.get("id_descripcion",None)
                estado = mCita.CatEstatuscita.objects.get(idEstatus=estado)
                tipoCita = mCita.CatTipocita.objects.get(idTipoCita=tipoCita)
                cita = mCita.Cita(
                    idAsesorCliente = idAsesorCliente,
                    idTipoCita = tipoCita,
                    idEstatus = estado,
                    direccionCita  = direccion,
                    descripcion = descripcion,
                    fecha = 
                )
                cita.save()
                return redirect('agenda:contactos')
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
        cita = []
        for i in range(0,len(asesorClientes)):
            cita.append(mCita.Cita.objects.filter(idAsesorCliente=asesorClientes))
        context = {
            "clientes":asesorClientes,
            "citas":cita,
        }
        return render(request,"agenda/contactos.html",context)
    else:
        return render(request,'error/404.html')

def calendario(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        cita = f.agendaForm()
        context = {
            "cita":cita,
        }
        return render(request,"agenda/calendario.html",context)
    else:
        return render(request,'error/404.html')
