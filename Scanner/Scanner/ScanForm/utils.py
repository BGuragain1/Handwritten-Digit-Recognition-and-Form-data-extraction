from ScanForm.models import ClientDetails
import os

def insertData(data,id,form_n):
    
    personal = data["personal_info"]
    nominee = data["nominee_info"]
    temp = data["temporary_address"]
    perm = data["permanent_address"]

    client = ClientDetails(
        user_id=id,
        form_name = form_n,
        first_name=personal["first_name"],
        middle_name=personal["middle_name"],
        last_name=personal["last_name"],
        citizenship_no=personal["citizenship_no"],
        email=personal["email"],
        issued_district=personal["issued_district"],
        issued_date=personal["issued_date"],
        first_name_nominee=nominee["first_name"],
        middle_name_nominee=nominee["middle_name"],
        last_name_nominee=nominee["last_name"],
        citizenship_no_nominee=nominee["citizenship_no"],
        temp_district=temp["district"],
        temp_house_no=temp["house_no"],
        temp_vdc=temp["vdc"],
        temp_ward_no=temp["ward_no"],
        perm_district=perm["district"],
        perm_house_no=perm["house_no"],
        perm_vdc=perm["vdc"],
        perm_ward_no=perm["ward_no"]
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
