from django.conf.urls import patterns, include, url
from .views import RegistrarPartidos, ListarPartidos, BorrarPartidos, EditarPartidos
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarPartidos.as_view(template_name="partido/listar.html"),
                                                 login_url='/login/'), name='listar_partido'),
                       url(r'^registrarpartido/$', login_required(RegistrarPartidos.as_view(template_name="partido/partido.html"),
                                                 login_url='/login/'), name='registrar_partido'),
                       url(r'^editarpartido/(?P<pk>\d+)/$', login_required(EditarPartidos.as_view(template_name="partido/modificar.html"),
                                                 login_url='/login/'), name='editar_partido'),
                       url(r'^borrarpartido/(?P<pk>\d+)/$', login_required(BorrarPartidos.as_view(template_name="partido/borrar.html"),
                                                 login_url='/login/'), name='borrar_partido'),

                       )
