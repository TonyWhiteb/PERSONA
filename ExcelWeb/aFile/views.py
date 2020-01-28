from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import aFileFieldForm
# Create your views here.

def model_from_upload(request):
    if request.method == 'POST':
        form = aFileFieldForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')
        else:
            form = aFileFieldForm()
        return render(request, 'file_upload.html', {'form':form})