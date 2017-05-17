# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class clients(models.Model):
	usuario = models.CharField(max_length=100, blank=True, null=True)
	nombreapp = models.CharField(max_length=100, blank=True, null=True)
	descripcion =  models.CharField(max_length=500, blank=True, null=True)

	def __unicode__(self):
		return self.usuario

	def __str__(self):
		return self.usuario


	