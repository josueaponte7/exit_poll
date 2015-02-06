from django.conf.urls import patterns, include, url
from .views import RegistrarCategoria, ListarCategoria, BorrarCategoria, EditarCategoria
from apps.configuraciones.views import Tipos_Eleccion
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarCategoria.as_view(template_name="categoria_eleccion/listar.html"),
                                                 login_url='/login/'), name='listar_categoria'),
                       url(r'^registrarcategoria/$', login_required(RegistrarCategoria.as_view(template_name="categoria_eleccion/categoria.html"),
                                                 login_url='/login/'), name='registrar_categoria'),
                       url(r'^editarcategoria/(?P<pk>\d+)/$',login_required(EditarCategoria.as_view(template_name="categoria_eleccion/modificar.html"),
                                                 login_url='/login/'), name='editar_categoria'),
                       url(r'^borrarcategoria/(?P<pk>\d+)/$', login_required(BorrarCategoria.as_view(template_name="categoria_eleccion/borrar.html"),
                                                 login_url='/login/'), name='borrar_categoria'),

                       )
