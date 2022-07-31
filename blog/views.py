from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse

from blog.models import BlogPost
from blog.forms import ArticleForm

from home.slug import create_slug_text

# Create your views here.

def blog_summary(request):
    all_blogs = BlogPost.objects.all()
    context = {
        'all_blogs': all_blogs
        }
    return render(request, "blog/summary.html", context)

def youtube_id(url):
    o = urlparse(url)
    if o.netloc == 'youtu.be':
        return o.path[1:]
    elif o.netloc in ('www.youtube.com', 'youtube.com'):
        if o.path == '/watch':
            id_index = o.query.index('v=')
            return o.query[id_index+2:id_index+13]
        elif o.path[:7] == '/embed/':
            return o.path.split('/')[2]
        elif o.path[:3] == '/v/':
            return o.path.split('/')[2]
    return None  # fail?

def check_youtube_link(content):
    if content.find('>https://www.youtube'):
        first_position = content.find('>https://www.youtube') + 1
        last_postion = content.find('</a>', first_position)
        url = content[first_position:last_postion]
        return youtube_id(url)
    else:
        return False

@login_required(login_url='/team/login/')
def blog_thanks(request):
    return render(request, "blog/form_thanks.html")

@login_required(login_url='/team/login/')
def show_blogs_editing(request):
    all_blogs = BlogPost.objects.all().order_by("date").reverse()
    context = {
        'all_blogs': all_blogs
        }
    return render(request, "blog/edit/show_blog_editing.html", context)

@login_required(login_url='/team/login/')
def create_blog(request):
    form = ArticleForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArticleForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            blog = form.save(commit=False)
            blog.slug = create_slug_text(request.POST['title'])
            blog.save()
            return redirect('blog_thanks')
        else:
            form = ArticleForm(request.POST)
    context = {
        'form': form
        }
    return render(request, "blog/edit/form.html", context)

class BlogPostView(View):
    def get(self, request, *args, **kwargs):
        blog_post = get_object_or_404(BlogPost, slug=kwargs['slug'], published_year=kwargs['published_year'])
        youtube = check_youtube_link(blog_post.content.html)
        if youtube:
            context = {'blog_post': blog_post, 'youtube':youtube}
        else:
            context = {'blog_post': blog_post}
        return render(request, 'blog/blog_post.html', context)

@login_required(login_url='/intern/login/')
def blog_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
        return redirect('show_blogs_editing')
    else:
        form = ArticleForm(instance=post)
    return render(request, 'blog/edit/form.html', {'form': form})
