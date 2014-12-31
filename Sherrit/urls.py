from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),

 	url(r'^$', 'apps.usuarios.views.login', name="login"),
 	url(r'^login-error/$', 'apps.usuarios.views.error', name="error"),
 	url(r'^new-users/$', 'apps.usuarios.views.nuevo_usuario', name="new-users"),
 	url(r'^salir/$', 'apps.usuarios.views.logOut', name="logOut"),

 	url(r'^home/$', 'apps.articulos.views.home', name="home"),
 	url(r'^add/$', 'apps.articulos.views.add', name="add"),
 	url(r'^articulo/(?P<slug>[-\w]+)/$', 'apps.articulos.views.articulo', name="articulo"),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )