from django.conf.urls import url
from . import views


urlpatterns = [
    url('index2', views.index2, name='index2'),
    url('hassan', views.hassan, name='hassan'),
    url('post_job', views.post_job, name='post_job'),
    url('sign2_recruiter', views.sign2_recruiter, name='sign2_recruiter'),
    url('my_connections', views.my_connections, name='my_connections'),
    url('send_requsts', views.send_requsts, name='send_requsts'),
    url('edit_profile', views.edit_profile, name='edit_profile'),
    url('suggested', views.suggested, name='suggested'),
    url('sign2', views.sign2, name='sign2'),
    url('login', views.login, name='login'),
    url('job-details/(?P<id>\d+)', views.job_details, name='job-details'),
    url('job-details/(?P<id>\d+)/(?P<uid>\d+)', views.job_details, name='job-details'),
    
    url('wall', views.wall, name='wall'),
    url('details/(?P<id>\d+)', views.details, name='details'),
    
    url('details/(?P<id>\d+)/(?P<uid>\d+)', views.details, name='details'),

    url('jobapply/(?P<id>\d+)/(?P<uid>\d+)', views.jobapply, name='jobapply'),
    url('jobposted', views.jobposted, name='jobposted'),
    url('request', views.request, name='request'),
    
    url('sign_up_applicant', views.sign_up_applicant, name='sign_up_applicant'),
    url('sign_up_recruiter', views.sign_up_recruiter, name='sign_up_recruiter'),
    url('update_profile', views.update_profile, name='update_profile'),
    url('attempt_log_in', views.attempt_log_in, name='attempt_log_in'),
    

    

    url('', views.index, name='index'),
    
]
