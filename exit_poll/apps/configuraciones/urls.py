from django.conf.urls import patterns, include, url
from .views import Configuraciones
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(Configuraciones.as_view(template_name="configuraciones/configuraciones.html"),
                                                 login_url='/login/')),
                       url(r'^topologia/', include('apps.topologia.urls')),
                       url(r'^circuitos/', include('apps.circuitos.urls')),
                       url(r'^grupo_etareo/', include('apps.grupo_etareo.urls')),
                       url(r'^tipo_eleccion/', include('apps.tipos.urls')),
                       url(r'^centros/', include('apps.centro_votacion.urls')),
                       )
