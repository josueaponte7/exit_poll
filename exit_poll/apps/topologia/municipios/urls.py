from django.conf.urls import patterns, include, url
from .views import RegistrarMunicipio, ListarMunicipio, EditarMunicipio, BorrarMunicipio
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^registrarmunicipio/$', login_required(RegistrarMunicipio.as_view(template_name="topologia/municipios/municipios.html"),
                                                     login_url='/login/'), name='registrar_municipio'),
                       url(r'^editarmunicipio/(?P<pk>\d+)/$', login_required(EditarMunicipio.as_view(template_name="topologia/municipios/modificar.html"),
                                                     login_url='/login/'), name='editar_municipio'),
                       url(r'^borrarmunicipio/(?P<pk>\d+)/$', login_required(BorrarMunicipio.as_view(template_name="topologia/municipios/borrar.html"),
                                                     login_url='/login/'), name='borrar_municipio'),
                       url(r'^$', login_required(ListarMunicipio.as_view(template_name="topologia/municipios/listar.html"),
                                                 login_url='/login/'), name='listar_municipio'),
                       )
