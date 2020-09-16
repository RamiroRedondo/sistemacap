# -*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import date
from datetime import datetime
from django.template import loader, Context
from .models import Socio, RegistroPagos, Cuota, Anio
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import SocioForm, CuotaForm
from django.db.models import Q

def index(request):
   
    queryset = request.GET.get("buscar")
    
    socios = Socio.objects.all()
    if queryset:
        socios = Socio.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(apellido__icontains = queryset)
        ).distinct()


    return render(
    request,
    'index.html',
     context={'socios':socios},
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

def socio_detail(request, id_socio):
    now = datetime.now()
    current_year = now.year
    socio = Socio.objects.get(id= id_socio)
    cuotas = Cuota.objects.filter(registro = socio.registro,aniocuota = current_year)
    anios = Anio.objects.all()
    queryset = request.GET.get("select_year")
    if queryset:
        cuotas = Cuota.objects.filter(
            Q(aniocuota__icontains = queryset),registro = socio.registro
        )
    return render (request, 'socio_detail.html',{'socio':socio, 'cuotas':cuotas,'anios':anios,'current_year':current_year})

def socio_agregar(request):
    if request.method =='POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save()
            #creo registro
            registro = RegistroPagos.objects.create(numeroregistro = socio.dni)
            #creo cuotas
            c1 = Cuota.objects.create(nrocuota="1",mes= "Enero",pago= "no", aniocuota= "2020",registro = registro)
            c2 = Cuota.objects.create(nrocuota="2",mes= "Febrero",pago= "no", aniocuota= "2020",registro = registro)
            c3 = Cuota.objects.create(nrocuota="3",mes= "Marzo",pago= "no", aniocuota= "2020",registro = registro)
            c4 = Cuota.objects.create(nrocuota="4",mes= "Abril",pago= "no", aniocuota= "2020",registro = registro)
            c5 = Cuota.objects.create(nrocuota="5",mes= "Mayo",pago= "no", aniocuota= "2020",registro = registro)
            c6 = Cuota.objects.create(nrocuota="6",mes= "Junio",pago= "no", aniocuota= "2020",registro = registro)
            c7 = Cuota.objects.create(nrocuota="7",mes= "Julio",pago= "no", aniocuota= "2020",registro = registro)
            c8 = Cuota.objects.create(nrocuota="8",mes= "Agosto",pago= "no", aniocuota= "2020",registro = registro)
            c9 = Cuota.objects.create(nrocuota="9",mes= "Septiembre",pago= "no", aniocuota= "2020",registro = registro)
            c10 = Cuota.objects.create(nrocuota="10",mes= "Octubre",pago= "no", aniocuota= "2020",registro = registro)
            c11= Cuota.objects.create(nrocuota="11",mes= "Noviembre",pago= "no", aniocuota= "2020",registro = registro)
            c12 = Cuota.objects.create(nrocuota="12",mes= "Diciembre",pago= "no", aniocuota= "2020",registro = registro)
            socio.registro = registro
            socio.save()

            return redirect('socio_detail',id_socio= socio.id)
    else:
        form = SocioForm()
    return render (request, 'socio_form.html',{'form': form,})


def cuota_view(request,id_cuota, id_socio):
    cuota = Cuota.objects.get(id = id_cuota)
    socio = Socio.objects.get(id = id_socio)
    if request.method == 'GET':
        form = CuotaForm(instance = cuota)
    else:
        form = CuotaForm(request.POST,instance = cuota)
        if form.is_valid():
            form.save()
        return redirect('socio_detail',id_socio = id_socio)

    return render(request, 'cuota_form.html',{'form': form})

