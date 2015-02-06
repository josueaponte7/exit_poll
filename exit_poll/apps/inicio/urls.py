from django.conf.urls import patterns, include, url
from .views import Inicio
#from apps.configuraciones.views import Configuraciones

urlpatterns = patterns('',
                       url(r'^$', Inicio.as_view()),
                       #url(r'^/', include('apps.configuraciones.urls')),
                       )
