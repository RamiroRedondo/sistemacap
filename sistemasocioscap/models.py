# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver

class RegistroPagos (models.Model):

	numeroregistro = models.CharField (max_length = 200, null=True, blank=True)
	
	def __str__(self):
    		return "Registro de pago"
  	def get_absolute_url(self):
    		return reverse ('RegistroPagos-detail', args=[str(self.id)])

class Cobrador (models.Model):
	dni = models.IntegerField()
	nombre = models.CharField(max_length= 200)
	apellido = models.CharField (max_length = 200)

	def __str__(self):
    		return self.nombre
  	def get_absolute_url(self):
    		return reverse ('cobrador-detail', args=[str(self.id)])
	
class Socio (models.Model):
	dni = models.IntegerField ()
	nombre = models.CharField(max_length= 200)
	apellido = models.CharField (max_length = 200)
	fecha_nacimiento = models.DateField(null = True, blank=True)
	nrosocio = models.IntegerField(null = True, blank=True)
	direccion = models.CharField (max_length = 200)
	mail = models.EmailField(max_length=254, null=True)
	cbu = models.IntegerField (null=True)
	dar_baja = models.CharField(max_length=32,choices=[('si', 'Si'),('no', 'No')],null = True, blank=True)
	registro = models.OneToOneField(RegistroPagos, on_delete=models.SET_NULL, null = True, blank=True)
	cobrador = models.ForeignKey(Cobrador, on_delete=models.SET_NULL, null = True, blank=True)
	
	#anioocuota = models.ManyToManyField(Anual, help_text="Año cuota")
  	def get_absolute_url(self):
    		return reverse ('socio-detail', args=[str(self.id)])

class Cuota(models.Model):
	"""docstring for Cuota"""
	nrocuota = models.CharField (max_length = 200)
	mes = models.CharField (max_length = 200, null=True, blank=True)
	pago = models.CharField(max_length=32,choices=[('si', 'Si'),('no', 'No')], default="",null = True, blank=True)
	fecha_pago = models.DateField(null=True, blank=True)
	total = models.IntegerField (null=True)
	aniocuota = models.CharField (max_length = 200,null=True, blank=True)
	registro = models.ForeignKey('RegistroPagos', on_delete=models.SET_NULL, null=True, blank=True)
	socio = models.ForeignKey('Socio', on_delete=models.SET_NULL, null=True, blank=True)
	# ForeignKey, ya que una cuota tiene un solo registro, pero el mismo registro puede tener muchas cuotas.
	def __str__(self):
    		return self.nrocuota
  	def get_absolute_url(self):
    		return reverse ('cuota-detail', args=[str(self.id)])



class Anio(models.Model):
	anio = models.CharField(max_length = 200)
	monto_cuota = models.IntegerField (null=True)

"""
@receiver(post_save, sender = Socio)
def socio_post_save(sender, instance, created, **kwargs):

    if created:
    	RegistroPagos.objects.create(numeroregistro = instance.dni, socio= instance)
		
    else:
    	instance.save()
       # se guarda el socio pero no se creó, no hago nada

    pass


@receiver(post_save, sender = RegistroPagos)
def registropago_post_save(sender, instance, created, **kwargs):
    if created:
    	c1 =Cuota.objects.create(nrocuota="1",mes= "Enero",pago='no', anioocuota= "2020",registro = instance)
		c2 =Cuota.objects.create(nrocuota="2",mes= "Febrero",pago='no', anioocuota= "2020",registro = instance)

    else:
    	instance.save()
       # se guarda el socio pero no se creó, no hago nada
    pass
"""