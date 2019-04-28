from django.contrib import admin

# Register your models here.
from mysite.models import *


admin.site.register(Designation)
admin.site.register(HRManager)
admin.site.register(Department)
admin.site.register(Offices)