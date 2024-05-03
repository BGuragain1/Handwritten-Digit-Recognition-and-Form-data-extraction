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
import json

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
    messages.success(request, 'Login Sucessfully')
    return render(request, "home.html")

@login_required
def addStudents(request):
    if request.method == "POST":
        id = request.user.id
        form_name = np.random.random()
        data = {
            'user_id': id,
            'form_name': form_name,
            'first_name': request.POST.get('firstName'),
            'middle_name': request.POST.get('middleName'),
            'last_name': request.POST.get('lastName'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phoneNumber'),
            'dob': request.POST.get('dob'),
            'gender': request.POST.get('gender'),
            'citizenship_number': request.POST.get('citizenshipNumber'),
            'course': request.POST.get('course'),
            'guardian': {
                'first_name': request.POST.get('guardianFirstName'),
                'middle_name': request.POST.get('guardianMiddleName'),
                'last_name': request.POST.get('guardianLastName'),
                'phone_number': request.POST.get('guardianPhoneNumber'),
                'relation': request.POST.get('relation')
            },
            'secondary_school': {
                'name': request.POST.get('secondarySchoolName'),
                'year_completion': request.POST.get('secondaryYearCompletion'),
                'cgpa': request.POST.get('secondaryCGPA'),
                'district': request.POST.get('secondaryDistrict')
            },
            'higher_secondary_school': {
                'name': request.POST.get('higherSecondarySchoolName'),
                'year_completion': request.POST.get('higherSecondaryYearCompletion'),
                'cgpa': request.POST.get('higherSecondaryCGPA'),
                'district': request.POST.get('higherSecondaryDistrict')
            },
            'permanent_address': {
                'province': request.POST.get('permanentProvince'),
                'district': request.POST.get('permanentDistrict'),
                'municipality': request.POST.get('permanentMunicipality'),
                'ward_no': request.POST.get('permanentWardNo'),
                'zip_code': request.POST.get('permanentZipCode')
            },
            'temporary_address': {
                'province': request.POST.get('temporaryProvince'),
                'district': request.POST.get('temporaryDistrict'),
                'municipality': request.POST.get('temporaryMunicipality'),
                'ward_no': request.POST.get('temporaryWardNo'),
                'zip_code': request.POST.get('temporaryZipCode')
            },
        }
        photo_file = request.FILES.get('photo')
        signature_file = request.FILES.get('signature')
        
        if photo_file:
            photo_directory = 'media/uploads/photo'
            with open(os.path.join(photo_directory, "P_"+str(form_name)), 'wb+') as destination:
                for chunk in photo_file.chunks():
                    destination.write(chunk)

        if signature_file:
            signature_directory = 'media/uploads/signature'
            with open(os.path.join(signature_directory, "S_"+str(form_name)), 'wb+') as destination:
                for chunk in signature_file.chunks():
                    destination.write(chunk)
        json_data = json.dumps(data)

        utils.insertData(json_data)
        messages.success(request, 'Student Added Successfully')
        return render(request,"home.html")
    
    return render(request,"student.html")

@login_required
def uploadForms(request):
    return render(request,"formPhoto.html")


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

    if "delete" in request.POST:
        id = request.POST.get("delete")
        utils.deleteClient(id)
        messages.success(request, 'Deleted Successfully')
    elif "edit" in request.POST:
        id = request.POST.get("edit")
        student = utils.getSpecified(id)
        return render(request,"edit.html",{"student":student})
    elif "update" in request.POST:
        id = request.POST.get("update")
        datas = {
            'first_name': request.POST.get('first_name'),
            'middle_name': request.POST.get('middle_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'dob': request.POST.get('date_of_birth'),
            'gender': request.POST.get('gender'),
            'citizenship_number': request.POST.get('citizenship_number'),
            'course': request.POST.get('course'),
            'guardian': {
                'first_name': request.POST.get('guardian_first_name'),
                'middle_name': request.POST.get('guardian_middle_name'),
                'last_name': request.POST.get('guardian_last_name'),
                'phone_number': request.POST.get('guardian_phone_number'),
                'relation': request.POST.get('relation_to_student')
            },
            'secondary_school': {
                'name': request.POST.get('secondary_school_name'),
                'year_completion': request.POST.get('secondary_year_completion'),
                'cgpa': request.POST.get('secondary_cgpa'),
                'district': request.POST.get('secondary_district')
            },
            'higher_secondary_school': {
                'name': request.POST.get('higher_secondary_school_name'),
                'year_completion': request.POST.get('higher_secondary_year_completion'),
                'cgpa': request.POST.get('higher_secondary_cgpa'),
                'district': request.POST.get('higher_secondary_district')
            },
            'permanent_address': {
                'province': request.POST.get('permanent_province'),
                'district': request.POST.get('permanent_district'),
                'municipality': request.POST.get('permanent_municipality'),
                'ward_no': request.POST.get('permanent_municipality'),
                'zip_code': request.POST.get('permanent_zip_code')
            },
            'temporary_address': {
                'province': request.POST.get('temporary_province'),
                'district': request.POST.get('temporary_district'),
                'municipality': request.POST.get('temporary_municipality'),
                'ward_no': request.POST.get('temporary_ward_no'),
                'zip_code': request.POST.get('temporary_zip_code')
            },
        }
        json_data = json.dumps(datas)
        utils.updateData(json_data,id)
        messages.success(request, 'Updated Successfully')
    return render(request,"search.html",{"students":data})

@login_required
def viewDetails(request):
    id = request.POST.get("detail")
    data = utils.getSpecified(id)
    return render(request,"details.html",{"student":data})