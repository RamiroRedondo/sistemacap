# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#from .models import Poll
#from .models import Choice
from .models import Socio
from .models import Cuota
from .models import RegistroPagos
from .models import Anio
from .models import Cobrador
#admin.site.register(Poll)
#admin.site.register(Choice)
#admin.site.register(Socio)

class SocioAdmin(admin.ModelAdmin):
	list_filter = ('apellido','nombre')
	list_display = ['apellido','nombre','nrosocio','dni','direccion']
	fields = ['nombre','apellido','nrosocio','dni','direccion', 'fecha_nacimiento', 'mail', 'cbu','dar_baja','registro']

admin.site.register(Socio, SocioAdmin)
admin.site.register(Cuota)
admin.site.register(RegistroPagos)
admin.site.register(Anio)
admin.site.register(Cobrador)
"""admin.site.register(Socio, SocioAdmin)
admin.site.register(Anual)
admin.site.register(Cuota)
admin.site.register(RegistroPagos)
"""
# Register your models here.