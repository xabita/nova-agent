from django import forms
from .models import User

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
	us_imageine = forms.ImageField()

	class Meta:
		model = User
		fields = ('first_name','last_name', 'email', 'us_imageine',  'us_birthday','us_ciudad', 'us_isactive', 'username','password')

		