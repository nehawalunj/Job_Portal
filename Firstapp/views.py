from django.shortcuts import render,redirect
from Firstapp.forms import AdminRegister,MechanicalJobsForm,ItJobsForm,CivilJobsForm
 #forms importd from forms.py
from Firstapp.models import MechanicalJobs,ItJobs,CivilJobs
#model class imported from models.py


#************************home page***************************
#thius is view for index.html or index page having url /index/
def index(request):
    return render(request,"index.html")
#this is for administration login
def postjobs(request):
    return render(request,"postjobs.html")
def contact_us(request):
    return render(request,"contactus.html")
def about_us(request):
    return render(request,"aboutus.html")
#*****************admin******************************************
#thus is for admin registration
def admin_register(request):
    form=AdminRegister()
    if request.method == "POST":
        form = AdminRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/firstapp/adminlogin/")
    return render(request,"adminregister.html",{"form":form})
#this is for admin login
def admin_login(request):
    form=AdminRegister()
    return render(request,"firstapp/adminlogin.html",{"form":form})

#this is for admin dashboard where types of jobs available after login
def admindashboard(request):
    return render(request,"admindashboard.html")


#***************this is to show mechanical jobs table*************

#this is for mech jobs entering dataa
def mech_add_data(request):
    form = MechanicalJobsForm()
    if request.method == "POST":
        form = MechanicalJobsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/firstapp/mechdata/")
    return render(request,"addmech.html",{"form":form})
#this is to show mech data into table
def mech_data(request):
    data = MechanicalJobs.objects.all()
    print(data)
    return render(request,"mechanicaljob.html",{"data":data})
#this is for delete mech mech_data
def delete_mech(request,id):
    obj = MechanicalJobs.objects.get(pk=id)
    obj.delete()
    return redirect("/firstapp/mechdata/")
#this is for updating dataa im mechnicals jobs
def mech_update(request,id):
    obj = MechanicalJobs.objects.get(pk=id)
    form = MechanicalJobsForm(instance=obj)
    if request.method == "POST":
        form = MechanicalJobsForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect("/firstapp/mechdata/")
    return render(request,"mechupdate.html",{"form":form,"obj":obj})


#***************this is to show IT jobs table ****************************
#this is for IT jobs entering dataa
def it_add_data(request):
    form = ItJobsForm()
    if request.method == "POST":
        form = ItJobsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/firstapp/itdata/")
    return render(request,"addit.html",{"form":form})
#this is to show mech data into table
def it_data(request):
    data = ItJobs.objects.all()
    print(data)
    return render(request,"itjob.html",{"data":data})
#this is for delete mech mech_data
def delete_it(request,id):
    obj = ItJobs.objects.get(pk=id)
    obj.delete()
    return redirect("/firstapp/itdata/")
#this is for updating dataa im mechnicals jobs
def it_update(request,id):
    obj = ItJobs.objects.get(pk=id)
    form = ItJobsForm(instance=obj)
    if request.method == "POST":
        form = ItJobsForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect("/firstapp/itdata/")
    return render(request,"itupdate.html",{"form":form,"obj":obj})


#************this is for Civil  jobs table*******************************
#this is for IT jobs entering dataa
def civil_add_data(request):
    form = CivilJobsForm()
    if request.method == "POST":
        form = CivilJobsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/firstapp/civildata/")
    return render(request,"addcivil.html",{"form":form})
#this is to show mech data into table
def civil_data(request):
    data = CivilJobs.objects.all()
    print(data)
    return render(request,"civiljob.html",{"data":data})
#this is for delete mech mech_data
def delete_civil(request,id):
    obj = CivilJobs.objects.get(pk=id)
    obj.delete()
    return redirect("/firstapp/civildata/")
#this is for updating dataa im mechnicals jobs
def civil_update(request,id):
    obj = CivilJobs.objects.get(pk=id)
    form = CivilJobsForm(instance=obj)
    if request.method == "POST":
        form = CivilJobsForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
        return redirect("/firstapp/civildata/")
    return render(request,"civilupdate.html",{"form":form,"obj":obj})
#******************************************************************************
