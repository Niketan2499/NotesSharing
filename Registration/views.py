from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from Studenthome.views import *
from .models import CustomUser
# here i have used login(request), override ho rha tha , import wala login 
def login_views(request):
    return render(request, 'login.html') 


def handlestudentsignup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        # here i used firstname in place of first_name toh data nahi ja rha tha 
        last_name=request.POST['last_name']
        branch=request.POST['branch']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'Dear Student, Username is already taken.')
            return redirect('login')
        
        myuser = CustomUser.objects.create_user(username=username, email=email, password=password)
        myuser.usertype='Student'
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.branch = branch
        myuser.save()
        
        messages.info(request, "Your Account has been successfully created.")

        return render(request,'login.html')

    else:
        return render(request,'home.html')
    

def handleteachersignup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        
        if CustomUser.objects.filter(username=username).exists():
            messages.info(request, 'Dear Teacher, Username is already taken.')
            return redirect('login')
        
        myuser = CustomUser.objects.create_user(username=username, email=email, password=password)
        myuser.usertype='Teacher'
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        
        messages.success(request, "Your Account has been successfully created.")
        
        return render(request,'login.html')
    
    else:
        return render(request,'home.html')
 
    
def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
    
        # Add request parameter here
        user = authenticate(request, username=loginusername, password=loginpassword)
        
        if user is not None:
            login(request, user)  
            if user.usertype=='Student':
                print("cutomuser k under student wala")
                return render(request, 'student.html', {'user': user})
            elif user.usertype=='Teacher':
                print("teacher k under")
                return render(request, 'teacher.html', {'user': user})
            else:
                return HttpResponse("User Not Found")

        else: 
            messages.error(request, "Invalid Credentials, Please try again")
            # redirect me login.html likhne pr error page not found  
            return redirect('login')

        
        

def handlelogout(request):
    logout(request) 
    messages.info(request,"Successfully Logged Out ")
    return redirect('login')
     
