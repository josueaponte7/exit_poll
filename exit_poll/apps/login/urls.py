from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from .views import login_view, logout_view


#Declaramos la salida de las url
urlpatterns = patterns('',
                       url(r'^$', login_view, name='vista_login'),
                       url(r'^logout/$', logout_view, name='vista_logout'),
                       #url(r'^add_user/$', 'add_user_view', name='add_user'),
                       )
