from django.conf.urls import patterns, include, url
from .views import Menu
from django.contrib.auth.decorators import login_required
from apps.configuraciones.views import Configuraciones


urlpatterns = patterns('',
                       url(r'^$', login_required(Menu.as_view(template_name="base.html"), login_url='/login/')),
                       url(r'^/', include('apps.configuraciones.urls')),

                       )
