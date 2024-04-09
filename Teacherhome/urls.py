from django.urls import path
# from .views import upload_file
from . import views

urlpatterns = [
    path('teacherhome',views.teacherhomee,name='teacherhomee'),
    path('upload_file/',views.upload_filee, name='upload_filee'),
]