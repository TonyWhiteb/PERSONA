from django.urls import path
from . import views

urlpatterns = [
    path('type/<int: file_pk>', views.file_type_page, name='file_type_page'),
]
