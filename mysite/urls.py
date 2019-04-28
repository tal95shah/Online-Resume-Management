from django.urls import path

from mysite import views
from mysite.views import *

urlpatterns = [
    path('', index),
    path('addDepartment', addDepartment ,name='adddept'),
    path('DeleteDepartment', DeleteDepartment,name='deletedept'),
    path('ViewDepartment', ViewDepartment,name='viewdept'),
    path('addDesignation', addDesignation,name='adddes'),
    path('RemoveDesignation', RemoveDesignation,name='deletedes'),
    path('ViewDesignation',ViewDesignation,name='viewdes'),
    path('addOffice', addOffice,name='addo'),
    path('viewOffice', viewOffice,name='viewo'),
    path('RemoveOffice', RemoveOffice,name='deleteo'),

]