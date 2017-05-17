from django.shortcuts import render
from .forms import RegForm

from .models import clients

# Create your views here.
def inicio(request):
	titulo="AMBIENTES DE PRODUCCION"
	form= RegForm(request.POST or None)
	if form.is_valid():
		form_data =form.cleaned_data
		abc= form_data.get("usuario")
		abc2= form_data.get("nombreapp")
		abc3= form_data.get("descripcion")
		obj= clients.objects.create(usuario=abc, nombreapp=abc2,descripcion=abc3)
	context = {
	    "temp_titulo":titulo,
		"el_form":form,
	}
	return render(request,"inicio.html",context)