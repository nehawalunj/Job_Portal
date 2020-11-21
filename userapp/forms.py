from django import forms
from userapp.models import UserRegister
from Firstapp.models import MechanicalJobs,CivilJobs,ItJobs


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserRegister
        fields = "__all__"

class MechanicalJobsForm(forms.ModelForm):
    class Meta:
        model = MechanicalJobs
        fields = "__all__"

class ItJobsForm(forms.ModelForm):
    class Meta:
        model = ItJobs
        fields = "__all__"

class CivilJobsForm(forms.ModelForm):
    class Meta:
        model = CivilJobs
        fields = "__all__"
