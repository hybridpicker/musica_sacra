from django.db import models
from django.utils.translation import gettext as _
#Quill Editor
from django_quill.fields import QuillField

# Create your models here.
class IndexText(models.Model):
    content = QuillField(_("Text Startseite"),null=True, blank=True)

    def __str__(self):
        return '%s' % ('Index Text')

    class Meta: 
        '''
        Meta class for Index Text
        '''
        verbose_name = u'Index Text'
        verbose_name_plural = u'Index Texts'   

class Alert(models.Model):
    title = models.CharField(max_length=255, default="Untitled")  # Titel für den Alert
    message = models.TextField()  # Längeres Textfeld für den Inhalt des Alerts
    is_active = models.BooleanField(default=False)  # Flag, um zu entscheiden, ob der Alert aktiv ist
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # Anzeige des Titels im Admin-Bereich

