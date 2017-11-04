from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex = r'',view=views.gestionr,name='gestionarProducto'),
    url(regex = r'',view=views.gestionr,name='agregarProducto'),
    url(regex = r'',view=views.gestionr,name='editarProducto'),
    url(regex = r'',view=views.gestionr,name='eliminarProducto'),
]
