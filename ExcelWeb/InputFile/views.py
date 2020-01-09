from django.shortcuts import render
from .models import InputFile
# Create your views here.
def InputFile_detail(request, file_id):
    afile = InputFile.objects.get(id = file_id)
    pass