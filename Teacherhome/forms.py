from django import forms

class FileUploadForm(forms.Form):
    file = forms.FileField()
# from django import forms
# from .models import UploadedFile

# class UploadFileForm(forms.ModelForm):
#     class Meta:
#         model = UploadedFile
#         fields = ['file']
#         fields = ['file','permission']
