from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^orden/$',
        view=views.orden,
        name='orden'
    ),
	url(
		regex=r'^inicio/$',
		view=views.index,
		name='inicio'
	),
]
