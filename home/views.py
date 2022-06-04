from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request, 'home/index.html')

def contact (request):
    return render (request, 'home/contact.html')

def program (request):
    return render (request, 'home/program.html')

def about (request):
    return render (request, 'home/about.html')