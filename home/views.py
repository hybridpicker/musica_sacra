from django.shortcuts import render
from events.models import Event, EventCategory

# Create your views here.
def home (request):
    return render (request, 'home/index.html')

def contact (request):
    return render (request, 'home/contact.html')

def program (request):
    events = Event.objects.all()
    categories = EventCategory.objects.all()
    context = { 'events': events, 
                'categories': categories,}
    return render (request, 'home/program.html', context)

def about (request):
    return render (request, 'home/about.html')