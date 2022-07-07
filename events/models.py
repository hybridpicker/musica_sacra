import datetime
from django.db import models
from django.utils.translation import gettext as _

import datetime


#Quill Editor
from django_quill.fields import QuillField

# Create your models here.
class EventCategory(models.Model):
    name = models.CharField(_(u'Name of Category'), max_length=100)
    ordering = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return '%s' % (self.name)

    class Meta: 
        '''
        Meta class for EventCategory
        '''
        ordering = ['ordering']        
        verbose_name = u'EventCategory'
        verbose_name_plural = u'EventCategories'   

#Function for generating year-slug-string in view
def current_year():
    return datetime.date.today().year

class Event(models.Model):
    '''
    Model holding events data
    '''
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(_(u'Name of Event'), max_length=100)
    composer = models.CharField(_(u'Composer'), max_length=500, blank=True)
    contributing = models.CharField(_(u'Contributing'), max_length=500, blank=True)
    venue = models.CharField(_(u'Venue'), max_length=80, blank=True)
    date = models.DateField(
        _("date for event"),
        default=datetime.date.today, blank=True)
    time = models.TimeField(_("Event Time "), db_index=True,
                            null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    content_title = models.TextField(null=True, blank=True)
    content_lead = models.TextField(null=True, blank=True)
    content = QuillField(null=True, blank=True)
    published_year = models.IntegerField(_('Year of Article'), default=current_year())
    slug = models.SlugField(_("slug"), max_length=200, unique=True, null=True)
    image = models.ImageField(upload_to='events/images/', null=True)
    image_desc = models.TextField(null=True, blank=True)
    ticket_url = models.URLField(_(u'Ticket URL Seite'), blank=True, max_length=80)

    def get_date_presentation(self):
        tp = self.date
        import locale
        locale.setlocale(locale.LC_ALL, 'de_DE')
     #  dayname = tp.strftime('%a')
        day = tp.strftime('%d')
        month = tp.strftime('%m')
        return str(day + '.' + month + '.')

    def get_time_presentation(self):
        tp = self.time
        hour = tp.strftime('%H')
        minutes = tp.strftime('%M')
        return str(hour + ':' + minutes + ' Uhr')

    def __str__(self):
        return '%s - %s' % (self.name, self.date)

    class Meta: 
        '''
        Meta class for Event
        '''
        ordering = ('date',)
        verbose_name = u'Event'
        verbose_name_plural = u'Events' 