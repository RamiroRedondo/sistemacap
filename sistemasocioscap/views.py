# -*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import date
from datetime import datetime
from django.template import loader, Context
from .models import Socio, RegistroPagos, Cuota, Anio, Cobrador
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from .forms import SocioForm, CuotaForm, CobradorForm, AnioForm
from django.db.models import Q
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.conf import settings
from reportlab.lib.utils import ImageReader
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import cm
from reportlab.lib import colors


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

##SOCIO
class SocioList(ListView):
    model = Socio
    template_name = 'socio_listado.html'

    def get_queryset(self):
        queryset = self.request.GET.get("buscar")
        socios = Socio.objects.all()
        if queryset:
            socios = Socio.objects.filter(
                Q(nombre__icontains = queryset) |
                Q(apellido__icontains = queryset)
        ).distinct()

        return socios

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
        cuots = Cuota.objects.filter(aniocuota__icontains = queryset, socio= socio)
        cuotas = cuots.extra( select={'nrocuota': 'CAST(nrocuota AS INTEGER)'}).order_by('nrocuota')
    else:
        cuots = Cuota.objects.filter(aniocuota = current_year, socio = socio)
        cuotas = cuots.extra( select={'nrocuota': 'CAST(nrocuota AS INTEGER)'}).order_by('nrocuota')
    return render (request, 'socio_detail.html',{'socio':socio, 'cuotas':cuotas,'anios':anios,'current_year':current_year})

def socio_agregar(request):
    now = datetime.now()
    current_year = now.year
    year = Anio.objects.get(anio = current_year)
    monto = year.monto_cuota
    if request.method =='POST':
        form = SocioForm(request.POST)
        if form.is_valid():
            socio = form.save()
            #creo registro
            registro = RegistroPagos.objects.create(numeroregistro = socio.dni)
            #creo cuotas

            meses = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril':4, 'Mayo':5, 'Junio':6, 'Julio':7, 'Agosto':8, 'Septiembre':9,'Octubre':10, 'Noviembre':11, 'Diciembre':12 }
        
            for mes in meses:
                Cuota.objects.create(nrocuota=meses[mes],mes= mes,pago= "no", total= monto, aniocuota= current_year,registro = registro, socio = socio)
             
            socio.registro = registro
            socio.dar_baja = "No"
            socio.save()
           

            return redirect('socio_detail',id_socio= socio.id)
    else:
        form = SocioForm()
    return render (request, 'socio_form.html',{'form': form,})
## PANEL
def panel(request):
   
    
    return render(
    request,
    'panel.html',
     context={},
)
##COBRADOR
class CobradorList(ListView):
    model = Cobrador
    template_name = 'cobrador_listado.html'

class CobradorCreate(CreateView):
    model = Cobrador
    form_class = CobradorForm
    template_name = 'cobrador_form.html'
    success_url = reverse_lazy('listado_cobrador')

class CobradorUpdate(UpdateView):
    model = Cobrador
    form_class = CobradorForm
    template_name = 'cobrador_form.html'
    success_url = reverse_lazy('listado_cobrador')

class CobradorDelete(DeleteView):
    model = Cobrador
    template_name = 'cobrador_delete.html'
    success_url = reverse_lazy('listado_cobrador')

##AÑO
class AnioList(ListView):
    model = Anio
    template_name = 'anio_listado.html'

class AnioCreate(CreateView):
    model = Anio
    form_class = AnioForm
    template_name = 'anio_form.html'
    success_url = reverse_lazy('listado_anio')

    def form_valid(self, form):
        year = form.instance.anio
        monto= form.instance.monto_cuota
        
        socios = Socio.objects.all()

        for socio in socios:
            meses = {'Enero': 1, 'Febrero': 2, 'Marzo': 3, 'Abril':4, 'Mayo':5, 'Junio':6, 'Julio':7, 'Agosto':8, 'Septiembre':9,'Octubre':10, 'Noviembre':11, 'Diciembre':12 }
            registro = socio.registro
            for mes in meses:     
                Cuota.objects.create(nrocuota=meses[mes],mes= mes,pago= "no", total= monto, aniocuota= year,registro = registro, socio = socio)

        return super(AnioCreate, self).form_valid(form)

class AnioUpdate(UpdateView):
    model = Anio
    form_class = AnioForm
    template_name = 'anio_form.html'
    success_url = reverse_lazy('listado_anio')

class AnioDelete(DeleteView):
    model = Anio
    template_name = 'anio_delete.html'
    success_url = reverse_lazy('listado_anio')

## CUOTA
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

class ReporteSociosPDF(View):  
     
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        logo = ImageReader('https://i.pinimg.com/564x/21/b4/86/21b486d3cff802856f0db300de1723a9.jpg')
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(logo, 40, 750, 120, 90,preserveAspectRatio=True)                
         
    def get(self, request, *args, **kwargs):
        #Indicamos el tipo de contenido a devolver, en este caso un pdf
        response = HttpResponse(content_type='application/pdf')
        #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
        buffer = BytesIO()
        #Canvas nos permite hacer el reporte con coordenadas X y Y
        pdf = canvas.Canvas(buffer)
        #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
        self.cabecera(pdf)
        pdf.setFont("Helvetica", 16)
#Dibujamos una cadena en la ubicación X,Y especificada
        pdf.drawString(200, 790, u"Club Atlético Pellegrini - Listado de socios")
        pdf.setFont("Helvetica", 14)
        y = 600
        self.tabla(pdf, y)
        #Con show page hacemos un corte de página para pasar a la siguiente
        pdf.showPage()
        pdf.save()
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = ('Nro de socio', 'Nombre', 'Apellido', 'DNI', 'Dirección')
        #Creamos una lista de tuplas que van a contener a las personas
        detalles = [(socio.nrosocio, socio.nombre, socio.apellido, socio.dni, socio.direccion) for socio in Socio.objects.all()]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles, colWidths=[2 * cm, 3 * cm, 3 * cm,2 * cm ,  6 * cm])
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(3,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 10
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 60,y)
