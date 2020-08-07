from django.conf.urls import url
from django.views.generic.detail import DetailView
from django.views import generic
from . import views

urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^nuevo$', views.socio_view, name='socio_crear'),
	url(r'^listado$', views.socios_listado, name='listado_socios'),
	url(r'^editar/(?P<id_socio>\d+)/$', views.socio_edit, name='socio_editar'),

    #url(r'^$', views.index, name='index'),
    #url(r'^nuevo$', views.socio_view, name='socio_crear'),
    #url(r'^socios/$', views.SociosListView.as_view(), name=socios),
    #url(r'^socios/(?P<pk>\d+)$', views.SocioDetailView.as_view(), name='socio-detail'),
]