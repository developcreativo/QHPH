from django.db import models
from ciudades.models import Ciudad #Aqui importo el modelo ciudad

class Lugar(models.Model):

	nombre = models.CharField(max_length=255)

	ciudad = models.ForeignKey(Ciudad)

	def __unicode__(self):
		return self.nombre