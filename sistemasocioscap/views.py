# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader, Context
from .models import Socio, RegistroPagos
from django.shortcuts import render, redirect
from django.views import generic
from .forms import SocioForm

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
def socios_listado(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    socios = Socio.objects.all()
    tot_socios= Socio.objects.all().count()
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
    request,
    'socio_listado.html',
     context={'tot_socios':tot_socios, 'socios':socios},
)    

def socio_view(request):
    if request.method == 'POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form= SocioForm()

    return render(request, 'socio_form.html',{'form': form})

def socio_list(request):
    socios = Socio.objects.all()
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
    request,
    'socios_list.html',
    context={'socios':socios},
)
def socio_edit(request, id_socio):
    socio = Socio.objects.get(id= id_socio)
    if request.method == 'GET':
        form = SocioForm(instance = socio)
    else:
        form = SocioForm(request.POST,instance = socio)
        if form.is_valid():
            form.save()
        return redirect('listado_socios')
    return render (request, 'socio_form.html',{'form': form})

class SocioListView(generic.ListView):
    model = Socio
    paginate_by = 5
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