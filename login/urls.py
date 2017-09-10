from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    url(
        regex=r'^registrar/$',
        view=views.registrar,
        name='registrar'
    ),
    url(
        regex=r'^login/$',
        view=views.login,
        name='login',
    ),
    url(
        regex=r'^hola/$',
        view=views.hola,
        name='hola'
    ),
]
