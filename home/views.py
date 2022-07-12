from django.shortcuts import render, redirect
from events.models import Event
from home.models import IndexText
from home.forms import IndexTextForm
from django.contrib.auth.decorators import login_required

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


@login_required(login_url='/intern/login')
def index_text_edit(request):
    index_text = IndexText.objects.all().first()
    if request.method == "POST":
        form = IndexTextForm(request.POST, instance=index_text)
        if form.is_valid():
            index_text = form.save(commit=False)
            index_text.save()
        return redirect('event_thanks')
    else:
        form = IndexTextForm(instance=index_text)
    return render(request, 'home/edit/form.html', {'form': form})