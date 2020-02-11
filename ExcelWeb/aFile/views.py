from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .models import MainModel, Document
from django.core.files.storage import FileSystemStorage

import os
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .forms import DocumentForm
# Create your views here.
# def upload_home(request):
#     aFile = FileFieldForm.objects.all()
#     return render(request, 'upload.html', {'aFile': aFile})


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         upload_file_url = fs.url(filename)
#         return render(request, 'simple_upload.html', {'upload_file_url': upload_file_url})

#     return render(request, 'simple_upload.html')

@require_POST
def file_upload(request):
    # save_path = os.path.join(settings.MEDIA_ROOT,request.FILES['file'])


    myfile = request.FILES('file')
    fs = FileSystemStorage()
    path = fs.save(myfile.name,myfile)
    document = Document.objects.create(document=path,upload_by=request.user)
    return JsonResponse({'document':document.id})

@require_POST
def file_upload_test(request):
    form = DocumentForm(request.POST, request.FILES)
    myfile = request.FILES('file')
    if form.is_valid():
        new_file = Document()