from django.shortcuts import render
from events.models import Event
from home.models import IndexText

# Create your views here.
def home (request):
    events = Event.objects.all().filter(category__name="Konzert")
    index_text = IndexText.objects.all().first()
    context = { 'events': events ,
                'index_text': index_text,}
    return render (request, 'home/index.html', context)

def contact (request):
    return render (request, 'home/contact.html')

def prices (request):
    return render (request, 'home/prices.html')

def impressum (request):
    return render (request, 'home/impressum.html')

def about (request):
    return render (request, 'home/about.html')