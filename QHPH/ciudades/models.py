from django.db import models

class Ciudad(models.Model):
	ciudad = models.CharField(max_length=250)

	def __unicode__(self):
		return self.ciudad