from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime

#Quill Editor
from django_quill.fields import QuillField

#Sorl Thumbnail
from sorl.thumbnail import ImageField

#Function for generating year-slug-string in view
def current_year():
    return datetime.date.today().year

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    lead_paragraph = models.TextField(blank=True)
    number_of_posts = models.IntegerField(null=True, blank=True)
    content = QuillField(_("Beitragsinhalt"))
    image = ImageField(_("Beitragsbild"), upload_to='blog/images/', null=True, blank=True)
    image_desc = models.TextField(_("Bildbezeichnung"), null=True, blank=True)
    date = models.DateField(_(u"Blog Post Date"), default=timezone.now, blank=True)
    published_year = models.IntegerField(_('Year of Article'), default=current_year)
    meta_title = models.CharField(max_length=60)
    meta_description = models.TextField()
    slug = models.SlugField(_("slug"), max_length=200, unique=True)

    def __str__(self):
        return '%s (%s)' % (self.title, self.published_year)

    class Meta:  # pylint: disable=too-few-public-methods
        '''
        Meta class for BlogPosts
        '''
        ordering = ('-date',)
        verbose_name = u'Blog Post'
        verbose_name_plural = u'Blog Posts'
