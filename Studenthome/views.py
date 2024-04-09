from django.shortcuts import render

def studenthome(request):
  return render(request,'student.html')
def teacherhome(request):
  return render(request,'teacher.html')
  
  
  