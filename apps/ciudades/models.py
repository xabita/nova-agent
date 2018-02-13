from django.db import models


class Estado(models.Model):
	estado_name= models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.estado_name

	def __unicode__(self):
		return self.estado_name

class Ciudad(models.Model):
	ciudad_name= models.CharField(max_length=100)
	ciudad_estado = models.ForeignKey('Estado', on_delete=models.CASCADE, blank=False, null=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.ciudad_name

	def __unicode__(self):
		return self.ciudad_name
