# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader, Context
from .models import Socio, RegistroPagos
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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

def socio_delete(request, id_socio):
    socio = Socio.objects.get(id= id_socio)
    if request.method == 'POST':
        socio.delete()
        return redirect('listado_socios')
    return render (request, 'socio_delete.html',{'socio': socio})


class SocioList(ListView):
    model = Socio
    template_name = 'socio_listado.html'

class SocioCreate(CreateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socio_form.html'
    success_url = reverse_lazy('listado_socios')

class SocioUpdate(UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = 'socio_form.html'
    success_url = reverse_lazy('listado_socios')

class SocioDelete(DeleteView):
    model = Socio
    template_name = 'socio_delete.html'
    success_url = reverse_lazy('listado_socios')
