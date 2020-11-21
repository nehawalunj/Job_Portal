from django.shortcuts import render,redirect
from userapp.forms import UserRegisterForm
from userapp.models import UserRegister
from django.contrib import messages
from Firstapp.forms import MechanicalJobsForm,ItJobsForm,CivilJobsForm
from Firstapp.models import MechanicalJobs,ItJobs,CivilJobs
from django.db.models import Q

#this is for User panel where user login and register
def user_index(request):
    return render(request,"user.html")
#******************user registration *************************************
def user_view(request):
    form = UserRegisterForm()
    if request.method == "POST":
        form = UserRegisterForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/userapp/userlogin/")
    return render(request,"userregister.html",{"form":form})

#***********************user login*****************************************
def user_login(request):
    print(request.POST)
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("upass")
        print(username,password)
        try:
            user = UserRegister.objects.get(username = username, password = password)
            print(user)
            if user is not None:
                return redirect("/userapp/welcome/")
            else:
                return redirect("/userapp/userlogin")
        except:
            messages.error(request,"Please enter valid username or password")
            return redirect("/userapp/userlogin/")
    return render(request,"userlogin.html")

#******************* user welcome page for jobs showing************
def welcome(request):
    return render(request,"welcome.html")

#**********************User mechnical table show*******************************
def user_mech_jobs(request):
    data = MechanicalJobs.objects.all()
    return render(request,"usermechjob.html",{"data":data})

def search_mech(request):
    print(request.GET)
    x = request.GET.get("data")
    form = MechanicalJobsForm(instance=x)
    data = MechanicalJobs.objects.filter(Q(company_name__contains = x)|Q(job_title__contains = x)|Q(designation__contains = x)|Q(location__contains = x))
    print(data)
    return render(request,"search_mech.html",{"data":data,"x":x})
#**********************User IT table show*******************************
def user_it_jobs(request):
    data = ItJobs.objects.all()
    return render(request,"useritjob.html",{"data":data})
#**********************User civil table show*******************************
def user_civil_jobs(request):
    data = CivilJobs.objects.all()
    return render(request,"userciviljob.html",{"data":data})
