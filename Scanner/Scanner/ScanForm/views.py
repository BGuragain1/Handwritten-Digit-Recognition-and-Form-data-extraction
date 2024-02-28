from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import os
import requests
from django.conf import settings

# Create your views here.
def startPage(request):
    return render(request,"index.html")

def Login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
          # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect("homePage")
        else:
            return render(request,"login.html")
            
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

# @login_required
def homePage(request):
    user = request.user
    
    userInfo = {
        "username" : user.username,
        "first_name": user.first_name,
    }
    return render(request,"home.html",{"userInfo":userInfo})

def form(request):
    if request.method == "POST":
        # Check if a file was uploaded
        if 'imageUpload' in request.FILES:
            image = request.FILES["imageUpload"]
            # Save the uploaded image to the 'media' folder
            file_path = os.path.join(settings.MEDIA_ROOT, image.name)
            with open(file_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)
            print(image.name)
            return render(request, "form.html", {'image_path': image.name})
        else:
            # Handle the case where no file was uploaded
            return render(request, "form.html", {'error_message': 'No file was uploaded'})

    return render(request, "form.html")


def process(request):
    response = requests.get('http://localhost:8000/process')
    message = response.json().get('message')
    return render(request,"processess.html",{"message":message})