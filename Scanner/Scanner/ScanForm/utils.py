from ScanForm.models import StudentDetails
import os
from django.utils import timezone
import json
from django.db.models import Q


def insertData(data):
    parsed_data = json.loads(data)

    client_details = StudentDetails(
        user_id=parsed_data['user_id'],
        form_name=parsed_data['form_name'],
        first_name=parsed_data['first_name'],
        middle_name=parsed_data['middle_name'],
        last_name=parsed_data['last_name'],
        email=parsed_data['email'],
        phone_number=parsed_data['phone_number'],
        date_of_birth=parsed_data['dob'],
        gender=parsed_data['gender'],
        citizenship_number=parsed_data['citizenship_number'],
        course=parsed_data['course'],
        guardian_first_name=parsed_data['guardian']['first_name'],
        guardian_middle_name=parsed_data['guardian']['middle_name'],
        guardian_last_name=parsed_data['guardian']['last_name'],
        guardian_phone_number=parsed_data['guardian']['phone_number'],
        relation_to_student=parsed_data['guardian']['relation'],
        secondary_school_name=parsed_data['secondary_school']['name'],
        secondary_year_completion=parsed_data['secondary_school']['year_completion'],
        secondary_cgpa=parsed_data['secondary_school']['cgpa'],
        secondary_district=parsed_data['secondary_school']['district'],
        secondary_municipality=parsed_data['secondary_school']['municipality'],
        secondary_wardno=parsed_data['secondary_school']['ward_no'],
        higher_secondary_school_name=parsed_data['higher_secondary_school']['name'],
        higher_secondary_year_completion=parsed_data['higher_secondary_school']['year_completion'],
        higher_secondary_cgpa=parsed_data['higher_secondary_school']['cgpa'],
        higher_secondary_district=parsed_data['higher_secondary_school']['district'],
        higher_secondary_municipality=parsed_data['higher_secondary_school']['municipality'],
        higher_secondary_wardno=parsed_data['higher_secondary_school']['ward_no'],
        higher_secondary_faculty=parsed_data['higher_secondary_school']['faculty'],
        permanent_province=parsed_data['permanent_address']['province'],
        permanent_district=parsed_data['permanent_address']['district'],
        permanent_municipality=parsed_data['permanent_address']['municipality'],
        permanent_ward_no=parsed_data['permanent_address']['ward_no'],
        permanent_tole=parsed_data['permanent_address']['tole'],
        temporary_province=parsed_data['temporary_address']['province'],
        temporary_district=parsed_data['temporary_address']['district'],
        temporary_municipality=parsed_data['temporary_address']['municipality'],
        temporary_ward_no=parsed_data['temporary_address']['ward_no'],
        temporary_tole=parsed_data['temporary_address']['tole']
    )
    client_details.uploaded_time = timezone.now()
    client_details.save()
 
def insertFormData(data,form_name,id):
    
    client_details = StudentDetails(
        user_id=id,
        form_name=form_name,
        first_name=data['first_name'],
        middle_name=data['middle_name'],
        last_name=data['last_name'],
        email=data['email_1'],
        phone_number=data['phone_number'],
        date_of_birth=data['date_of_birth'],
        gender=data['gender'],
        citizenship_number=data['citizen_number'],
        course=data['course'],
        guardian_first_name=data['guardian_first_name'],
        guardian_middle_name=data['guardian_middle_name'],
        guardian_last_name=data['guardian_last_name'],
        guardian_phone_number=data['guardian_phone'],
        relation_to_student=data['relation'],
        secondary_school_name=data['school'],
        secondary_year_completion=data['graduation_year'],
        secondary_cgpa=data['cgpa'],
        secondary_district=data['district'],
        secondary_municipality=data['municipality'],
        secondary_wardno=data['ward'],
        higher_secondary_school_name=data['high_school'],
        higher_secondary_year_completion=data['high_school_graduation_year'],
        higher_secondary_cgpa=data['high_school_cgpa'],
        higher_secondary_district=data['high_school_district'],
        higher_secondary_municipality=data['high_school_municipality'],
        higher_secondary_faculty=data['high_school_faculty'],
        higher_secondary_wardno=data['high_school_ward'],
        permanent_province=data['permanent_province'],
        permanent_district=data['permanent_district'],
        permanent_municipality=data['permanent_municipality'],
        permanent_ward_no=data['permanent_ward'],
        permanent_tole=data['permanent_tole'],
        temporary_province=data['temporary_province'],
        temporary_district=data['temporary_district'],
        temporary_municipality=data['temporary_municipality'],
        temporary_ward_no=data['temporary_ward'],
        temporary_tole=data['temporary_tole'],
    )
    client_details.uploaded_time = timezone.now()
    client_details.save()
    
    return

