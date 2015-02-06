from django.conf.urls import patterns, include, url
from .views import RegistrarParroquia, ListarParroquia, EditarParroquia, BorrarParroquia
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^registrarparroquia/$', login_required(RegistrarParroquia.as_view(template_name="topologia/parroquias/parroquias.html"),
                                                     login_url='/login/'), name='registrar_parroquia'),
                       url(r'^editarparroquia/(?P<pk>\d+)/$', login_required(EditarParroquia.as_view(template_name="topologia/parroquias/modificar.html"),
                                                     login_url='/login/'), name='editar_parroquia'),
                       url(r'^borrarparroquia/(?P<pk>\d+)/$', login_required(BorrarParroquia.as_view(template_name="topologia/parroquias/borrar.html"),
                                                     login_url='/login/'), name='borrar_parroquia'),
                       url(r'^$', login_required(ListarParroquia.as_view(template_name="topologia/parroquias/listar.html"),
                                                     login_url='/login/'), name='listar_parroquia'),
                       )
