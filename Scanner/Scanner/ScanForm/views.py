from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import os
from django.conf import settings
from Form_Detection import app
from . import utils
import numpy as np

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
            messages.error(request,"Invalid Username or Password")
            
    return render(request,"login.html")

def signup(request):
    if request.method == 'POST':
        username1 = request.POST.get("username")
        email1= request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 == password2:
            if User.objects.filter(email = email1).exists():
                messages.info(request,"Email already exists")
                return redirect("signup")
            elif User.objects.filter(username = username1).exists():
                messages.info(request,"Username already exists")
                return redirect("signup")
            else:
                user = User.objects.create_user(username= username1,email=email1,first_name = first_name, last_name = last_name,
                                                password=password1)
                user.save()
                messages.info(request,"Sign Up Successfully")
                return redirect("login")
        else:
            messages.info(request,"Passwords do not match")
            return redirect("signup")
    else:
        return render(request, "signup.html")

def logout_view(request):
    logout(request)
    request.session.flush()  
    return redirect('login')

@login_required
def homePage(request):
    user_id = request.user.id
    forms = utils.getForms(user_id)
    if request.method=="POST":
        if "delete" in request.POST:
            form_id = request.POST.get('delete')
            utils.deleteClient(form_id)
        elif "approve" in request.POST:
            form_name = request.POST.get('approve')
            utils.approve(form_name)
    return render(request, "home.html", {"forms": forms})

@login_required
def editForm(request):
    if request.method == "POST":
        if "edit" in request.POST:
            form_name = request.POST.get("edit")
            data = utils.getDetails(form_name)
            return render(request, "edit.html", {"data": data, "id":form_name,"image_path": "media/uploads/form_pic/" + str(form_name)})
        
        elif "submit" in request.POST:
            form_id = request.POST.get('submit')
            utils.updateData(form_id,request.POST.get("first_name"),
                             request.POST.get("middle_name"),
                             request.POST.get("last_name"),
                             request.POST.get("citizenship_no"),
                             request.POST.get("issued_date"),
                             request.POST.get("email"),
                             request.POST.get("phone_number"),
                             request.POST.get("issued_district"),
                             request.POST.get("nominee_first_name"),
                             request.POST.get("nominee_middle_name"),
                             request.POST.get("nominee_last_name"),
                             request.POST.get("nominee_citizenship_no"),
                             request.POST.get("temp_district"),
                             request.POST.get("temp_house_no"),
                             request.POST.get("temp_vdc"),
                             request.POST.get("temp_ward_no"),   
                             request.POST.get("perm_district"),
                             request.POST.get("perm_house_no"),
                             request.POST.get("perm_vdc"),
                             request.POST.get("perm_ward_no"),                          
                             )
    return redirect("homePage")

@login_required
def details(request):
    if request.method == "POST":
        user_id = request.user.id
        # Check if a file was uploaded
        if 'imageUpload' in request.FILES:
            image = request.FILES["imageUpload"] 
            image_name = np.random.rand()
            file_path = os.path.join(settings.MEDIA_ROOT, str(image_name))
            with open(file_path, 'wb') as f:
                for chunk in image.chunks():
                    f.write(chunk)  

            data = app.predict_from_form(file_path,image_name)
            utils.insertData(data,user_id,image_name)
            return render(request, "form.html", {'image_path': "../media/uploads/form_pic/"+str(image_name),'image_name':image_name,'data':data})

        elif "cancel" in request.POST:
            form_name = request.POST.get('cancel')
            utils.deleteClient_name(form_name)
            return redirect('homePage')

        elif "save" in request.POST:
            form_name = request.POST.get('save')
            utils.updateData(form_name,request.POST.get("first_name"),
                             request.POST.get("middle_name"),
                             request.POST.get("last_name"),
                             request.POST.get("citizenship_no"),
                             request.POST.get("issued_date"),
                             request.POST.get("email"),
                             request.POST.get("phone_number"),
                             request.POST.get("issued_district"),
                             request.POST.get("nominee_first_name"),
                             request.POST.get("nominee_middle_name"),
                             request.POST.get("nominee_last_name"),
                             request.POST.get("nominee_citizenship_no"),
                             request.POST.get("temp_district"),
                             request.POST.get("temp_house_no"),
                             request.POST.get("temp_vdc"),
                             request.POST.get("temp_ward_no"),   
                             request.POST.get("perm_district"),
                             request.POST.get("perm_house_no"),
                             request.POST.get("perm_vdc"),
                             request.POST.get("perm_ward_no"),                          
                             )
            return redirect('homePage')

@login_required
def searchDetails(request):
    data = utils.getAll()
    if request.method == "POST":
        if "delete" in request.POST:
            name = request.POST.get("delete")
            utils.deleteClient_name(name)
    return render(request,"search.html",{"datas":data})

