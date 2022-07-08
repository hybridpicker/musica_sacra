from django.utils.translation import gettext as _
from django import forms
from django_quill.forms import QuillFormField
from .models import Event

class EventForm(forms.ModelForm):
    content = QuillFormField()
    class Meta:
        model = Event
        fields = ['name', 'category', 'composer', 'contributing', 'venue', 'date', 
                'content_title', 'content_lead', 'content', 'image', 'image_desc',
                'ticket_url']
