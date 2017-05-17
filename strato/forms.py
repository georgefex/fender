from django import forms

from .models import clients

class RegModelForm(forms.ModelForm):
	class Meta:
		model = clients
		fields = ["usuario","nombreapp","descripcion","puerto","ip"]

class RegForm(forms.Form):
	usuario = forms.CharField(max_length=100)
	nombreapp = forms.CharField(max_length=100)
	descripcion = forms.CharField(max_length=500)
	puerto = forms.CharField(max_length=100)
	ip = forms.CharField(max_length=100)