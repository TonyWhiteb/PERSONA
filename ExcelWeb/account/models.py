from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(User):
    
    pass

class Documents(models.Model):
    title = models.CharField(max_length=255, blank=True)
    afile = models.FileField(upload_to='docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)