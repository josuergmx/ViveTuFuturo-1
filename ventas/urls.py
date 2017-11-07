from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^reporte/$',
        view=views.ReporteVentas.as_view(),
        name='reporte'
    ),
]
