from django.shortcuts import render,include
from django.http import JsonResponse
from django.views import View

from .forms import DocForm
from .models import Document
# Create your views here.

class BasicUploadView(View):
    def get(self, request):
        file_list = Document.objects.all()
        return render(self.reqeust, '')
X