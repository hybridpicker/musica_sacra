from django.shortcuts import render, redirect
from events.models import Event, EventCategory
from blog.models import BlogPost
from home.models import IndexText
from home.forms import IndexTextForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

def home(request):
    try:
        # Attempt to find the "Konzert" category
        concert_category = EventCategory.objects.get(name="Konzert")
    except EventCategory.DoesNotExist:
        # If it does not exist, use the first available category
        concert_category = EventCategory.objects.first()

    if concert_category:
        # Filter events by the found category
        events = Event.objects.filter(category=concert_category)
    else:
        # No events if no category is found
        events = Event.objects.none()

    # Fetch the latest 6 blog posts
    blog_content = BlogPost.objects.all()[0:6]
    # Fetch the first instance of index text
    index_text = IndexText.objects.all().first()
    
    # Create the context to pass to the template
    context = {
        'events': events,
        'blog_content': blog_content,
        'index_text': index_text,
    }
    
    # Render the template with the given context
    return render(request, 'home/index.html', context)

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

def view_404(request, *args, **kwargs):
    return redirect('home_view')

def view_500(request, *args, **kwargs):
    return redirect('home_view')