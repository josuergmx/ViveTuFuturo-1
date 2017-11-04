from django.conf.urls import url
from . import views

<<<<<<< HEAD
urlpatterns = [
    url(regex = r'',view=views.gestionarProducto,name='gestionarProducto'),
    url(regex = r'',view=views.agregarProducto,name='agregarProducto'),
    url(regex = r'',view=views.editarProducto,name='editarProducto'),
    url(regex = r'',view=views.eliminarProducto,name='eliminarProducto'),
]
