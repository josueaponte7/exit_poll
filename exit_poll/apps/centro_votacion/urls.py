from django.conf.urls import patterns, include, url
from .views import RegistrarCentros, ListarCentros, BorrarCentros, EditarCentros
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarCentros.as_view(template_name="centros/listar.html"),
                                                 login_url='/login/'), name='listar_centros'),
                       url(r'^registrarcentros/$', login_required(RegistrarCentros.as_view(template_name="centros/centros.html"),
                                                 login_url='/login/'), name='registrar_centros'),
                       url(r'^editarcentros/(?P<pk>\d+)/$', login_required(EditarCentros.as_view(template_name="centros/modificar.html"),
                                                 login_url='/login/'), name='editar_centros'),
                       url(r'^borrarcentros/(?P<pk>\d+)/$', login_required(BorrarCentros.as_view(template_name="centros/borrar.html"),
                                                 login_url='/login/'), name='borrar_centros'),

                       )
