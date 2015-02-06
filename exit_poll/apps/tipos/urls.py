from django.conf.urls import patterns, include, url
from apps.configuraciones.views import Tipos_Eleccion
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(Tipos_Eleccion.as_view(template_name="configuraciones/categoria_eleccion.html"),
                                                 login_url='/login/')),
                       url(r'^categorias/', include('apps.tipos.categoria_eleccion.urls')),
                       url(r'^tipos/', include('apps.tipos.tipo_eleccion.urls')),

                       )
