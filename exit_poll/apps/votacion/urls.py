from django.conf.urls import patterns, include, url
from .views import ListarVotacion, RegistrarVotacion

urlpatterns = patterns('',
                       #url(r'^listarcandidato/$', ListarVotacion.as_view(), name='listar_votacion'),
                       url(r'^votar/(?P<pk>\d+)$', RegistrarVotacion.as_view(), name='votar'),
                       )
