from django import forms
from .models import Socio,Cuota
from django.contrib.admin import widgets
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'
    
class SocioForm(forms.ModelForm):
	class Meta:
		model = Socio

		fields = [
			'nombre',
			'apellido',
			'dni',
			'fecha_nacimiento',
			'nrosocio',
			'direccion',
			'mail',
			'cbu',
			
		
		]
		labels = {
			'nombre': 'Nombre',
			'apellido': 'Apellido',
			'dni': 'Documento',
			'fecha_nacimiento': 'Fecha de nacimiento',
			'nrosocio': 'Numero de socio',
			'direccion':'Direccion',
			'mail': 'E-Mail',
			'cbu':'CBU',
		
		
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'dni': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento': forms.DateInput(attrs={'type':'date'}),
			'nrosocio': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'mail': forms.TextInput(attrs={'class':'form-control'}),
			'cbu': forms.TextInput(attrs={'class':'form-control'}),
		
	
		}

class CuotaForm(forms.ModelForm):
	class Meta:
		model = Cuota

		fields = [
			'nrocuota',
			'mes',
			'pago',
			'fecha_pago',
			'total',
			'aniocuota',
			
		]
		labels = {
			'nrocuota': 'Cuota numero:',
			'mes': 'Mes',
			'pago': 'Paga',
			'fecha_pago': 'Fecha de pago',
			'total':'Total ($)',
			'anio_cuota':'Year'

		}
		widgets = {
			'nrocuota': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'mes': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'pago': forms.Select(attrs={'class':'form-control'}),
			'fecha_pago': forms.DateInput(),
			'nrosocio': forms.TextInput(attrs={'class':'form-control'}),
			'total': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
			'aniocuota': forms.TextInput(attrs={'class':'form-control','readonly':'readonly'}),
		
	
		}
