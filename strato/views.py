from django.shortcuts import render
from .forms import RegForm
from django.views import generic
from .models import clients
import os
import time
from strato.tables import ClientTable 

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


def despliegue(request):
	despliegue=ClientTable()
	context = {
		"despliegue":despliegue
	}
	if 'name' in request.POST:
	    name = request.POST['name']
	    ip = clients.objects.filter(nombreapp=name)[0].ip
	    #print ip
	    os.system("fab -H "+ip+" -p \"122333\" -P despliegue1 -f \"fabfile.py\"")
	    time.sleep(0.1)
	    os.system("fab -H "+ip+" -p \"122333\" -P despliegue2 -f \"fabfile.py\"")
	    time.sleep(0.1)
	    os.system("fab -H "+ip+" -p \"122333\" -P despliegue3 -f \"fabfile.py\"")
	else:
	    name = False
	return render(request,"despliegue.html",context)


def pruebas(request):
	titulo="PRUEBAS"
	context = {
	    "temp_titulo":titulo,
	}
	return render(request,"pruebas.html",context)



	
