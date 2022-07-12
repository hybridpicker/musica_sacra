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