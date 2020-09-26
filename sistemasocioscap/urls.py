from django.conf.urls import url
from django.views.generic.detail import DetailView
from . import views
from sistemasocioscap.views import SocioList, SocioCreate, SocioUpdate, SocioDelete
from django.contrib.auth.decorators import login_required


urlpatterns = [
	
	url(r'^$', login_required(views.index), name='index'),
	url(r'^nuevo$', login_required(SocioCreate.as_view()), name='socio_crear'),
	url(r'^listado$', login_required(views.socios_listado), name='listado_socios'),
	url(r'^editar/(?P<pk>\d+)/$', login_required(SocioUpdate.as_view()), name='socio_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', login_required(SocioDelete.as_view()), name='socio_eliminar'),
	url(r'^socio_detail/(?P<id_socio>\d+)/$', login_required(views.socio_detail), name='socio_detail'),
	url(r'^socio_agregar$', login_required(views.socio_agregar), name='socio_agregar'),
	url(r'^cuota_view/(?P<id_cuota>\d+)/(?P<id_socio>(\d+))/$', login_required(views.cuota_view), name='cuota_view'),



	#url(r'^listado$', views.socios_listado, name='listado_socios'),
	  
]