from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

app_name = "accounts"
urlpatterns = [
	path('',views.home,name='website-home'),
	path('view_resume',views.resume,name="view_resume"),
	path('edit_resume',views.edit_resume,name="edit_resume"),
	path('main/',views.index),
    path('sign_up/',views.form,name="sign_up"),
    path('sign_in/',views.SignIn,name="sign_in"),
    path('candidate/', views.ChangeP),
    path('Security/', views.SecurityC),
    path('hr/', views.ChangeP),

    #######TEAM APLHA#######
    path('jobhome', views.index, name='index'),
    path('display',views.display), 
    path('internshiphome',views.index1),
    path('createinternship',views.createinternship),
    url(r'create', views.create, name='create'),
    url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
	url('show',views.show), 
	
    #url(r'^create1', views.create1, name='create1'),
	url(r'^edit1/(?P<id>\d+)$', views.edit1, name='edit1'),
    url(r'^edit1/update1/(?P<id>\d+)$', views.update1, name='update1'),
    url(r'^delIntern/(?P<id>\d+)$', views.delIntern, name='delIntern'),
    path('res',views.intershipresume,name='internship-resume'),
	path('rese',views.edit_intershipresume,name='internship-resume'),
    #######DEV GURU#######
    path('hr/jobs',views.view_jobs_hr,name="view_jobs_hr"),
    path('hr/jobs/<int:num>',views.view_job_hr,name="view_job_hr"),
    path('hr/jobs/<int:jobId>/applicant/<int:applicantId>/interview',views.schedule_interview_hr,name="schedule_interview_hr")
]
