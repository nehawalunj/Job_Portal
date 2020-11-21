#this is urls.py file for application level

from django.contrib import admin
from django.urls import path
from Firstapp import views     #this is importing views from apllication
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/',views.index),    #thus is url/link for index/front page with the index fun from views
    path('postjobs/',views.postjobs),     #this is for administration login
    path('adminregister/',views.admin_register),  #this url for registration of admin
    path('contactus/',views.contact_us),
    path('aboutus/',views.about_us),
     #this url for login of admin after register
    path('adminlogin/',auth_views.LoginView.as_view(template_name="Firstapp/adminlogin.html")),
    path('adminlogout/',auth_views.LogoutView.as_view()),
    path('admindashboard/',views.admindashboard),   #showing types of jobs

    #this is for mechanical jobs
    path('addmechjobs/',views.mech_add_data),      #add mechanical jobs
    path('mechdata/',views.mech_data),   #add data to mech jobs table
    path('mechdelete/<int:id>/',views.delete_mech),  #delete data from mech table
    path('mechupdate/<int:id>/',views.mech_update),   #upate data from mech table
    #this is for IT jobs
    path('additjobs/',views.it_add_data),      #add IT jobs
    path('itdata/',views.it_data),   #add data to IT jobs table nd show
    path('itdelete/<int:id>/',views.delete_it),  #delete data from IT table
    path('itupdate/<int:id>/',views.it_update),   # update data in IT table
    #this is for Civil postjobs
    path('addciviljobs/',views.civil_add_data),      #add civil jobs
    path('civildata/',views.civil_data),   #add data to civil jobs table nd show
    path('civildelete/<int:id>/',views.delete_civil),  #delete data from civil table
    path('civilupdate/<int:id>/',views.civil_update),   # update data in civil table


]
