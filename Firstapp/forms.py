from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Firstapp.models import MechanicalJobs,CivilJobs,ItJobs  #import from models.py model classes

# forms are here
class AdminRegister(UserCreationForm):     #AdminRegister we have created class and Usercreation form inherited here
    class Meta:
        model = User                   #model class name
        fields = ["username","password1","password2"]

class MechanicalJobsForm(forms.ModelForm):         #MechnicalJobs
    class Meta:
        model = MechanicalJobs
        fields = "__all__"

class ItJobsForm(forms.ModelForm):         #ITJobs
    class Meta:
        model = ItJobs
        fields = "__all__"

class CivilJobsForm(forms.ModelForm):         #civilJobs
    class Meta:
        model = CivilJobs
        fields = "__all__"
