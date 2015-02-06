from django.conf.urls import patterns, include, url
from apps.configuraciones.views import Topologia
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(Topologia.as_view(template_name="configuraciones/topologia.html"),
                                                 login_url='/login/')),
                       url(r'^estados/', include('apps.topologia.estados.urls')),
                       url(r'^municipios/', include('apps.topologia.municipios.urls')),
                       url(r'^parroquias/', include('apps.topologia.parroquias.urls')),

                       )
