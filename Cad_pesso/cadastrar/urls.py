from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

	url(r'^Home/', views.Home, name="Home"),
	url(r'^cadastro_pessoas/', views.cadastro_pessoas, name="cadastro_pessoas"),
	url(r'^deletar/(?P<pessoa_id>\d+)/$', views.deletar, name="deletar"),
	url(r'^update/(?P<pessoa_id>\d+)/$', views.update, name="update"),
	url(r'^exibe_grafico/', views.exibe_grafico, name="exibe_grafico"),
]