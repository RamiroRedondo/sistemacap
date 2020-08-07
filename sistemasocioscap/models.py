# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.urls import reverse


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class RegistroPagos (models.Model):

	numeroregisro = models.CharField (max_length = 200)
	def __str__(self):
    		return self.numeroregisro
  	def get_absolute_url(self):
    		return reverse ('RegistroPagos-detail', args=[str(self.id)])

class Socio (models.Model):

	dni = models.IntegerField ()
	nombre = models.CharField(max_length= 200, help_text="Ingrese el nombre del usuario")
	apellido = models.CharField (max_length = 200)
	fecha_nacimiento = models.DateField(help_text="Ingrese el fecha de nacimiento en formato AAAA-MM-DD, por ejemplo: 1990-06-15")
	nrosocio = models.IntegerField ()
	direccion = models.CharField (max_length = 200)
	mail = models.EmailField(max_length=254, null=True)
	cbu = models.IntegerField (null=True)
	dar_baja = models.CharField(max_length=32,choices=[('si', 'Si'),('no', 'No')], default="",null = True, blank=True)
	registropago = models.OneToOneField(RegistroPagos, null = True, blank=True)
	#anioocuota = models.ManyToManyField(Anual, help_text="Año cuota")
  	def get_absolute_url(self):
    		return reverse ('socio-detail', args=[str(self.id)])


class Anual (models.Model):

	anio = models.CharField (max_length = 200)
	registro_anio = models.ForeignKey('RegistroPagos', on_delete=models.SET_NULL, null=True, blank=True)
	def __str__(self):
    		return self.anio
  	def get_absolute_url(self):
    		return reverse ('anio-detail', args=[str(self.id)])

class Cuota(models.Model):
	"""docstring for Cuota"""
	nrocuota = models.CharField (max_length = 200)
	mes = models.CharField (max_length = 200, null=True, blank=True)
	fecha_pago = models.DateField(null=True, blank=True)
	anioocuota = models.ForeignKey('Anual', on_delete=models.SET_NULL, null=True, blank=True)
    # ForeignKey, ya que una cuota tiene un solo año, pero el mismo año puede tener muchas cuotas.
    # 
	def __str__(self):
    		return self.nrocuota
  	def get_absolute_url(self):
    		return reverse ('cuota-detail', args=[str(self.id)])
