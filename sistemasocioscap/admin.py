# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#from .models import Poll
#from .models import Choice
from .models import Socio
from .models import Anual
from .models import Cuota
from .models import RegistroPagos

#admin.site.register(Poll)
#admin.site.register(Choice)
#admin.site.register(Socio)

class SocioAdmin(admin.ModelAdmin):
	list_filter = ('apellido','nombre')
	list_display = ['apellido','nombre','nrosocio','dni','direccion']
	fields = ['nombre','apellido','nrosocio','dni','direccion', 'fecha_nacimiento', 'mail', 'cbu', 'registropago']
admin.site.register(Socio, SocioAdmin)
admin.site.register(Anual)
admin.site.register(Cuota)
admin.site.register(RegistroPagos)
"""admin.site.register(Socio, SocioAdmin)
admin.site.register(Anual)
admin.site.register(Cuota)
admin.site.register(RegistroPagos)
"""
# Register your models here.