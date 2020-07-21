# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader, Context
from .models import Socio, RegistroPagos
from django.shortcuts import render
from django.views import generic



def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    socios = Socio.objects.all()
    tot_socios= Socio.objects.all().count()
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
    request,
    'index.html',
     context={'tot_socios':tot_socios, 'socios':socios},
)

class SocioListView(generic.ListView):
    model = Socio
    def get_queryset(self):
        return Socio.objects.all()
"""
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def archive(request):
	socios = Socio.objects.all()
	mi_template = loader.get_template("archivo.html")
	mi_contexto = Context({'socios:':socios})
	return HttpResponse(mi_template.render(mi_contexto))
"""