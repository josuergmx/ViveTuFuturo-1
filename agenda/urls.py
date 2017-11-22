from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
    url(
        regex=r'^contactos',
        view=views.contactos,
        name='contactos'
    ),
    url(
        regex=r'^$',
        view=views.calendario,
        name='calendario'
    ),
    url(
        regex=r'^agendar/(?P<idAsesorCliente>\d+)$',
        view=views.agenda,
        name='agendar'
    ),
]
