from django import forms
from .models import Socio

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
			'dar_baja',
		
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
			'dar_baja': 'Dar de baja',
		
		}
		widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'apellido': forms.TextInput(attrs={'class':'form-control'}),
			'dni': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
			'nrosocio': forms.TextInput(attrs={'class':'form-control'}),
			'direccion': forms.TextInput(attrs={'class':'form-control'}),
			'mail': forms.TextInput(attrs={'class':'form-control'}),
			'cbu': forms.TextInput(attrs={'class':'form-control'}),
			'dar_baja': forms.TextInput(attrs={'class':'form-control'}),
	

		}