def updateData(data, id):
    client = StudentDetails.objects.get(id=id)
    data = json.loads(data)
    
    client.first_name = data['first_name']
    client.middle_name = data['middle_name']
    client.last_name = data['last_name']
    client.email = data['email']
    client.phone_number = data['phone_number']
    client.date_of_birth = data['dob']
    client.gender = data['gender']
    client.citizenship_number = data['citizenship_number']
    client.course = data['course']

    # Guardian information
    client.guardian_first_name = data['guardian']['first_name']
    client.guardian_middle_name = data['guardian']['middle_name']
    client.guardian_last_name = data['guardian']['last_name']
    client.guardian_phone_number = data['guardian']['phone_number']
    client.relation_to_student = data['guardian']['relation']

    # Secondary school information
    client.secondary_school_name = data['secondary_school']['name']
    client.secondary_year_completion = data['secondary_school']['year_completion']
    client.secondary_cgpa = data['secondary_school']['cgpa']
    client.secondary_district = data['secondary_school']['district']
    client.secondary_municipality = data['secondary_school']['municipality']
    client.secondary_wardno = data['secondary_school']['ward_no']

    # Higher secondary school information
    client.higher_secondary_school_name = data['higher_secondary_school']['name']
    client.higher_secondary_year_completion = data['higher_secondary_school']['year_completion']
    client.higher_secondary_cgpa = data['higher_secondary_school']['cgpa']
    client.higher_secondary_faculty = data['higher_secondary_school']['faculty']
    client.higher_secondary_district = data['higher_secondary_school']['district']
    client.higher_secondary_municipality = data['higher_secondary_school']['municipality']
    client.higher_secondary_wardno = data['higher_secondary_school']['ward_no']

    # Permanent address information
    client.permanent_province = data['permanent_address']['province']
    client.permanent_district = data['permanent_address']['district']
    client.permanent_municipality = data['permanent_address']['municipality']
    client.permanent_ward_no = data['permanent_address']['ward_no']
    client.permanent_tole = data['permanent_address']['tole']

    # Temporary address information
    client.temporary_province = data['temporary_address']['province']
    client.temporary_district = data['temporary_address']['district']
    client.temporary_municipality = data['temporary_address']['municipality']
    client.temporary_ward_no = data['temporary_address']['ward_no']
    client.temporary_tole = data['temporary_address']['tole']

    client.save()
    return

def deleteClient(id):
    client = StudentDetails.objects.get(id=id)
    os.remove("media/uploads/signature/S_"+client.form_name+".jpg")
    os.remove("media/uploads/photo/P_"+client.form_name+".jpg")
    try:
        os.remove("media/uploads/form_pic/"+client.form_name+"_1.jpg")
        os.remove("media/uploads/form_pic/"+client.form_name+"_2.jpg")
    except FileNotFoundError:
        pass
    client.delete()
    return True  

# def deleteForm(name):
#     client = StudentDetails.objects.get(form_name=name)
#     os.remove("media/uploads/signature/S_"+name+".jpg")
#     os.remove("media/uploads/photo/P_"+name+".jpg")
#     try:
#         os.remove("media/uploads/form_pic/"+name+"_1.jpg")
#         os.remove("media/uploads/form_pic/"+name+"_2.jpg")
#     except FileNotFoundError:
#         pass
#     client.delete()
#     return True  

# def getForms(id_value):
#     form_list = StudentDetails.objects.filter(user_id=id_value,status="pending")
#     return form_list

# def getDetails(name):
#     form_list = StudentDetails.objects.get(form_name=name)
#     return form_list

def getAll():
    data = StudentDetails.objects.all().order_by('-uploaded_time')
    return data

def getSpecified(id):
    data = StudentDetails.objects.get(id = id)
    return data

def searchSpecificStudent(name):
    data = StudentDetails.objects.filter(Q(first_name__icontains=name))
    return data

# def approve(name):
#     client = StudentDetails.objects.get(form_name=name)
#     client.status = "approved"
#     client.save()
#     return