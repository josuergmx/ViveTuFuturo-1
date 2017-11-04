from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
    url(
        regex=r'^$',
        view=views.agenda,
        name='agenda'
    ),

]
