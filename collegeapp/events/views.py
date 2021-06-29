from django.shortcuts import render
from .models import event1
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def events(request):
    events=event1.objects.all()
    data={
        'event':events,
    }
    return render(request,'events/events.html',data)