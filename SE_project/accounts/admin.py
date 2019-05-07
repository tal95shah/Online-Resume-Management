from django.contrib import admin
from accounts import models
# Register your models here.
class ApplicantAdmin(admin.ModelAdmin):
    list_display=['user','date_of_birth','contact_num1']

    search_fields=['user.username']

admin.site.register(models.signup)
admin.site.register(models.Profile)
admin.site.register(models.Reference)
admin.site.register(models.Hr_Manger)
admin.site.register(models.Applicant,ApplicantAdmin)
admin.site.register(models.Job)
admin.site.register(models.Interview)
admin.site.register(models.Internship)
admin.site.register(models.InterviewQuestion)
admin.site.register(models.Experience)
admin.site.register(models.Databackup)
admin.site.register(models.Qualification)
admin.site.register(models.Resume)
admin.site.register(models.Intern)
admin.site.register(models.InternshipResume)
admin.site.register(models.InternshipReference)
admin.site.register(models.InternshipExperience)
admin.site.register(models.Department)
admin.site.register(models.Institute)
admin.site.register(models.Degree)
admin.site.register(models.Field)
