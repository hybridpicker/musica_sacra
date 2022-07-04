from django.shortcuts import render
from events.models import Event

# Create your views here.
def home (request):
    events = Event.objects.all().filter(category__name="Konzert")
    context = { 'events': events }
    return render (request, 'home/index.html', context)

def contact (request):
    return render (request, 'home/contact.html')

def prices (request):
    return render (request, 'home/prices.html')

def impressum (request):
    return render (request, 'home/impressum.html')

def about (request):
    return render (request, 'home/about.html')