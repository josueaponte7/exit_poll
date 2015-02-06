from django.conf.urls import patterns, include, url
from .views import RegistrarGrupo_Etareo, ListarGrupo_Etareo, BorrarGrupo_Etareo, EditarGrupo_Etareo
from django.contrib.auth.decorators import login_required


urlpatterns = patterns('',
                       url(r'^$', login_required(ListarGrupo_Etareo.as_view(template_name="grupo_etareo/listar.html"),
                                                 login_url='/login/'), name='listar_grupo_etareo'),
                       url(r'^registrargrupo_etareo/$', login_required(RegistrarGrupo_Etareo.as_view(template_name="grupo_etareo/grupo_etareo.html"),
                                                 login_url='/login/'), name='registrar_grupo_etareo'),
                       url(r'^editargrupo_etareo/(?P<pk>\d+)/$', login_required(EditarGrupo_Etareo.as_view(template_name="grupo_etareo/modificar.html"),
                                                 login_url='/login/'), name='editar_grupo_etareo'),
                       url(r'^borrargrupo_etareo/(?P<pk>\d+)/$', login_required(BorrarGrupo_Etareo.as_view(template_name="grupo_etareo/borrar.html"),
                                                 login_url='/login/'), name='borrar_grupo_etareo'),

                       )
