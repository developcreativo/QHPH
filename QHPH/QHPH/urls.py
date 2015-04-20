from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework import routers
from QHPH.eventos import viewsets

router = routers.DefaultRouter()
router.register(r'eventos', viewsets.EventoViewSet)
router.register(r'ciudades', viewsets.CiudadViewSet)
router.register(r'lugares', viewsets.LugarViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'QHPH.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
