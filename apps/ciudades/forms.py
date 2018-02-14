from django import forms

class Ciudad(forms.Form):
    ciudad_name = forms.CharField(max_length=100)