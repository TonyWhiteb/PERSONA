from django.contrib import admin
from .models import Document
# Register your models here.


@admin.register(Document)
class MainModel(admin.ModelAdmin):
    list_display = ['title','upload_by','datestamp']
