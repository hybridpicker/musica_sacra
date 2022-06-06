from django.contrib import admin
from django.urls import path
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
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)