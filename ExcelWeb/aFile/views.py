from django.shortcuts import render, get_object_or_404
from .models import aFile 
# Create your views here.

def file_list(request):
    context = {}
    context['files'] = aFile.objects.all()
    return render(request, 'file_list.html', context= context)

def file_upload(request, file_pk):
    context  = {}
    context['file'] = get_object_or_404(aFile, pk= file_pk)
    return render(request, 'file_upload.html', context= context)