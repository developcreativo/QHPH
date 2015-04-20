from .models import Evento
from ciudades.models import Ciudad
from lugares.models import Lugar

from rest_framework import serializers

class EventoSerializer(serializers.HyperLinkedModelSerializer):

	class Meta:
		model = Evento
		fields = ('nombre', 'fecha', 'hora', 'descripcion', 'lugar')

class CiudadSerializer(serializers.HyperLinkedModelSerializer):

	class Meta:
		model = Ciudad
		fields = ('ciudad')

class LugarSerializer(serializers.HyperLinkedModelSerializer):

	class Meta:
		model = Lugar
		fields = ('lugar', 'ciudad')