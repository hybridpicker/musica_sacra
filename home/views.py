from django.shortcuts import render, redirect
from events.models import Event, EventCategory
from blog.models import BlogPost
from home.models import IndexText, Alert  # Importiere das neue Alert-Modell
from home.forms import IndexTextForm
from django.contrib.auth.decorators import login_required

def home(request):
    try:
        # Versuch, die Kategorie "Konzert" zu finden
        concert_category = EventCategory.objects.get(name="Konzert")
    except EventCategory.DoesNotExist:
        # Falls diese nicht existiert, benutze die erste verfügbare Kategorie
        concert_category = EventCategory.objects.first()

    if concert_category:
        # Filtere Events nach der gefundenen Kategorie
        events = Event.objects.filter(category=concert_category)
    else:
        # Keine Events, falls keine Kategorie gefunden wird
        events = Event.objects.none()

    # Die neuesten 6 Blog-Posts abrufen
    blog_content = BlogPost.objects.all()[0:6]
    # Den ersten Index-Text abrufen
    index_text = IndexText.objects.all().first()

    # Den aktiven Alert abrufen
    active_alert = Alert.objects.filter(is_active=True).first()  # Nur den ersten aktiven Alert anzeigen

    # Kontext erstellen, um ihn an das Template zu übergeben
    context = {
        'events': events,
        'blog_content': blog_content,
        'index_text': index_text,
        # Alert Mode
        'alert_message': active_alert.message if active_alert else None,
        'alert_title': active_alert.title if active_alert else None,
    }

    # Das Template mit dem übergebenen Kontext rendern
    return render(request, 'home/index.html', context)

def contact(request):
    return render(request, 'home/contact.html')

def prices(request):
    return render(request, 'home/prices.html')

def impressum(request):
    return render(request, 'home/impressum.html')

def about(request):
    return render(request, 'home/about.html')

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

def view_404(request, *args, **kwargs):
    return redirect('home_view')

def view_500(request, *args, **kwargs):
    return redirect('home_view')
