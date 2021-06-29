from django.shortcuts import render
from .models import youtuber
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def youtubers(request):
    youtubers=youtuber.objects.order_by('-createddate')
    data={
   'youtuber':youtubers
    }
    return render(request,'youtubers/youtubers.html',data)

def tubersdetails(request,id):
    tuber=get_object_or_404(youtuber,pk=id)
    data={
        'tuber':tuber
    }
    return render(request, 'youtubers/tuberdetails.html',data)
@login_required(login_url='login')
def search(request):
    tuber=youtuber.objects.order_by('-createddate')

    namesearch=youtuber.objects.values_list('name',flat=True).distinct()

    if 'keyword' in request.GET:
        keyword=request.GET['keyword']
        if keyword:
            tuber=tuber.filter(description__icontains=keyword)
    if 'name' in request.GET:
        name=request.GET['name']
        if name:
            tuber=tuber.filter(name__iexact=name)        
            
    data={'tuber':tuber,
           'namesearch':namesearch 
        }

    return render(request, 'youtubers/search.html',data)