from django.contrib import admin
from .models import FileFieldForm
# Register your models here.


@admin.register(FileFieldForm)
class FileFieldFormAdmin(admin.ModelAdmin):
    list_display = ['title', 'upload_by', 'create_time', 'last_update']
