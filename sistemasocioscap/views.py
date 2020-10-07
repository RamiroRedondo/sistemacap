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
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


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

    queryset = request.GET.get("buscar")
    socios = Socio.objects.all()
    if queryset:
        socios = Socio.objects.filter(
            Q(nombre__icontains = queryset) |
            Q(apellido__icontains = queryset)
        ).distinct()

    return render(request,'socio_listado.html', context={'socios':socios},
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

class IndexListView(ListView):
    model = Socio
    template_name = 'index.html'
    paginate_by = 4

    def get_queryset(self):
        queryset = self.request.GET.get("buscarindex")
        socios = Socio.objects.all()
        if queryset:
            socios = Socio.objects.filter(
                Q(nombre__icontains = queryset) |
                Q(apellido__icontains = queryset)
        ).distinct()

        return socios

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
    now = datetime.now()
    current_year = now.year
    if request.method =='POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save()
            #creo registro
            registro = RegistroPagos.objects.create(numeroregistro = socio.dni)
            #creo cuotas
           
            c1 = Cuota.objects.create(nrocuota="1",mes= "Enero",pago= "no", total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c2 = Cuota.objects.create(nrocuota="2",mes= "Febrero",pago= "no", total= 500,aniocuota= current_year,registro = registro, socio = socio)
            c3 = Cuota.objects.create(nrocuota="3",mes= "Marzo",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c4 = Cuota.objects.create(nrocuota="4",mes= "Abril",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c5 = Cuota.objects.create(nrocuota="5",mes= "Mayo",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c6 = Cuota.objects.create(nrocuota="6",mes= "Junio",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c7 = Cuota.objects.create(nrocuota="7",mes= "Julio",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c8 = Cuota.objects.create(nrocuota="8",mes= "Agosto",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c9 = Cuota.objects.create(nrocuota="9",mes= "Septiembre",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c10 = Cuota.objects.create(nrocuota="10",mes= "Octubre",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c11= Cuota.objects.create(nrocuota="11",mes= "Noviembre",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
            c12 = Cuota.objects.create(nrocuota="12",mes= "Diciembre",pago= "no",total= 500, aniocuota= current_year,registro = registro, socio = socio)
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

def cuota_pagar(request,id_cuota, id_socio):
    cuota = Cuota.objects.get(id = id_cuota)
    fecha = datetime.now()
    cuota.pago = "si"
    cuota.fecha_pago = fecha
    cuota.save()
    return redirect('socio_detail',id_socio = id_socio)

def cuotas_deuda(request):

    cuotas = Cuota.objects.filter(pago='no')

    return render(request, 'deudas.html',{'cuotas': cuotas})

def reporte_cuota(request,id_cuota, id_socio):
    cuota = Cuota.objects.get(id = id_cuota)
    socio = Socio.objects.get(id = id_socio)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attatchment; filename= Recibo-cuota.pdf'


    buffer = BytesIO()
    c= canvas.Canvas(buffer,pagesize=A4)

    c.setLineWidth(.3)
    c.setFont('Helvetica',22)
    c.drawString(30,750, 'Club Atlético Pellegrini')
   

    c.setFont('Helvetica',12)
    c.drawString(30,730, 'Alsina 70 6346 Pellegrini, Provincia de Buenos Aires, Argentina')

    c.setFont('Helvetica',12)
    c.drawString(30,700, 'Socio: ' + socio.nombre + ' ' + socio.apellido )
    c.setFont('Helvetica',12)
    c.drawString(30,680, 'Cuota: ' + cuota.nrocuota + '- Mes: ' + cuota.mes + ' ' + cuota.aniocuota)

    c.setFont('Helvetica',12)
    c.drawString(30,660, 'Total: ' + '$' + str(cuota.total) )
    

    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response


