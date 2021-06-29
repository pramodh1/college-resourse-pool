from django.shortcuts import render,redirect
from .models import contactus,postsub1
from django.contrib import messages,auth




def contact1(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        designation=request.POST['designation']
        subject=request.POST['subject']
        details=request.POST['details']
        contact=contactus(fullname=fullname,phonenumber=phonenumber,email=email,designation=designation,subject=subject,details=details)
        contact.save()
        messages.success(request,'message sent')
        return redirect('home')
    return render(request,'webpages/contact.html')
def postsub(request):
    if request.method=='POST':
        fullname=request.POST['fullname']
        branch=request.POST['branch']
        topic=request.POST['topic']
        subject1=request.POST['subject1']
        details=request.POST['details']
        dash=postsub1(fullname=fullname,topic=topic,branch=branch,subject1=subject1,details=details)
        dash.save()
        messages.success(request,'message posted')
        return redirect('home')
    return render(request,'post/dashboard.html')
def dashboard(request):

    postc=postsub1.objects.all()
    data={
        'post1':postc,
    }
    return render(request,'post/dashboard.html',data)




