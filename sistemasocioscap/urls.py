from django.conf.urls import url
from django.views.generic.detail import DetailView
from . import views
from sistemasocioscap.views import SocioList, SocioCreate, SocioUpdate, SocioDelete, IndexListView, ReporteSociosPDF, CobradorCreate, CobradorList, CobradorUpdate, CobradorDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
	
	url(r'^$', login_required(IndexListView.as_view()), name='index'),
	url(r'^panel$', login_required(views.panel), name='panel'),
	url(r'^nuevo$', login_required(SocioCreate.as_view()), name='socio_crear'),
	url(r'^listado$', login_required(SocioList.as_view()), name='listado_socios'),
	url(r'^deudas$', login_required(views.cuotas_deuda), name='cuotas_deuda'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(SocioUpdate.as_view()), name='socio_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(SocioDelete.as_view()), name='socio_eliminar'),
	url(r'^socio_detail/(?P<id_socio>\d+)/$', login_required(views.socio_detail), name='socio_detail'),
	url(r'^socio_agregar$', login_required(views.socio_agregar), name='socio_agregar'),
	url(r'^cuota_view/(?P<id_cuota>\d+)/(?P<id_socio>(\d+))/$', login_required(views.cuota_view), name='cuota_view'),
	url(r'^cuota_pagar/(?P<id_cuota>\d+)/(?P<id_socio>(\d+))/$', login_required(views.cuota_pagar), name='cuota_pagar'),
	url(r'^reporte_cuota/(?P<id_cuota>\d+)/(?P<id_socio>(\d+))/$', login_required(views.reporte_cuota), name='reporte_cuota'),
	url(r'^reporte_socios_pdf/$',login_required(ReporteSociosPDF.as_view()), name="reporte_socios_pdf"),
	url(r'^nuevocobrador$', login_required(CobradorCreate.as_view()), name='cobrador_crear'),
	url(r'^listadocobradores$', login_required(CobradorList.as_view()), name='listado_cobrador'),
	url(r'^eliminarcobrador/(?P<pk>\d+)/$', login_required(CobradorDelete.as_view()), name='cobrador_eliminar'),
	url(r'^editarcobrador/(?P<pk>\d+)/$', login_required(CobradorUpdate.as_view()), name='cobrador_editar'),


	#url(r'^listado$', views.socios_listado, name='listado_socios'),
	  
]