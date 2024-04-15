from ScanForm.models import ClientDetails
import os
from django.utils import timezone

def insertData(data,id,form_n):

    client = ClientDetails(
        user_id=id,
        form_name = form_n,
        first_name=data["first_name"],
        middle_name=data["middle_name"],
        last_name=data["last_name"],
        citizenship_no=data["citizenship_no"],
        email=data["email"],
        issued_district=data["issued_district"],
        issued_date=data["issued_date"],
        first_name_nominee=data["first_name_nominee"],
        middle_name_nominee=data["middle_name_nominee"],
        last_name_nominee=data["last_name_nominee"],
        citizenship_no_nominee=data["citizenship_no_nominee"],
        temp_district=data["temp_district"],
        temp_house_no=data["temp_house_no"],
        temp_vdc=data["temp_vdc"],
        temp_ward_no=data["temp_ward_no"],
        perm_district=data["perm_district"],
        perm_house_no=data["perm_house_no"],
        perm_vdc=data["perm_vdc"],
        perm_ward_no=data["perm_ward_no"],
        uploaded_date = timezone.now()
    )

    client.save()
 

def updateData(form_id,f_name,m_name,l_name,c_no,iss_date,email,iss_dis,n_f_name,n_m_name,n_l_name,
               n_c_no,t_d,t_h,t_vdc,t_wno,p_d,p_h,p_vdc,p_wno):
    client = ClientDetails.objects.get(id=form_id)

    client.first_name = f_name
    client.middle_name = m_name
    client.last_name = l_name
    client.citizenship_no = c_no
    client.issued_date = iss_date
    client.email = email
    client.issued_district = iss_dis

    client.first_name_nominee = n_f_name
    client.middle_name_nominee = n_m_name
    client.last_name_nominee = n_l_name
    client.citizenship_no_nominee = n_c_no

    client.temp_district = t_d
    client.temp_house_no = t_h
    client.temp_vdc = t_vdc
    client.temp_ward_no = t_wno

    client.perm_district = p_d
    client.perm_house_no = p_h
    client.perm_vdc = p_vdc
    client.perm_ward_no = p_wno
    client.save()
    return

def deleteClient(id):
    client = ClientDetails.objects.get(id=id)
    os.remove("media/uploads/form_pic/"+client.form_name)
    os.remove("media/uploads/signature/S1_"+client.form_name+'.jpg')
    os.remove("media/uploads/signature/S2_"+client.form_name+'.jpg')
    os.remove("media/uploads/fingerprints/FR_"+client.form_name+'.jpg')
    os.remove("media/uploads/fingerprints/FL_"+client.form_name+'.jpg')
    client.delete()
    return True  # Indicate successful deletion

def getForms(id_value):
    form_list = ClientDetails.objects.filter(user_id=id_value)
    return form_list

def getDetails(id):
    form_list = ClientDetails.objects.get(id=id)
    # print(form_list.form_name)
    return form_list
