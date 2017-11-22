from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import models as modelo

@login_required(redirect_field_name='login:login')
def gestionarProducto(request):
    servicios = modelo.Servicio.objects.all()
    return render(request,"productos/productos_gestionar.html", locals())

@login_required(redirect_field_name='login:login')
def agregarProducto(request):
    return render(request,"productos/productos_add.html")

@login_required(redirect_field_name='login:login')
def editarProducto(request, idServicio):
    return render(request,"productos/productos_editar.html")

@login_required(redirect_field_name='login:login')
def eliminarProducto(request, idservicio):
    if request.method == 'GET':
        servicio = modelo.Servicio.objects.get(idServicio = idservicio)
        servicio.delete()
        messages.add_message(request, messages.SUCCESS, 'El servicio fue eliminado con exito.')
    return redirect(request,"producto:gestionarProducto")

@login_required(redirect_field_name='login:login')
def consultarProducto(request, idservicio):
    servicio = modelo.Servicio.objects.get(idServicio = idservicio)
    return render(request,"productos/productos_show.html", locals())
