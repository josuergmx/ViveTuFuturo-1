from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.principal,name='principal'),
    url(r'^login/',include('login.urls',namespace='login')),
    url(r'^asesor/',include('asesor.urls',namespace='asesor')),
    url(r'^creditos/',include('creditos.urls',namespace='conekta')),
    url(r'^cliente/',include('cliente.urls',namespace='cliente')),
    url(r'^ventas/',include('ventas.urls',namespace='ventas')),
<<<<<<< HEAD
]
=======
    url(r'^productos/',include('productos.urls',namespace='productos')),
]

>>>>>>> fffb3d5fc45af0122ab9f7b630c33dd44174d5ef
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
