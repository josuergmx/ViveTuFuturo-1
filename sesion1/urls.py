from django.conf.urls import url
from . import views
urlpatterns = [
    url(
        regex=r'^$',
        view=views.sesion1,
        name='sesion1'
    ),
]
