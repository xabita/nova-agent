from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import User
from ciudades.models import  Ciudad

# -----------------------------------------------------------------------------
# CONTENT FORMS
# -----------------------------------------------------------------------------
class UserForm(forms.ModelForm):
	first_name = 	forms.CharField(
					widget=forms.TextInput(attrs={'class': 'form-control'}),
					label="Nombre",
				)
	last_name = 	forms.CharField(
					widget=forms.TextInput(attrs={'class': 'form-control'}),
					label="Apellidos",
				)
	email = 	forms.CharField(
					widget=forms.TextInput(attrs={'class': 'form-control'}),
					label="Correo electrónico",
				)

	username = 	forms.CharField(
					widget=forms.TextInput(attrs={'class': 'form-control'}),
					label="Usuario",
				)
	password = 	forms.CharField(
					widget=forms.PasswordInput(attrs={'class': 'form-control'}),
					label="Contraseña",
				)
	us_isactive = forms.BooleanField(
					widget= forms.CheckboxInput(attrs={'class':'filled-in', 'id':'filled-in-box'}),
					label="Activo",
				)
	#us_ciudad = forms.SelectField




	us_imageine = forms.ImageField(),

	us_birthday = forms.DateField(widget=forms.DateInput()),

	


	class Meta:
		model = User
		fields = ('first_name','last_name', 'email', 'us_imageine', 'us_birthday', 'us_isactive', 'username','password')

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['us_ciudad'].queryset = Ciudad.objects.none()
