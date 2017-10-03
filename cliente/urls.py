from django.conf.urls import url
from . import views
urlpatterns = [
    url(
        regex=r'^registrar/$',
        view=views.agregarCliente,
        name='agregarCliente'
    ),
    url(
        regex=r'^$',
        view=views.clientes,
        name='clientes'
    ),
    url(
        regex=r'^gestionar/$',
        view=views.gestionarClientes,
        name='gestionarCliente'
    ),
]
