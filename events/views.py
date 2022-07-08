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
            title = form.cleaned_data['title']
            lead_paragraph = form.cleaned_data['lead_paragraph']
            content = form.cleaned_data['content']
            title = request.POST['title']
            lead_paragraph = request.POST['lead_paragraph']
            image = request.FILES['image']
            content = request.POST['content']
            #create slug from title-input
            slug = create_slug_text(title)
            new_event = Event(title=title,
                                lead_paragraph=lead_paragraph,
                                image=image,
                                slug=slug,
                                meta_title=title,
                                meta_description=lead_paragraph,
                                content=content)
            new_event.save()
            # redirect to a event_url:
            return redirect('event_thanks')
            # if a GET (or any other method) we'll create a blank form
        else:
            form = EventForm()
    context = {
        'form': form
        }
    return render(request, "events/edit/form.html", context)