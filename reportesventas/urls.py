from django.conf.urls import url
from reportesventas import views

urlpatterns = [
    url(
        regex=r'^reportes_ventas/$',
        view=views.ReporteVentas.as_view(),
        name='reportes_ventas'
    ),
]
