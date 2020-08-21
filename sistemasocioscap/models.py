# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver



class Socio (models.Model):

	dni = models.IntegerField ()
	nombre = models.CharField(max_length= 200, help_text="Ingrese el nombre del usuario")
	apellido = models.CharField (max_length = 200)
	fecha_nacimiento = models.DateField(help_text="Ingrese el fecha de nacimiento en formato MES/DIA/AÑO")
	nrosocio = models.IntegerField ()
	direccion = models.CharField (max_length = 200)
	mail = models.EmailField(max_length=254, null=True)
	cbu = models.IntegerField (null=True)
	dar_baja = models.CharField(max_length=32,choices=[('si', 'Si'),('no', 'No')], default="",null = True, blank=True)
	#anioocuota = models.ManyToManyField(Anual, help_text="Año cuota")
  	def get_absolute_url(self):
    		return reverse ('socio-detail', args=[str(self.id)])

class RegistroPagos (models.Model):

	numeroregisro = models.CharField (max_length = 200, null=True, blank=True)
	socio = models.OneToOneField(Socio, on_delete=models.SET_NULL, null = True, blank=True)
	def __str__(self):
    		return "Registro de pago"
  	def get_absolute_url(self):
    		return reverse ('RegistroPagos-detail', args=[str(self.id)])

class Cuota(models.Model):
	"""docstring for Cuota"""
	nrocuota = models.CharField (max_length = 200)
	mes = models.CharField (max_length = 200, null=True, blank=True)
	fecha_pago = models.DateField(null=True, blank=True)
	anioocuota = models.CharField (max_length = 200, null=True, blank=True)
	registro = models.ForeignKey('RegistroPagos', on_delete=models.SET_NULL, null=True, blank=True)
	# ForeignKey, ya que una cuota tiene un solo registro, pero el mismo registro puede tener muchas cuotas.
	def __str__(self):
    		return self.nrocuota
  	def get_absolute_url(self):
    		return reverse ('cuota-detail', args=[str(self.id)])

@receiver(post_save, sender = Socio)
def socio_post_save(sender, instance, created, **kwargs):
    if created:
    	RegistroPagos.objects.create(socio= instance)
    else:
    	instance.save()
       # se guarda el socio pero no se creó, no hago nada
    pass

@receiver(post_save, sender = RegistroPagos)
def registropago_post_save(sender, instance, created, **kwargs):
    if created:
    	Cuota.objects.create(nrocuota="1",mes= "Enero",fecha_pago='0001-01-01', anioocuota= "2020",registro = instance)
    else:
    	instance.save()
       # se guarda el socio pero no se creó, no hago nada
    pass