from __future__ import unicode_literals
from django.db import models


from helpers.helper_images import make_upload_path
from defaults.strings import *



from ciudades.models import Ciudad
from django.conf import settings




class UserType(models.Model):
	usertype_name= models.CharField(max_length=50)
	usertype_desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
#	slug = AutoSlugField( populate_from='name', max_length=100, always_update=True, unique=True)
	

	def __str__(self):
		return self.usertype_name

	def __unicode__(self):
		return self.usertype_name
		
   
class User(models.Model):
	first_name = models.CharField(max_length=60 ,blank=True, null=False)
	last_name = models.CharField(max_length=60 ,blank=True, null=False)
	us_imageine = models.ImageField(upload_to='make_upload_path',
									default=DEFAULT_PICTURE_FOR_USER)
	us_birthday = models.DateField()
	us_ciudad = models.ForeignKey('ciudades.Ciudad', on_delete=models.CASCADE, blank=False, null=False)
	us_isactive = models.BooleanField(default=True)
	username = models.CharField(max_length=15 ,blank=True, null=False, unique=True)
	password = models.CharField(max_length=150,blank=True, null=False)
	email = models.EmailField(default='mail@co.co', blank=False, unique=True)
	last_login = models.DateTimeField(auto_now=True)
	is_staff = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
