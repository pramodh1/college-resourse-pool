from django.shortcuts import render
from .models import slide,team
from webapp1.models import youtuber
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    slider=slide.objects.all()
    teams=team.objects.all()
    flessons=youtuber.objects.filter(important=True)
    alllessons=youtuber.objects.all()
    data={
        'slider': slider,
        'teams':teams,
        'flessons':flessons,
        'alllessons':alllessons
    }
    return render(request,'webpages/home.html',data)
def post(request):
    return render(request,'post/post.html')
def about(request):
    return render(request,'webpages/about.html')

def services(request):
    return render(request,'webpages/services.html')

def contact(request):
    return render(request,'webpages/contact.html')
def daa(request):
    return render(request,'courses/daa.html')
def unix(request):
    return render(request,'courses/unix.html')
def python(request):
    return render(request,'courses/python.html')
def java(request):
    return render(request,'courses/java.html')    
def development(request):
    return render(request,'courses/development.html') 
def coding(request):
    return render(request,'courses/coding.html')  
def interview(request):
    return render(request,'courses/interview.html')            
