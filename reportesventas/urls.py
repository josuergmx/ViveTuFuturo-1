from django.conf.urls import url
from ventas import views
urlpatterns = [
    url(
        regex=r'^reporte_ventas/$',
        view=views.agregarCliente,
        name='agregarCliente'
    ),
]
