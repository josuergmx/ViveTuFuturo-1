from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


urlpatterns = [
    url(r'^login/$',auth_views.login,{'template_name':'log/login.html'},'login'),
    url(r'^logout/$',auth_views.logout_then_login,{'template_name':'log/logout.html'},'hola'),
    url(
        regex=r'^registrar/$',
        view=views.registrar,
        name='registrar'
    ),
    url(
        regex=r'^hola/$',
        view=views.hola,
        name='hola'
    ),
]
