# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .forms import RegModelForm
from .models import clients

class AdminRegistrado(admin.ModelAdmin):
	list_display = ["usuario","nombreapp","descripcion"]
	form = RegModelForm

admin.site.register(clients,AdminRegistrado)