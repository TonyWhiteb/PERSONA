from django.urls import path
from . import views

urlpatterns = [
    path('', views.file_upload, name = 'upload_home'),
    # path('upload/', views.simple_upload, name = 'simple_upload'),
]
