from django.conf.urls import patterns, include, url
from django.contrib import admin

from eventos.views import crearLugar

from eventos.viewsets import EventoViewSet, CiudadViewSet, LugarViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'ciudades', CiudadViewSet)
router.register(r'lugares', LugarViewSet)


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'eventos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^crearEvento/', 'eventos.views.crearEvento', name="crearEvento"),
    url(r'^crearEvento2/', crearLugar.as_view()),#CBV

)