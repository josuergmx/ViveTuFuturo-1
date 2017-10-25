from django.conf.urls import url
from reportesventas import views

urlpatterns = [
    url(
        regex=r'^reportes_ventas/$',
        view=views.ventas,
        name='reportes_ventas'
    ),
]
