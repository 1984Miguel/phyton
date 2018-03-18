
from django.conf.urls import url
from django.contrib import admin
from promociones import views as promocont
from primera  import views  as primeracont
from contacto  import views  as contactoControlador




urlpatterns = [
    #path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'^$', primeracont.prin , name='iniciogen'),
    url(r'^promociones/$', promocont.home , name="iniciogen"),
    url(r'^promociones/(?P<pk>[0-9]+)$', promocont.detalle , name="promodetail"),
    url(r'^contacto$', contactoControlador.contacta , name="contacta"),
    url(r'^banner/$', promocont.home , name="baner"),
]
