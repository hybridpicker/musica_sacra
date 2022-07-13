from django.utils.translation import gettext as _
from django import forms
from django_quill.forms import QuillFormField
from .models import BlogPost

class ArticleForm(forms.ModelForm):
    content = QuillFormField()
    class Meta:
        model = BlogPost
        fields = ['content', 'image', 'title', 'lead_paragraph', 
                  'meta_title', 'meta_description']
