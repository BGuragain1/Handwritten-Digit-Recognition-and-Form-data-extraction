import cv2
from Form_Detection import getTheBox as get

def createData(image,image_name):
    gb = get.getTheWords(image)
    data = {
        "personal_info": {
            "first_name": gb.getFirstName().lower(),
            "middle_name": gb.getMiddleName().lower(),
            "last_name": gb.getLastName().lower(),
            "citizenship_no": gb.getCitizenNo(),
            "email": gb.getEmail1().lower()+"@"+gb.getEmail2().lower(),
            "issued_district": gb.getIssuedDistrict().lower(),
            "issued_date": gb.getIssuedDate(),
            "phone_number" : gb.getPhoneNumber()
        },
        "nominee_info": {
            "first_name": gb.getNFirstName().lower(),
            "middle_name": gb.getNMiddleName().lower(),
            "last_name": gb.getNLastName().lower(),
            "citizenship_no": gb.getNCitizenNo()
        },
        "temporary_address": {
            "district": gb.getTempDistrict().lower(),
            "house_no": gb.getTempHouseNo(),
            "vdc": gb.getTempVDC().lower(),
            "ward_no": gb.getTempWardNo()
        },
        "permanent_address": {
            "district": gb.getPermDistrict().lower(),
            "house_no": gb.getPermHouseNo(),
            "vdc": gb.getPermVDC().lower(),
            "ward_no": gb.getPermWardNo()
        },
        "biometric_info": {
            gb.getSignature(image_name),gb.getFingerPrints(image_name)
        }
    }
    return data


def main():
    createData(cv2.imread("Forms/Aligned_Image1.jpg"))

if __name__ == "__main__":
    main()