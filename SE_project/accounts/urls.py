from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
	path('',views.home,name='website-home'),
	url(r'^$', views.index, name='index'),
	url('home', views.index),
	url(r'^create$', views.create, name='create'),
	url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
	url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
	url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
	url('postJobs', views.jobForm, name='showJobForm'),

	url('postInternship', views.internForm, name='showInternshipForm'),
	url('createInternship', views.createInternship),

]
