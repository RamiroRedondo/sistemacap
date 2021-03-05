from django.conf.urls import url
from django.views.generic.detail import DetailView
from . import views
from sistemasocioscap.views import SocioList, SocioCreate, SocioUpdate, SocioDelete, IndexListView, ReporteSociosPDF, CobradorCreate, CobradorList, CobradorUpdate, CobradorDelete, AnioCreate, AnioUpdate, AnioList, AnioDelete,SociosBajaList
from django.contrib.auth.decorators import login_required


urlpatterns = [
	
	url(r'^$', login_required(IndexListView.as_view()), name='index'),
	url(r'^panel$', login_required(views.panel), name='panel'),
	url(r'^nuevo$', login_required(SocioCreate.as_view()), name='socio_crear'),
	url(r'^listado$', login_required(SocioList.as_view()), name='listado_socios'),
	url(r'^listadobajas$', login_required(SociosBajaList.as_view()), name='listado_sociosbaja'),
	url(r'^deudas$', login_required(views.cuotas_deuda), name='cuotas_deuda'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(SocioUpdate.as_view()), name='socio_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(SocioDelete.as_view()), name='socio_eliminar'),
	url(r'^socio_detail/(?P<id_socio>\d+)/$', login_required(views.socio_detail), name='socio_detail'),
	url(r'^socio_agregar$', login_required(views.socio_agregar), name='socio_agregar'),
	url(r'^cuota_view/(?P<id_cuota>\d+)/(?P<id_socio>(\d+))/$', login_required(views.cuota_view), name='cuota_view'),
	url(r'^cuota_pagar/(?P<id_cuota>\d+)/(?P<id_socio>(\d+))/$', login_required(views.cuota_pagar), name='cuota_pagar'),
	url(r'^cuota_anular/(?P<id_cuota>\d+)/(?P<id_socio>(\d+))/$', login_required(views.cuota_anular), name='cuota_anular'),
	url(r'^socio_baja/(?P<id_socio>\d+)/$', login_required(views.socio_baja), name='socio_baja'),
	url(r'^socio_darbaja/(?P<id_socio>\d+)/$', login_required(views.socio_darbaja), name='socio_darbaja'),
	url(r'^socio_alta/(?P<id_socio>\d+)/$', login_required(views.socio_alta), name='socio_alta'),
	url(r'^socio_daralta/(?P<id_socio>\d+)/$', login_required(views.socio_daralta), name='socio_daralta'),
	#PDF
	url(r'^reporte_cuota/(?P<id_cuota>\d+)/(?P<id_socio>(\d+))/$', login_required(views.reporte_cuota), name='reporte_cuota'),
	url(r'^reporte_socios_pdf/$',login_required(ReporteSociosPDF.as_view()), name="reporte_socios_pdf"),
	url(r'^reporte_cobrador_pdf/(?P<id_cobrador>\d+)/$',login_required(views.cobrador_generate_pdf), name="reporte_cobrador_pdf"),
	#cobrador
	url(r'^nuevocobrador$', login_required(CobradorCreate.as_view()), name='cobrador_crear'),
	url(r'^listadocobradores$', login_required(CobradorList.as_view()), name='listado_cobrador'),
	url(r'^eliminarcobrador/(?P<pk>\d+)/$', login_required(CobradorDelete.as_view()), name='cobrador_eliminar'),
	url(r'^editarcobrador/(?P<pk>\d+)/$', login_required(CobradorUpdate.as_view()), name='cobrador_editar'),
	url(r'^socioscobrador/(?P<id_cobrador>\d+)$', login_required(views.cobradorSociosList), name='cobrador_listadosocios'),
	#anio
	url(r'^nuevoanio$', login_required(AnioCreate.as_view()), name='anio_crear'),
	url(r'^listadoanio$', login_required(AnioList.as_view()), name='listado_anio'),
	url(r'^eliminaranio/(?P<pk>\d+)/$', login_required(AnioDelete.as_view()), name='anio_eliminar'),
	url(r'^editaranio/(?P<pk>\d+)/$', login_required(AnioUpdate.as_view()), name='anio_editar'),
	


	#url(r'^listado$', views.socios_listado, name='listado_socios'),
	  
]