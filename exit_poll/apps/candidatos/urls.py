from django.conf.urls import patterns, include, url
from .views import RegistrarCandidatos, ListarCandidatos, BorrarCandidatos, EditarCandidatos
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarCandidatos.as_view(template_name="candidato/listar.html"),
                                                 login_url='/login/'), name='listar_candidato'),
                       url(r'^registrarcandidato/$', login_required(RegistrarCandidatos.as_view(template_name="candidato/candidato.html"),
                                                                    login_url='/login/'), name='registrar_candidato'),
                       url(r'^editarcandidato/(?P<pk>\d+)/$', login_required(EditarCandidatos.as_view(template_name="candidato/modificar.html"),
                                                                             login_url='/login/'), name='editar_candidato'),
                       url(r'^borrarcandidato/(?P<pk>\d+)/$', login_required(BorrarCandidatos.as_view(template_name="candidato/borrar.html"),
                                                                             login_url='/login/'), name='borrar_candidato'),

                       )
