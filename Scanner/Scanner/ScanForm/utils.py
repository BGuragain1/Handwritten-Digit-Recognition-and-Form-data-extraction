from ScanForm.models import ClientDetails
import os
from django.utils import timezone
import json

def insertData(data):
    parsed_data = json.loads(data)

    client_details = ClientDetails(
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
        higher_secondary_school_name=parsed_data['higher_secondary_school']['name'],
        higher_secondary_year_completion=parsed_data['higher_secondary_school']['year_completion'],
        higher_secondary_cgpa=parsed_data['higher_secondary_school']['cgpa'],
        higher_secondary_district=parsed_data['higher_secondary_school']['district'],
        permanent_province=parsed_data['permanent_address']['province'],
        permanent_district=parsed_data['permanent_address']['district'],
        permanent_municipality=parsed_data['permanent_address']['municipality'],
        permanent_ward_no=parsed_data['permanent_address']['ward_no'],
        permanent_zip_code=parsed_data['permanent_address']['zip_code'],
        temporary_province=parsed_data['temporary_address']['province'],
        temporary_district=parsed_data['temporary_address']['district'],
        temporary_municipality=parsed_data['temporary_address']['municipality'],
        temporary_ward_no=parsed_data['temporary_address']['ward_no'],
        temporary_zip_code=parsed_data['temporary_address']['zip_code']
    )
    client_details.uploaded_time = timezone.now()
    client_details.save()
 

def updateData(data, id):
    client = ClientDetails.objects.get(id=id)
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

    # Higher secondary school information
    client.higher_secondary_school_name = data['higher_secondary_school']['name']
    client.higher_secondary_year_completion = data['higher_secondary_school']['year_completion']
    client.higher_secondary_cgpa = data['higher_secondary_school']['cgpa']
    client.higher_secondary_district = data['higher_secondary_school']['district']

    # Permanent address information
    client.permanent_province = data['permanent_address']['province']
    client.permanent_district = data['permanent_address']['district']
    client.permanent_municipality = data['permanent_address']['municipality']
    client.permanent_ward_no = data['permanent_address']['ward_no']
    client.permanent_zip_code = data['permanent_address']['zip_code']

    # Temporary address information
    client.temporary_province = data['temporary_address']['province']
    client.temporary_district = data['temporary_address']['district']
    client.temporary_municipality = data['temporary_address']['municipality']
    client.temporary_ward_no = data['temporary_address']['ward_no']
    client.temporary_zip_code = data['temporary_address']['zip_code']
    client.save()
    return

def deleteClient(id):
    client = ClientDetails.objects.get(id=id)
    os.remove("media/uploads/signature/S_"+client.form_name)
    os.remove("media/uploads/photo/P_"+client.form_name)
    client.delete()
    return True  

def deleteClient_name(name):
    client = ClientDetails.objects.get(form_name=name)
    os.remove("media/uploads/form_pic/"+client.form_name)
    os.remove("media/uploads/signature/S1_"+client.form_name+'.jpg')
    os.remove("media/uploads/signature/S2_"+client.form_name+'.jpg')
    os.remove("media/uploads/fingerprints/FR_"+client.form_name+'.jpg')
    os.remove("media/uploads/fingerprints/FL_"+client.form_name+'.jpg')
    client.delete()
    return True 

def getForms(id_value):
    form_list = ClientDetails.objects.filter(user_id=id_value,status="pending")
    return form_list

def getDetails(name):
    form_list = ClientDetails.objects.get(form_name=name)
    return form_list

def getAll():
    data = ClientDetails.objects.all()
    return data

def getSpecified(id):
    data = ClientDetails.objects.get(id = id)
    return data

def approve(name):
    client = ClientDetails.objects.get(form_name=name)
    client.status = "approved"
    client.save()
    return