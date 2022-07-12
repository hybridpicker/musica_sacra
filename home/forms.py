from django import forms
from django_quill.forms import QuillFormField
from .models import IndexText

class IndexTextForm(forms.ModelForm):
    content = QuillFormField()
    class Meta:
        model = IndexText
        fields = ['content']
