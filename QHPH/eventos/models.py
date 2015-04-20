from django.db import models
from lugares.models import Lugar


class Evento(models.Model):

	nombre = models.CharField(max_length=200)
	fecha = models.DateField()
	hora = models.DateTimeField()
	descripcion = models.TextField()

	lugar = models.ForeignKey(Lugar)

	def __unicode__(self):
		return '%s - %s' % (self.nombre, self.fecha)