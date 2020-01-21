from django.shortcuts import render, get_object_or_404
from .models import aFile 
# Create your views here.

def file_list(request):
    context = {}
    context['files'] = aFile.objects.all()
    context['file_total'] = aFile.objects.all().count()
    return render(request, 'file_list.html', context= context)

def file_type_page(request, file_pk):
    context  = {}
    file_type = get_object_or_404(aFile, pk = file_pk)
    context['file'] = aFile.objects.filter()
    return render(request, 'file_type_page.html', context= context)