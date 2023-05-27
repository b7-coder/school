from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    events = Events.objects.all()
    mentors = Mentors.objects.all()
    courses = Courses.objects.all()
    
    context = {
        'events': events,
        'mentors' : mentors,
        'courses': courses
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {}
    return render(request , 'main/about.html', context)

def services(request):
    context = {}
    return render(request , 'main/services.html', context)

def blog(request):
    images = Gallery.objects.all()
    news = News.objects.all()
    context = {
        'images':images,
        'news': news
    }
    return render(request , 'main/blog.html', context)

def news(request, id):
    obj = News.objects.get(id=id)
    context = {
        'news' : obj,
    }
    if request.method == 'POST':
        return render(request , 'main/news.html', context)
    return redirect('index')
