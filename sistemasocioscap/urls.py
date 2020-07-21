from django.conf.urls import url
from django.views.generic.detail import DetailView
from django.views import generic
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^socios/$', views.SociosListView.as_view(), name=socios),
    #url(r'^socios/(?P<pk>\d+)$', views.SocioDetailView.as_view(), name='socio-detail'),

]