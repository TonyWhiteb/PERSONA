from django import forms
from .models import FileFieldForm

class aFileFieldForm(forms.ModelForm):
    class Meta:
        model = FileFieldForm
        fields = ('upload_by', 'fiel_field')
