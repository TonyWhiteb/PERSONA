from django import forms

from .models import Document

class DocForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file',)