from django.contrib import admin

from userapp.models import UserRegister
from userapp.models import MechanicalJobs,ItJobs,CivilJobs
# Register your models here.
admin.site.register(UserRegister)
admin.site.register(MechanicalJobs)
admin.site.register(ItJobs)
admin.site.register(CivilJobs)
