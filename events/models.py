import datetime
from django.db import models
from django.utils.translation import gettext as _

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

    def get_date_presentation(self):
        tp = self.date
        import locale
        locale.setlocale(locale.LC_ALL, 'de_DE')
        dayname = tp.strftime('%a')
        day = tp.strftime('%d')
        month = tp.strftime('%m')
        return str(dayname + ' ' + day + '.' + month + '.')

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