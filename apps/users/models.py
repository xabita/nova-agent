from __future__ import unicode_literals
from django.db import models

#from django.nuts.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from helpers.helper_images import make_upload_path
from defaults.strings import *

from .managers import UserManager


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
		return self.name
		
   
class User(AbstractBaseUser, PermissionsMixin):
	us_firstname = models.CharField(max_length=60 ,blank=True, null=False)
	us_lastname = models.CharField(max_length=60 ,blank=True, null=False)
	us_imageine = models.ImageField(upload_to='make_upload_path',
									default=DEFAULT_PICTURE_FOR_USER)
	us_email = models.EmailField(default='mail@co.co', blank=False, unique=True)
	us_birthday = models.DateTimeField()
	us_ciudad = models.ForeignKey('Ciudad', on_delete=models.CASCADE, blank=False, null=False)
	us_isactive = models.BooleanField(default=True)

	us_username = models.CharField(max_length=15 ,blank=True, null=False, unique=True)
	us_password = models.CharField(max_length=150,blank=True, null=False)
	us_last_login = models.DateTimeField(auto_now=True)
	is_staff = models.BooleanField(default=True)
	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')
	def get_full_name(self):
		'''Returns the first_name plus the last_name, with a space in between.'''
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()
	def get_short_name(self):
		'''Returns the short name for the user.'''
		return self.first_name

	def email_user(self, subject, message, from_email=None, **kwargs):
		'''Sends an email to this User.'''
		send_mail(subject, message, from_email, [self.email], **kwargs)


	def __str__(self):
		return '%s %s' % (self.first_name, self.last_name)


	def __unicode__(self):
		return self.first_name


