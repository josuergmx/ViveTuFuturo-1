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
        regex=r'^eliminar/$',
        view=views.eliminarAsesor,
        name='eliminar'
    ),
    url(
        regex=r'^editar/$',
        view=views.editarAsesor,
        name='editar'
    ),
]
