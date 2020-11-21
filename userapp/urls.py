from django.contrib import admin
from django.urls import path
from userapp import views
#this is url for userapp apllication level

urlpatterns = [
    #path('index/',views.index),    #thus is url/link for index/front page with the index fun from views
    path('user/',views.user_index),    #this is for Userregister and user login

    path('userregister/',views.user_view),
    path('userlogin/',views.user_login),

    path('welcome/',views.welcome),  #this is for types of jobs

    path('usermechanical/',views.user_mech_jobs),       #thus is to show mech Jobs
    path('userit/',views.user_it_jobs),                #thus is to show it Jobs
    path('usercivil/',views.user_civil_jobs),       #thus is to show civil Jobs

    path("searchmech/",views.search_mech),       #this is to search mech jobs

]
