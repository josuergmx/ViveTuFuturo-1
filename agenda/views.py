from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime,timedelta
from . import forms as f
import cliente.models as m
from . import models as mCita
from cliente import models as mCliente
# Create your views here.

@login_required(redirect_field_name='login:login')
def agenda(request,idAsesorCliente):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        if request.method == "POST":
            tipoCita = request.POST.get("idTipoCita",None)
            estadoCita = request.POST.get("idEstatus",None)
            mes = request.POST.get("fecha_month",None)
            dia = request.POST.get("fecha_day",None)
            ano = request.POST.get("fecha_year",None)
            hora = request.POST.get("hora",None)
            fecha = ano+"-"+mes+"-"+dia+" "+hora
            fecha = datetime.strptime(fecha,"%Y-%m-%d %H:%M")
            direccion = request.POST.get("direccionCita",None)
            descripcion = request.POST.get("descripcion",None)
            estado = mCita.CatEstatuscita.objects.get(idEstatus=estadoCita)
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
                estatusCita = estadoCita,
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

@login_required(redirect_field_name='login:login')
def contactos(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        asesorClientes = m.AsesorCliente.objects.filter(idAsesor=request.user.id)
        cita = []
        sin_agendar = []
        dia = datetime.today().strftime("%Y-%m-%d")
        for i in range(0,len(asesorClientes)):
            try:
                citas = mCita.Cita.objects.get(idAsesorCliente=asesorClientes[i],fecha=asesorClientes[i].fecha)
                print(asesorClientes[i].estatusCita)
                if asesorClientes[i].fecha.strftime("%Y-%m-%d") >= dia and asesorClientes[i].estatusCita != "10":
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

@login_required(redirect_field_name='login:login')
def editar(request,idCita):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        editar = mCita.Cita.objects.get(idCita=idCita)
        if request.method == "POST":
            editar = mCita.Cita.objects.filter(idCita=idCita)
            tipoCita = request.POST.get("idTipoCita",None)
            estadoCita = request.POST.get("idEstatus",None)
            mes = request.POST.get("fecha_month",None)
            dia = request.POST.get("fecha_day",None)
            ano = request.POST.get("fecha_year",None)
            hora = request.POST.get("hora",None)
            fecha = ano+"-"+mes+"-"+dia+" "+hora
            fecha = datetime.strptime(fecha,"%Y-%m-%d %H:%M")
            direccion = request.POST.get("direccionCita",None)
            descripcion = request.POST.get("descripcion",None)
            estado = mCita.CatEstatuscita.objects.get(idEstatus=estadoCita)
            tipoCita = mCita.CatTipocita.objects.get(idTipoCita=tipoCita)
            editar.update(
                idTipoCita = tipoCita,
                idEstatus = estado,
                direccionCita  = direccion,
                descripcion = descripcion,
                fecha = fecha,
            )
            editar = mCita.Cita.objects.get(idCita=idCita)
            mCliente.AsesorCliente.objects.filter(idAsesorCliente=editar.idAsesorCliente.idAsesorCliente).update(
                fecha = fecha,
                estatusCita = estadoCita,
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

@login_required(redirect_field_name='login:login')
def eliminar(request,idCita):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        eliminar = mCita.Cita.objects.filter(idCita=idCita)
        estado = mCita.CatEstatuscita.objects.get(idEstatus=10)
        eliminar.update(
            idEstatus = estado,
        )
        eliminar = mCita.Cita.objects.get(idCita=idCita)
        eliminar = mCliente.AsesorCliente.objects.filter(idAsesorCliente=eliminar.idAsesorCliente.idAsesorCliente)
        eliminar.update(
            estatusCita = "10",
        )
        return redirect('agenda:contactos')
    else:
        return render(request,'error/404.html')

@login_required(redirect_field_name='login:login')
def hoy(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        asesorClientes = mCliente.AsesorCliente.objects.filter(idAsesor=request.user.id)
        hoy1 = []
        hoy2 = []
        iterar = 0
        dia = datetime.today().strftime("%Y-%m-%d")
        for i in asesorClientes:
            print(i.fecha, i.idAsesorCliente)
            try:
                if i.fecha.strftime("%Y-%m-%d") == dia and i.estatusCita != "10":
                    hoy1.append(mCita.Cita.objects.get(idAsesorCliente=i,fecha=i.fecha))
            except:
                pass
        context = {
            "hoy1":hoy1,
        }
        return render(request,"agenda/hoy.html",context)
    else:
        return render(request,'error/404.html')

@login_required(redirect_field_name='login:login')
def historial(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
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
    else:
        return render(request,'error/404.html')

@login_required(redirect_field_name='login:login')
def calendario(request):
    if request.user.persona.idRol.idRole == 2 or request.user.persona.idRol.idRole == 3:
        asesorClientes = m.AsesorCliente.objects.filter(idAsesor=request.user.id)
        cita = []
        hora = []
        minutos = []
        print(len(asesorClientes))
        for i in range(0,len(asesorClientes)):
            try:
                cita.append(mCita.Cita.objects.filter(idAsesorCliente=asesorClientes[i]))
                hora.append(cita[i].hour)
                minutos.append(cita[i].minute)
            except:
                pass
        print(cita)
        context = {
            "cita":cita,
            "hora":hora,
            "minutos":minutos,
        }
        return render(request,"agenda/calendario.html",context)
    else:
        return render(request,'error/404.html')
