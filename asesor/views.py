from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.decorators import login_required
from . import models as mAsesor
from promotor import models as mPromotor
from login import models as mLogin
from login import forms as fLogin
from cliente import forms as fInfo
from . import forms as f
from django.contrib.auth import get_user
from productos import models as mProductos

# Create your views here.
@login_required(redirect_field_name='login:login')
def agregarAsesor(request):
        if request.user.persona.idRol.idRole == 3:
            if request.method == 'POST':
                usuario = fLogin.UserForm(request.POST)
                persona = fInfo.PersonaForm(request.POST)
                direccion = fInfo.DireccionForm(request.POST)
                contacto = fInfo.ContactoForm(request.POST)
                asesor = f.promotorAsesorForm(request.POST)
                if usuario.is_valid():
                    user = usuario.save()
                    rol = mLogin.Roles.objects.get(idRole=2)
                    fecha = request.POST.get("fechaDeNacimiento",None)
                    estadoCivil = request.POST.get("estadoCivil",None)
                    direccion = request.POST.get("idtipodireccion",None)
                    persona = mLogin.Persona.objects.get(user_id=user)
                    nombreaux = request.POST.get("institucion",None)
                    if estadoCivil == "":
                        estado = mLogin.EstadoCivil.objects.get(idEstadoCivil="1")
                    else:
                        estado = mLogin.EstadoCivil.objects.get(idEstadoCivil=estadoCivil)
                    if direccion == "":
                        tipodireccion = mLogin.CatTipodireccion.objects.get(idtipoDireccion="1")
                    else:
                        tipodireccion = mLogin.CatTipodireccion.objects.get(idtipoDireccion=direccion)
                    if request.POST.get("clienteProspecto",None) == "on":
                        prospecto = True
                    else:
                        prospecto = False

                    nombre = nombreaux.split(" ")
                    print(nombre[0])
                    institucion = mProductos.InstitucionFinanciera.objects.get(idInstitucion=nombre[0])
                    mLogin.Persona.objects.filter(user_id=user).update(
                        estadoCivil = estado,
                        fechaDeNacimiento = fecha,
                        idRol = rol,
                        curp = request.POST.get("curp",None),
                        rfc = request.POST.get("rfc",None),
                    )
                    direccion = mLogin.Direccion(
                        idpersona = persona,
                        idtipodireccion = tipodireccion,
                        calle = request.POST.get("calle",None),
                        colonia = request.POST.get("colonia",None),
                        delegacion = request.POST.get("delegacion",None),
                        cp = request.POST.get("cp",None),
                        numinterior = request.POST.get("numinterior",None),
                        numexterior = request.POST.get("numexterior",None),
                    )
                    contacto = mLogin.Contacto(
                        idpersona = persona,
                        celular = request.POST.get("celular",None),
                        telcasa = request.POST.get("telcasa",None),
                        oficina = request.POST.get("oficina",None),
                        facebookid = request.POST.get("facebookid",None),
                    )
                    promotor = mPromotor.promotorAsesor(
                        idAsesor = persona,
                        idPromotor = get_user(request),
                        institucion = institucion,
                        activo = True,
                    )
                    contacto.save()
                    direccion.save()
                    promotor.save()
                    return redirect('asesor:agregar')
                else:
                    context = {
                        "usuario":usuario,
                        "persona":persona,
                        "contacto":contacto,
                        "direccion":direccion,
                    }
                    return  render_to_response('asesor/asesor_add.html',context)

            usuario = fLogin.UserForm()
            persona = fInfo.PersonaForm()
            direccion = fInfo.DireccionForm()
            contacto = fInfo.ContactoForm()
            asesor = f.promotorAsesorForm()
            context = {
                "usuario":usuario,
                "persona":persona,
                "contacto":contacto,
                "direccion":direccion,
                "asesor":asesor,
            }
            return render(request,"asesor/asesor_add.html",context)


@login_required(redirect_field_name='login:login')
def editarAsesor(request,idAsesorPromotor):
    if request.user.persona.idRol.idRole == 3:
        editar = mPromotor.promotorAsesor.objects.get(idAsesorPromotor=idAsesorPromotor)
        if request.method == 'POST':
            usuario = fLogin.UserForm(request.POST,instance=editar.idAsesor.user)
            persona = fInfo.PersonaForm(request.POST,instance=editar.idAsesor)
            asesor = f.promotorAsesorForm(request.POST,instance=editar)

            if usuario.is_valid():
                print(persona)
                usuario.save()
                persona.save()
                asesor.save()
                return redirect('asesor:gestionarAsesor')
        else:
            usuario = fLogin.UserForm(instance=editar.idAsesor.user)
            persona = fInfo.PersonaForm(instance=editar.idAsesor)
            asesor = f.promotorAsesorForm(instance=editar)
            context = {
                "usuario":usuario,
                "persona":persona,
                "asesor":asesor,
            }
            return render(request,"asesor/asesor_editar.html",context)

    else:
        return render(request,'error/404.html')

@login_required(redirect_field_name='login:login')
def eliminarAsesor(request,idAsesorPromotor):
    if request.user.persona.idRol.idRole == 3:
        eliminar = mPromotor.promotorAsesor.objects.get(idAsesorPromotor=idAsesorPromotor)
        mPromotor.promotorAsesor.objects.filter(idAsesorPromotor=eliminar.idAsesorPromotor).update(
            activo = False
        )
        return redirect('asesor:gestionarAsesor')
    else:
        return render(request,'error/404.html')

@login_required(redirect_field_name='login:login')
def asesor(request,idAsesorPromotor):
    if request.user.persona.idRol.idRole == 3:
        promotorAsesor = mPromotor.promotorAsesor.objects.get(idAsesorPromotor=idAsesorPromotor)
        contacto = mLogin.Contacto.objects.filter(idpersona=promotorAsesor.idAsesor)
        direccion = mLogin.Direccion.objects.filter(idpersona=promotorAsesor.idAsesor)
        context = {
            "asesor":promotorAsesor,
            "contactos":contacto,
            "direcciones":direccion,
        }
        return render(request,"asesor/asesor_show.html",context)
    else:
        return render(request,'error/404.html')


@login_required(redirect_field_name='login:login')
def gestionarAsesor(request):
    if request.user.persona.idRol.idRole == 3:
        promotorAsesor = mPromotor.promotorAsesor.objects.filter(idPromotor=request.user)
        context = {
            "promotorAsesor":promotorAsesor,
        }
        return render(request,"asesor/asesor_gestionar.html",context)
    else:
        return render(request,'error/404.html')
