from django.shortcuts import render
# from django.http import HttpResponseRedirect
from .models import FileFieldForm
from django.core.files.storage import FileSystemStorage
# Create your views here.
def home(request):
    aFile = FileFieldForm.objects.all()
    return render(request, 'home.html', {'aFile': aFile})


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        upload_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {'upload_file_url': upload_file_url})

    return render(request, 'simple_upload.html')
