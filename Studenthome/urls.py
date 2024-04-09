from . import views
from django.urls import path

urlpatterns = [
    path('student/', views.studenthome, name='studenthome'),
]