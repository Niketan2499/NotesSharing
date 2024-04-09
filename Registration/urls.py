from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_views, name="login"),
    path('studentsignup', views.handlestudentsignup, name='handlestudentsignup'),
    path('teachersignup', views.handleteachersignup, name='handleteachersignup'),
    path('userlogin', views.handlelogin, name='handlelogin'),
    path('userlogout', views.handlelogout, name='handlelogout'),
]