from .models import Evento
from ciudades.models import Ciudad
from lugares.models import Lugar

from rest_framework import viewsets

from .serializers import EventoSerializer, CiudadSerializer, LugarSerializer


class EventoViewSet(viewsets.ModelViewSet):

	queryset = Evento.objects.all()
	serializer_class = EventoSerializer

class CiudadViewSet(viewsets.ModelViewSet):

	queryset = Ciudad.objects.all()
	serializer_class = CiudadSerializer

class LugarViewSet(viewsets.ModelViewSet):

	queryset = Lugar.objects.all()
	serializer_class = LugarSerializer