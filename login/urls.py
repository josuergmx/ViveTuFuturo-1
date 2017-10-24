from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    url(r'^logout/$',auth_views.logout,{'template_name':'hola.html'},'logout'),
    url(
        regex=r'^login/$',
        view=views.login,
        name='login'
    ),
    url(
        regex=r'^hola/$',
        view=views.hola,
        name='hola'
    ),
    url(
        regex=r'^seleccion/$',
        view=views.tipo,
        name='tipo'
    ),
]
