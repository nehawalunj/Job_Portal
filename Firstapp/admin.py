from django.contrib import admin
from django.db import models
#import all the model class/databse tables which have created in models.
from Firstapp.models import MechanicalJobs
from Firstapp.models import ItJobs
from Firstapp.models import CivilJobs

#register It job info table from model
class MechanicalJobsAdmin(admin.ModelAdmin):
    list_display = ['company_name','job_title','description','designation','experience','package','location']     # this method display mentioned fields in admin panel
admin.site.register(MechanicalJobs,MechanicalJobsAdmin)
#register It job info table from model
class ItJobsAdmin(admin.ModelAdmin):
    list_display = ['company_name','job_title','description','designation','experience','package','location']     # this method display mentioned fields in admin panel
admin.site.register(ItJobs,ItJobsAdmin)
#register It job info table from model
class CivilJobsAdmin(admin.ModelAdmin):
    list_display = ['company_name','job_title','description','designation','experience','package','location']     # this method display mentioned fields in admin panel
admin.site.register(CivilJobs,CivilJobsAdmin)

      
