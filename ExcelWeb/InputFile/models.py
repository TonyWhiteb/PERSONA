from django.db import models

# Create your models here.

class InputFile(models.Model):

    FILE_TYPE = (
        ('.xlsx','Excel File'),
        ('.txt','Text File'),
        ('.error','Error File'),
    )    

    file_name = models.CharField(max_length= 30)
    file_type = models.CharField(max_length=10, choices= FILE_TYPE)