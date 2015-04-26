from .models import Evento
from ciudades.models import Ciudad
from lugares.models import Lugar

from rest_framework import serializers

class EventoSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Evento
		fields = ('id', 'nombre', 'fecha', 'hora', 'descripcion', 'lugar')

class CiudadSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Ciudad
		fields = ('id', 'ciudad')

class LugarSerializer(serializers.HyperlinkedModelSerializer):

	class Meta:
		model = Lugar
		fields = ('id', 'nombre', 'ciudad')