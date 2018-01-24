from . import views
from django.conf.urls import url


urlpatterns = [
    url(
        regex=r'^$',
        view=views.mensajes,
        name='mensajes'
    ),
    url(
        regex=r'^mensaje/(?P<idAsesorCliente>\d+)$',
        view=views.mandar_mensaje,
        name='send'
    ),
]
