from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def startPage(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        myuser = User.objects.create(first_name = first_name, last_name = last_name , username = username, email = email, password = password1)
        
        myuser.save()
        messages.success(request, "Your account has been successfully created.")
        
        return redirect('login')
    
    return render(request,"signup.html")

def logout(request):
    return render(request,"index.html")

def homePage(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")
    
def feedback(request):
    return render(request,"feedback.html")

def base(request):
    return render(request, "base.html")