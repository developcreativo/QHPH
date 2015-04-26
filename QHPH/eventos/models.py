from django.db import models
from lugares.models import Lugar


class Evento(models.Model):

	nombre = models.CharField(max_length=200)
	fecha = models.DateField(blank=True)
	hora = models.DateTimeField(blank=True)
	descripcion = models.TextField(blank=True)

	lugar = models.ForeignKey(Lugar)

	def __unicode__(self):
		return '%s - %s' % (self.nombre, self.fecha)