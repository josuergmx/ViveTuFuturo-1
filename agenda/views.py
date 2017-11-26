from django.shortcuts import render,redirect
from datetime import datetime,timedelta
from . import forms as f
import cliente.models as m
from . import models as mCita
from cliente import models as mCliente
# Create your views here.

def agenda(request,idAsesorCliente):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        if request.method == "POST":
            agenda = f.agendaForm(request.POST)
            if agenda.is_valid():
                tipoCita = request.POST.get("idTipoCita",None)
                estado = request.POST.get("idEstatus",None)
                mes = request.POST.get("fecha_month",None)
                dia = request.POST.get("fecha_day",None)
                año = request.POST.get("fecha_year",None)
                hora = request.POST.get("hora",None)
                fecha = año+"-"+mes+"-"+dia+" "+hora
                fecha = datetime.strptime(fecha,"%Y-%m-%d %H:%M")
                print(fecha)
                direccion = request.POST.get("direccionCita",None)
                descripcion = request.POST.get("descripcion",None)
                estado = mCita.CatEstatuscita.objects.get(idEstatus=estado)
                tipoCita = mCita.CatTipocita.objects.get(idTipoCita=tipoCita)
                asesorCliente = mCliente.AsesorCliente.objects.get(idAsesorCliente=idAsesorCliente)
                cita = mCita.Cita(
                    idAsesorCliente = asesorCliente,
                    idTipoCita = tipoCita,
                    idEstatus = estado,
                    direccionCita  = direccion,
                    descripcion = descripcion,
                    fecha = fecha,
                )
                mCliente.AsesorCliente.objects.filter(idAsesorCliente=idAsesorCliente).update(
                    fecha = fecha,
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
        sin_agendar = []
        dia = datetime.today().strftime("%Y-%m-%d")
        for i in range(0,len(asesorClientes)):
            try:
                citas = mCita.Cita.objects.get(idAsesorCliente=asesorClientes[i],fecha=asesorClientes[i].fecha)
                if asesorClientes[i].fecha.strftime("%Y-%m-%d") >= dia:
                    cita.append(citas)
                else:
                    sin_agendar.append(asesorClientes[i])
            except:
                sin_agendar.append(asesorClientes[i])
        if len(sin_agendar) == 0:
            bien = 1
        else:
            bien = 0
        context = {
            "clientes":asesorClientes,
            "sin_cita":sin_agendar,
            "citas":cita,
            "bien":bien,
        }
        return render(request,"agenda/contactos.html",context)
    else:
        return render(request,'error/404.html')

def editar(request,idCita):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        editar = mCita.Cita.objects.get(idCita=idCita)
        if request.method == "POST":
            cita = f.agendaForm(request.POST,instance=editar)
            if cita.is_valid():
                cita = cita.save()
                mes = request.POST.get("fecha_month",None)
                dia = request.POST.get("fecha_day",None)
                año = request.POST.get("fecha_year",None)
                hora = request.POST.get("hora",None)
                fecha = año+"-"+mes+"-"+dia+" "+hora
                fecha = datetime.strptime(fecha,"%Y-%m-%d %H:%M")
                mCita.Cita.objects.filter(idCita=cita.idCita).update(
                    fecha = fecha,
                )
                mCliente.AsesorCliente.objects.filter(idAsesorCliente=idAsesorCliente).update(
                    fecha = fecha,
                )
                return redirect('agenda:contactos')
        else:
            cita = f.agendaForm(instance=editar)
            context = {
                "cita":cita,
            }
            return render(request,"agenda/agenda.html",context)

    else:
        return render(request,'error/404.html')

def hoy(request):
    asesorClientes = mCliente.AsesorCliente.objects.filter(idAsesor=request.user.id)
    hoy1 = []
    hoy2 = []
    iterar = 0
    dia = datetime.today().strftime("%Y-%m-%d")
    for i in asesorClientes:
        if i.fecha.strftime("%Y-%m-%d") == dia:
            if iterar%2 == 0:
                hoy1.append(mCita.Cita.objects.get(idAsesorCliente=i,fecha=i.fecha))
            else:
                hoy2.append(mCita.Cita.objects.get(idAsesorCliente=i,fecha=i.fecha))
        iterar = iterar + 1
    context = {
        "hoy1":hoy1,
        "hoy2":hoy2,
    }
    return render(request,"agenda/hoy.html",context)

def historial(request):
    asesorClientes = mCliente.AsesorCliente.objects.filter(idAsesor=request.user.id)
    historial1 = []
    historial2 = []
    iterar = 0
    for i in asesorClientes:
        try:
            if iterar%2 == 0:
                historial1.append(mCita.Cita.objects.filter(idAsesorCliente=i))
                print(historial1)
            else:
                historial2.append(mCita.Cita.objects.filter(idAsesorCliente=i))
        except:
            pass
        iterar = iterar + 1

    context = {
        "historial1":historial1,
        "historial2":historial2,
    }
    return render(request,"agenda/historial.html",context)

def calendario(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        asesorClientes = m.AsesorCliente.objects.filter(idAsesor=request.user.id)
        cita = []
        hora = []
        minutos = []
        for i in range(0,len(asesorClientes)):
            try:
                cita.append(mCita.Cita.objects.get(idAsesorCliente=asesorClientes[i]))
                hora.append(cita[i].hour)
                minutos.append(cita[i].minute)
            except:
                pass
        context = {
            "cita":cita,
            "hora":hora,
            "minutos":minutos,
        }
        return render(request,"agenda/calendario.html",context)
    else:
        return render(request,'error/404.html')
