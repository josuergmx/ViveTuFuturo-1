from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^reportes/$',
        view=views.ReporteVentas.as_view(),
        name='reportes_'
    ),
]
