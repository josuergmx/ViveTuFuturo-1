from django.conf.urls import url
from . import views
urlpatterns = [
    url(
        regex=r'^registrar/$',
        view=views.agregarCliente,
        name='agregarCliente'
    ),
    url(
        regex=r'^/(?P<idAsesorCliente>\d+)/$',
        view=views.clientes,
        name='clientes'
    ),
    url(
        regex=r'^gestionar/$',
        view=views.gestionarClientes,
        name='gestionarCliente'
    ),
    url(
        regex=r'^editar/(?P<idAsesorCliente>\d+)$',
        view=views.editar,
        name='editar'
    ),
    url(
        regex=r'^eliminar/(?P<idAsesorCliente>\d+)$',
        view=views.eliminar,
        name='eliminar'
    ),
]
