from django.shortcuts import render, redirect
from events.models import Event, EventCategory
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from events.forms import EventForm

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

@login_required(login_url='/intern/login')
def show_events_editing(request):
    all_events = Event.objects.all()
    context = {
        'all_events': all_events
        }
    return render(request, "events/edit/show_event_editing.html", context)

@login_required(login_url='/intern/login')
def event_edit(request, pk):
    post = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('show_events_editing')
    else:
        form = EventForm(instance=post)
    return render(request, 'events/edit/form.html', {'form': form})

@login_required(login_url='/intern/login')
def create_event(request):
    form = EventForm(request.POST)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = EventForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            composer = form.cleaned_data['composer']
            contributing = form.cleaned_data['contributing']
            content = form.cleaned_data['content']
            image = form.cleaned_data['image']
            image_desc = form.cleaned_data['image_desc']
            content = form.cleaned_data['content']
            content_lead = form.cleaned_data['content_lead']
            text = form.cleaned_data['text']
            slug = form.cleaned_data['slug']
            published_year = form.cleaned_data['published_year']
            ticket_url = form.cleaned_data['ticket_url']
            # request DATA
            name = request.POST['name']
            composer = request.POST['composer']
            contributing = request.POST['contributing']
            image = request.FILES['image']
            image_desc = request.POST['image_desc']
            content = request.POST['content']
            content_lead = request.POST['content_lead']
            text = request.POST['text']
            published_year = request.POST['published_year']
            ticket_url = request.POST['ticket_url']
            slug = request.POST['slug']
            new_event = Event(name=name,
                              category=category,
                              composer=composer,
                              contributing=contributing,
                              image=image,
                              image_desc=image_desc,
                              slug=slug,
                              content=content,
                              content_lead=content_lead,
                              text=text,
                              published_year=published_year,
                              ticket_url=ticket_url)
            new_event.save()
            # redirect to a event_url:
            return redirect('event_thanks')
            # if a GET (or any other method) we'll create a blank form
    context = {
        'form': form
        }
    return render(request, "events/edit/form.html", context)

@login_required(login_url='/intern/login/')
def event_thanks(request):
    return render(request, "events/edit/form_thanks.html")
