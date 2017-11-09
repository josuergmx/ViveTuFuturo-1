from django.conf.urls import url
from . import views

urlpatterns = [
    url(regex = r'^gestionar/$',view=views.gestionarProducto,name='gestionarProducto'),
    url(regex = r'^registrar/$',view=views.agregarProducto,name='agregarProducto'),
    url(regex = r'^editar/$',view=views.editarProducto,name='editarProducto'),
    url(regex = r'^eliminar/(?P<idservicio>\d+)$',view=views.eliminarProducto,name='eliminarProducto'),
    url(regex = r'^(?P<idservicio>\d+)$',view=views.consultarProducto,name='consultarProducto'),
]
