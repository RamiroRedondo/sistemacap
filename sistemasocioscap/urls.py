from django.conf.urls import url
from django.views.generic.detail import DetailView
from . import views
from sistemasocioscap.views import SocioList, SocioCreate, SocioUpdate, SocioDelete

urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^nuevo$', SocioCreate.as_view(), name='socio_crear'),
	url(r'^listado$', SocioList.as_view(), name='listado_socios'),
	url(r'^editar/(?P<pk>\d+)/$', SocioUpdate.as_view(), name='socio_editar'),
	url(r'^eliminar/(?P<pk>\d+)/$', SocioDelete.as_view(), name='socio_eliminar'),

	
	#url(r'^listado$', views.socios_listado, name='listado_socios'),
	  
]