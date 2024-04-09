from django.shortcuts import render, redirect
# from .forms import UploadFileForm
from .forms import FileUploadForm 
from .models import UploadedFile
from django.contrib import messages

def teacherhomee(request):
  return render(request, 'teacher.html') 

def upload_filee(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)  # Bind form data to request data
        if form.is_valid():# Check if form data is valid
            
            uploaded_file = form.cleaned_data['file']  # Get the uploaded file from form data
            owner = request.username
            
            with open(uploaded_file.name, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            
            # Create a new UploadedFile object with the saved file path
            uploaded_file_obj = UploadedFile.objects.create(file=uploaded_file.name, owner=owner)
            
            messages.info(request, "File Uploaded Successfully")  # Render success template
            return redirect('teacher')
    else:
        form = FileUploadForm()  # Create a form instance for GET requests
    return render(request, 'teacher.html', {'form': form})  # Render form template with form instance











# def upload_filee(request):
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST, request.FILES)  # Bind form data to request data
#         if form.is_valid():  # Check if form data is valid
#             uploaded_file = form.cleaned_data['file']  # Get the uploaded file from form data
#             with open(uploaded_file.name, 'wb+') as destination:
#                 for chunk in uploaded_file.chunks():
#                     destination.write(chunk)
#     # Create a new UploadedFile object with the saved file path
#             uploaded_file_obj = UploadedFile.objects.create(file=uploaded_file.name)
        
#             messages.info(request, "File Uploaded Successfully")  # Render success template
#             return redirect('teacher')
#     else:
#         form = FileUploadForm()  # Create a form instance for GET requests
#     return render(request, 'teacher.html', {'form': form})  # Render form template with form instance

    # if request.method == 'POST':
    #     uploaded_file = request.FILES.get('file')
    #     if uploaded_file:
    #         with open('path/to/save/' + uploaded_file.name, 'wb+') as destination:
    #             for chunk in uploaded_file.chunks():
    #                 destination.write(chunk)
    #         return render(request, 'file_uploaded.html')
    # return render(request, 'upload_file.html')
    #     form = UploadFileForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         print("formsaved")
    #         # messages.info(request, "File is Uploaded Successfully")
    #         return redirect('upload_file')
    # else:
    #     form = UploadFileForm()
    
    # uploaded_files = UploadedFile.objects.all()
    # return render(request, 'teacher.html', {'form': form, 'uploaded_files': uploaded_files})
