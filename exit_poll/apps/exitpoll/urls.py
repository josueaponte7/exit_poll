from django.conf.urls import patterns, url
from .views import RegistrarExitPoll, ListarExitPoll, EditarExitPoll, BorrarExitPoll, Candidatos

urlpatterns = patterns('',
                       url(r'^$', ListarExitPoll.as_view(), name='listar_exitpoll'),
                       url(r'^registrarexitpoll/$', RegistrarExitPoll.as_view(), name='registrar_exitpoll'),
                       url(r'^editarexitpoll/(?P<pk>\d+)/$', EditarExitPoll.as_view(), name='editar_exitpoll'),
                       url(r'^borrarexitpoll/(?P<pk>\d+)/$', BorrarExitPoll.as_view(), name='borrar_exitpoll'),
                       url(r'^listarcandidato/$', Candidatos.as_view(), name='candidatos'),
                       )
