from django.conf.urls import url
from .views import(
    ReporteView,
    GeneracionDepartamentos,
    GeneracionServicios
)

app_name="reportes"
urlpatterns = [
    url(r'^$', GeneracionDepartamentos.as_view(), name="reportes"),
    url(r'^reportes/servicios/$', GeneracionServicios.as_view(), name="servicios"),
    url(r'^reportes/generacion/$', ReporteView.as_view(), name="generacion"),
]
