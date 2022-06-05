from django.shortcuts import render
from events.models import Event, EventCategory

# Create your views here.
def program (request):
    events = Event.objects.all()
    categories = EventCategory.objects.all()
    context = { 'events': events, 
                'categories': categories,}
    return render (request, 'home/program.html', context)