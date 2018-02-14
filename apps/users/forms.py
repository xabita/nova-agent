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

	us_imageine = forms.ImageField(),


	
	class Meta:
		model = User
		fields = ('first_name','last_name', 'email', 'us_imageine', 'us_ciudad')

		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)
			self.fields['us_ciudad'].queryset = Ciudad.objects.none()




