from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

# class TypeManager(models.Manager):
#     # type_name = models.CharField(max_length= 6)
#     def get_file_type(self,file_name):
#         afile = self.


class aFile(models.Model):
    file_name = models.CharField(max_length=50)
    file_type = models.CharField(max_length=6)
    input_time = models.DateTimeField(auto_now_add= True) #update once on creation only
    is_deleted = models.BooleanField(default= False)
    created_by = models.ForeignKey(User, on_delete= models.DO_NOTHING) #Do nothing - Consistency must be handled elsewhere
    last_updated_time = modesl.DateTimeField(auto_now = True) #update each time when calling models.save()
    # file_col = models
    @classmethod
    def get_file_type(cls):
        pass

