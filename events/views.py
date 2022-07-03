from django.shortcuts import render
from events.models import Event, EventCategory
from django.shortcuts import get_object_or_404
from django.views.generic import View

# Create your views here.
def program (request):
    events = Event.objects.all()
    categories = EventCategory.objects.all()
    context = { 'events': events, 
                'categories': categories,}
    return render (request, 'home/program.html', context)

class EventView(View):
    def get(self, request, *args, **kwargs):
        event = get_object_or_404(Event, slug=kwargs['slug'], published_year=kwargs['published_year'])
        context = {'event': event}
        return render(request, 'events/single_event.html', context)