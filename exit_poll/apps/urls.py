from django.conf.urls import patterns, include, url
from apps.configuraciones.views import Configuraciones

urlpatterns = patterns('',
                       url(r'^$', include('apps.inicio.urls')),
                       url(r'^login/', include('apps.login.urls')),
                       url(r'^menu/', include('apps.menu.urls')),
                       url(r'^configuraciones/', include('apps.configuraciones.urls')),
                       url(r'^partidos/', include('apps.partidos.urls')),
                       url(r'^elecciones/', include('apps.elecciones.urls')),
                       url(r'^exitpoll/', include('apps.exitpoll.urls')),
                       url(r'^candidatos/', include('apps.candidatos.urls')),
                       )
