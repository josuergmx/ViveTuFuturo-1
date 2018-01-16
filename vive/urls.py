from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.principal,name='principal'),
    url(r'^login/',include('login.urls',namespace='login')),
    url(r'^cita/',include('agenda.urls',namespace='agenda')),
    url(r'^asesor/',include('asesor.urls',namespace='asesor')),
    url(r'^ventas/',include('ventas.urls',namespace='ventas')),
    url(r'^sesion1/',include('sesion1.urls',namespace='sesion1')),
    url(r'^cliente/',include('cliente.urls',namespace='cliente')),
    url(r'^creditos/',include('creditos.urls',namespace='conekta')),
    url(r'^productos/',include('productos.urls',namespace='producto')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
