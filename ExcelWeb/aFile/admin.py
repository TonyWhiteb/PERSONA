from django.contrib import admin

# Register your models here.
from .models import aFile

@admin.register(aFile)
class aFileAdmin(admin.ModelAdmin):
    list_display = ('id','file_name','file_type','input_time','created_by','last_updated_time')