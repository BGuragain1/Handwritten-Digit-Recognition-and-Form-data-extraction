import cv2
from Form_Detection import getTheBox as get


def createData(image1, image2, image_name):
    gb1 = get.getTheWords1(image1)
    gb2 = get.getTheWords2(image2)

    data = {
        'first_name': gb1.getFirstName().capitalize(),
        'middle_name': gb1.getMiddleName().capitalize(),
        'last_name': gb1.getLastName().capitalize(),
        'citizen_number': gb1.getCitizenno(),
        'phone_number': gb1.getPhoneNumber(),
        'email_1': gb1.getEmail1().lower()+"@"+gb1.getEmail2().lower(),
        'date_of_birth': gb1.getDOB(),
        'gender': gb1.getGender(),
        'course': gb1.getcourse(),
        'temporary_province': gb1.gettempProvince().capitalize(),
        'temporary_district': gb1.gettempDistrict().capitalize(),
        'temporary_municipality': gb1.gettempMunici().capitalize(),
        'temporary_ward': gb1.gettempWard(),
        'temporary_tole': gb1.gettempTole().capitalize(),
        'permanent_province': gb1.getpermProvince().capitalize(),
        'permanent_district': gb1.getpermDistrict().capitalize(),
        'permanent_municipality': gb1.getpermMunici().capitalize(),
        'permanent_ward': gb1.getpermWard(),
        'permanent_tole': gb1.getpermTole().capitalize(),
        'guardian_first_name': gb2.getGfirstname().capitalize(),
        'guardian_middle_name': gb2.getGmiddlename().capitalize(),
        'guardian_last_name': gb2.getGlastname().capitalize(),
        'guardian_phone': gb2.getGphone(),
        'relation': gb2.getRelation().capitalize(),
        'school': gb2.getSschool().capitalize(),
        'graduation_year': gb2.getSGraduation().capitalize(),
        'municipality': gb2.getSmuni().capitalize(),
        'cgpa': gb2.getSCGPA(),
        'district': gb2.getSDistrict().capitalize(),
        'ward': gb2.getSward(),
        'high_school': gb2.getHGschool().capitalize(),
        'high_school_graduation_year': gb2.getHSGraduation(),
        'high_school_municipality': gb2.getHSMuni().capitalize(),
        'high_school_cgpa': gb2.getHSCGPA(),
        'high_school_district': gb2.getHSDistrict().capitalize(),
        'high_school_ward': gb2.getHSWard(),
        'high_school_faculty':gb2.HFaculty().capitalize()
    }
    gb1.savePhoto(image_name),
    gb2.saveSignature(image_name)

    return data

def main():
    image1 = cv2.imread("Forms/output1.jpg")
    image2 = cv2.imread("Forms/output2.jpg")
    image_name = "example" 
    data = createData(image1, image2, image_name)
    print(data)

if __name__ == "__main__":
    main()
