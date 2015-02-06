from django.conf.urls import patterns, include, url
from .views import RegistrarEleccion, ListarEleccion, BorrarEleccion, EditarEleccion
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarEleccion.as_view(template_name="elecciones/listar.html"),
                                                 login_url='/login/'), name='listar_eleccion'),
                       url(r'^registrareleccion/$', login_required(RegistrarEleccion.as_view(template_name="elecciones/eleccion.html"),
                                                 login_url='/login/'), name='registrar_eleccion'),
                       url(r'^editareleccion/(?P<pk>\d+)/$', login_required(EditarEleccion.as_view(template_name="elecciones/modificar.html"),
                                                 login_url='/login/'), name='editar_eleccion'),
                       url(r'^borrareleccion/(?P<pk>\d+)/$', login_required(BorrarEleccion.as_view(template_name="elecciones/borrar.html"),
                                                 login_url='/login/'), name='borrar_eleccion'),

                       )
