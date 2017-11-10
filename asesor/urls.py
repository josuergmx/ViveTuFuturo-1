from django.conf.urls import url
from . import views
urlpatterns = [
    url(
        regex=r'^gestionar/$',
        view=views.gestionarAsesor,
        name='gestionar'
    ),
    url(
        regex=r'^agregar/$',
        view=views.agregarAsesor,
        name='agregar'
    ),
    url(
        regex=r'^ver/(?P<idAsesor>\d+)$',
        view=views.asesor,
        name='asesor'
    ),
    url(
        regex=r'^eliminar/(?P<idAsesor>\d+)$',
        view=views.eliminarAsesor,
        name='eliminar'
    ),
    url(
        regex=r'^editar/(?P<idAsesor>\d+)$',
        view=views.editarAsesor,
        name='editar'
    ),
]
