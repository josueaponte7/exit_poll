from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from apps.topologia.estados.viewsets import EstadoViewSet
from apps.topologia.municipios.viewsets import MunicipioViewSet
from apps.topologia.parroquias.viewsets import ParroquiaViewSet
from apps.circuitos.viewsets import CircuitoViewSet
from apps.grupo_etareo.viewsets import Grupo_EtareoViewSet
from apps.tipos.categoria_eleccion.viewsets import CategoriaViewSet
from apps.tipos.tipo_eleccion.viewsets import Tipo_eleccionViewSet
from apps.centro_votacion.viewsets import CentrosViewSet
from apps.partidos.viewsets import PartidosViewSet
from apps.elecciones.viewsets import EleccionViewSet
from apps.exitpoll.viewsets import ExitPollViewSet
import settings


router = DefaultRouter()
router.register(r'estado', EstadoViewSet)
router.register(r'municipio', MunicipioViewSet)
router.register(r'parroquia', ParroquiaViewSet)
router.register(r'circuito', CircuitoViewSet)
router.register(r'grupo_etareo', Grupo_EtareoViewSet)
router.register(r'categoria_eleccion', CategoriaViewSet)
router.register(r'tipo_eleccion', Tipo_eleccionViewSet)
router.register(r'centros', CentrosViewSet)
router.register(r'partidos', PartidosViewSet)
router.register(r'elecciones', EleccionViewSet)
router.register(r'exitpoll', ExitPollViewSet)


urlpatterns = patterns('',
                       url(r'^chaining/', include('pixelfields_smart_selects.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(router.urls)),
                       url(r'^', include('apps.urls')),
                       url(r'^imagenes/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.MEDIA_ROOT}),
		       url(r'^', include('apps.exitpoll.urls')),
                       url(r'^', include('apps.votacion.urls')),
                       )
