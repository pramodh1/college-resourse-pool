from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages,auth

# Create your views here.
def login(request):
    if  request.method=='POST':
        username=request.POST['username']
        password=request.POST['password'] 
        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'logged in success')
            return redirect('home') 
        else:
            messages.warning(request,"invalid details")   
            return redirect('login') 




            

        
    return render(request,'accounts/login.html')
def logoutuser(request):
    logout(request)
    return redirect('home')
def register(request):
    if  request.method=='POST':
        username=request.POST['username']
        rollno=request.POST['rollnumber']
        email=request.POST['email']
        password=request.POST['password']
        confirmpass=request.POST['confirmpassword']

        if password==confirmpass:
            if  User.objects.filter(username=username).exists():
                messages.warning(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.warning(request,'email already exists')
                return redirect('register') 
            elif len(password)<7:
                messages.warning(request,'password length should be minimum 7 characters')
                return redirect('register')                      
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                messages.success(request,'Account created successfully')
                return redirect('login')      
        else:
            messages.warning(request,'password didnt matched')
            return redirect('register')
    return render(request,'accounts/register.html')

