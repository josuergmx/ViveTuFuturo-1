from __future__ import unicode_literals

from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login:login')
def gestionarProducto(request):
    return render(request,"productos/productos_gestionar.html")

@login_required(redirect_field_name='login:login')
def agregarProducto(request):
    pass

@login_required(redirect_field_name='login:login')
def editarProducto(request):
    pass

@login_required(redirect_field_name='login:login')
def eliminarProducto(request):
    pass
