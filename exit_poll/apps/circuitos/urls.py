from django.conf.urls import patterns, include, url
from .views import RegistrarCircuito, ListarCircuito, BorrarCircuito, EditarCircuito
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarCircuito.as_view(template_name="circuito/listar.html"),
                                                 login_url='/login/'), name='listar_circuito'),
                       url(r'^registrarcircuito/$', login_required(RegistrarCircuito.as_view(template_name="circuito/circuito.html"),
                                                 login_url='/login/'), name='registrar_circuito'),
                       url(r'^editarcircuito/(?P<pk>\d+)/$', login_required(EditarCircuito.as_view(template_name="circuito/modificar.html"),
                                                 login_url='/login/'), name='editar_circuito'),
                       url(r'^borrarcircuito/(?P<pk>\d+)/$', login_required(BorrarCircuito.as_view(template_name="circuito/borrar.html"),
                                                 login_url='/login/'), name='borrar_circuito'),
                       )
