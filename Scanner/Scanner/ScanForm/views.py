from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import os
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.crypto import get_random_string
from django.contrib.sites.shortcuts import get_current_site
from django.conf import settings
from binascii import Error as BinasciiError
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from Form_Detection import app
from . import utils
import numpy as np
import json
from django.contrib.auth import get_user_model
User = get_user_model()

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
            messages.success(request, 'Login Sucessfully')
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
                user.is_active = False
                user.save()
                send_verification_email(request, user)
                messages.success(request,"Sign Up Successfully.Please Check Your email for verification")
                return redirect("login")
        else:
            messages.info(request,"Passwords do not match")
            return redirect("signup")
    else:
        return render(request, "signup.html")
    
def send_verification_email(request, user):
    current_site = get_current_site(request)
    mail_subject = 'Activate your account.'
    token = get_random_string(20)
    user.verification_token = token
    user.save()
    
    verification_link = f"http://{current_site.domain}/activate_account/?uid={urlsafe_base64_encode(force_bytes(user.pk))}&token={token}"
    
    message = render_to_string('verification_email.html', {
        'user': user,
        'domain': current_site.domain,
        'verification_link': verification_link,
    })
    
    to_email = user.email
    send_mail(mail_subject, message, 'guragainbigyan123@gmail.com', [to_email],html_message=message)

def activate_account(request):
    uidb64 = request.GET.get('uid')
    token = request.GET.get('token')

    try:
        # Decoding uidb64 to get the user ID
        uid = urlsafe_base64_decode(uidb64)
        uid = uid.decode('utf-8')
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, BinasciiError):
        user = None

    if user is not None and user.verification_token == token:
        user.is_active = True
        user.verification_token = None
        user.save()
        messages.success(request, 'Your account has been activated successfully.')
        return redirect('login')
    else:
        messages.error(request, 'Activation link is invalid or expired.')
        return redirect('login')
    
def logout_view(request):
    logout(request)
    request.session.flush() 
    messages.success(request,"Logged Out Successfully") 
    return redirect('login')

@login_required
def homePage(request):
    if request.method == "POST":
        formz = PasswordChangeForm(user=request.user, data=request.POST)
        if formz.is_valid():
            user = formz.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('homePage')  
        else:
            if 'old_password' in formz.errors:
                messages.error(request, 'Old password is incorrect.')
                return redirect('settings')  
            elif 'new_password2' in formz.errors:
                messages.error(request, 'The new passwords do not match.')
                return redirect('settings')  
            else:
                messages.error(request, 'Please correct the error below.')
                return redirect('settings')  
           
    return render(request, "home.html")

@login_required
def settings(request):
    return render(request,"settings.html")

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
                'district': request.POST.get('SecondaryDistrict'),
                'municipality': request.POST.get('SecondaryMunicipality'),  
                'ward_no': request.POST.get('SecondaryWard')  
            },
            'higher_secondary_school': {
                'name': request.POST.get('higherSecondarySchoolName'),
                'year_completion': request.POST.get('higherSecondaryYearCompletion'),
                'cgpa': request.POST.get('higherSecondaryCGPA'),
                'faculty': request.POST.get('higherSecondaryfaculty'),
                'district': request.POST.get('higherSecondaryDistrict'),
                'municipality': request.POST.get('higherSecondaryMunicipality'),
                'ward_no': request.POST.get('higherSecondaryWard')
            },
            'permanent_address': {
                'province': request.POST.get('permanentProvince'),
                'district': request.POST.get('permanentDistrict'),
                'municipality': request.POST.get('permanentMunicipality'),
                'ward_no': request.POST.get('permanentWardNo'),
                'tole': request.POST.get('permanenttole')
            },
            'temporary_address': {
                'province': request.POST.get('temporaryProvince'),
                'district': request.POST.get('temporaryDistrict'),
                'municipality': request.POST.get('temporaryMunicipality'),
                'ward_no': request.POST.get('temporaryWardNo'),
                'tole': request.POST.get('temporary_tole')
            },
        }

        photo_file = request.FILES.get('photo')
        signature_file = request.FILES.get('signature')
        
        if photo_file:
            photo_directory = 'media/uploads/photo'
            with open(os.path.join(photo_directory, "P_"+str(form_name)+".jpg"), 'wb+') as destination:
                for chunk in photo_file.chunks():
                    destination.write(chunk)

        if signature_file:
            signature_directory = 'media/uploads/signature'
            with open(os.path.join(signature_directory, "S_"+str(form_name)+".jpg"), 'wb+') as destination:
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
    elif "search" in request.POST:
        name = request.POST.get("search")     
        if name!="":
            data = utils.searchSpecificStudent(name)
            if not data.exists():
                messages.error(request, 'No data Found')
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
                'year_completion': request.POST.get('secondaryYearCompletion'),
                'cgpa': request.POST.get('secondaryCGPA'),
                'district': request.POST.get('SecondaryDistrict'),
                'municipality': request.POST.get('SecondaryMunicipality'),
                'ward_no': request.POST.get('SecondaryWard')
            },
            'higher_secondary_school': {
                'name': request.POST.get('higher_secondary_school_name'),
                'year_completion': request.POST.get('higher_secondary_year_completion'),
                'cgpa': request.POST.get('higher_secondary_cgpa'),
                'faculty': request.POST.get('higherSecondaryfaculty'),
                'district': request.POST.get('higherSecondaryDistrict'),
                'municipality': request.POST.get('higherSecondaryMunicipality'),
                'ward_no': request.POST.get('higherSecondaryWard')
            },
            'permanent_address': {
                'province': request.POST.get('permanent_province'),
                'district': request.POST.get('permanent_district'),
                'municipality': request.POST.get('permanent_municipality'),
                'ward_no': request.POST.get('permanent_ward_no'),
                'tole': request.POST.get('permanenttole')
            },
            'temporary_address': {
                'province': request.POST.get('temporary_province'),
                'district': request.POST.get('temporary_district'),
                'municipality': request.POST.get('temporary_municipality'),
                'ward_no': request.POST.get('temporary_ward_no'),
                'tole': request.POST.get('temporary_tole')
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

@login_required
def about(request):
    return render(request,"about.html")

@login_required
def forms(request):
    if request.method == "POST":
        if 'form1' and 'form2' in request.FILES:
            image1 = request.FILES["form1"]
            image2 = request.FILES["form2"]
            image_name = np.random.rand()

            # media_root = settings.MEDIA_ROOT
            image_path1 = os.path.join("/home/bigyan1/Desktop/Scanner/Scanner/media/uploads/form_pic", f"{image_name}_1.jpg")
            image_path2 = os.path.join("/home/bigyan1/Desktop/Scanner/Scanner/media/uploads/form_pic", f"{image_name}_2.jpg")

            with open(image_path1, 'wb') as f1, open(image_path2, 'wb') as f2:
                for chunk1, chunk2 in zip(image1.chunks(), image2.chunks()):
                    f1.write(chunk1)
                    f2.write(chunk2)

            data = app.predict_from_form(image_path1, image_path2, str(image_name))   
            utils.insertFormData(data,image_name,request.user.id)        
            return redirect("searchDetails")
        
        # elif "save" in request.POST:
        #     return render(request,"uploadForm.html")
            
        # elif "cancel" in request.POST:
        #     utils.deleteForm(request.POST.get("cancel"))
        #     return render(request,"uploadForm.html")

        elif "delete" in request.POST:
            name = request.POST.get("delete")
            utils.deleteForm(name)
            return render(request,"home.html")
