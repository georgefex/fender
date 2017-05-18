from django.shortcuts import render
from .forms import RegForm

from .models import clients
import os
import time

# Create your views here.
def inicio(request):
	titulo="AMBIENTES DE PRODUCCION"
	form= RegForm(request.POST or None)
	if form.is_valid():
		form_data =form.cleaned_data
		abc= form_data.get("usuario")
		abc2= form_data.get("nombreapp")
		abc3= form_data.get("descripcion")
		abc4= form_data.get("ip")
		abc5= form_data.get("puerto")
		obj= clients.objects.create(usuario=abc, nombreapp=abc2,descripcion=abc3,puerto=abc5,ip=abc4)
		os.system("fab -H 192.168.0.37 -p \"122333\" -P crear_contenedor:\""+abc2+"\",\""+abc5+"\" -f \"fabfile.py\"")
		time.sleep(0.1)
                os.system("fab -H 192.168.0.37 -p \"122333\" -P correr_contenedor:\""+abc2+"\" -f \"fabfile.py\"")
	context = {
	    "temp_titulo":titulo,
		"el_form":form,
	}
	return render(request,"inicio.html",context)
