from django.contrib import admin
from django.urls import path, include, re_path
import home.views
import events.views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.home, name='home_view'),
    path('programm/', events.views.program, name='program_view'),
    path('kontakt/', home.views.contact, name='contact_view'),
    path('ueber-uns/', home.views.about, name='about_view'),
    path('karten/', home.views.prices, name='prices_view'),
    path('impressum/', home.views.impressum, name='impressum_view'),
    path('intern/', include('users.urls')),
    # Home Url
    path('index-text/edit/', home.views.index_text_edit, name='index_edit_detail'),
    # Get Single Event View
    path('<published_year>/<slug>/', events.views.EventView.as_view(), name='event_detail'),
    re_path(r'^eventedit/', include('events.edit_urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)