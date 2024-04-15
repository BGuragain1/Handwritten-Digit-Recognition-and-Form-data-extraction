import cv2
from Form_Detection import getTheBox as get

def createData(image,image_name):
    gb = get.getTheWords(image)
    data = {
        "first_name": gb.getFirstName().lower(),
        "middle_name": gb.getMiddleName().lower(),
        "last_name": gb.getLastName().lower(),
        "citizenship_no": gb.getCitizenNo(),
        "email": gb.getEmail1().lower()+"@"+gb.getEmail2().lower(),
        "issued_district": gb.getIssuedDistrict().lower(),
        "issued_date": gb.getIssuedDate(),
        "phone_number" : gb.getPhoneNumber(),

        "first_name_nominee": gb.getNFirstName().lower(),
        "middle_name_nominee": gb.getNMiddleName().lower(),
        "last_name_nominee": gb.getNLastName().lower(),
        "citizenship_no_nominee": gb.getNCitizenNo(),

        "temp_district": gb.getTempDistrict().lower(),
        "temp_house_no": gb.getTempHouseNo(),
        "temp_vdc": gb.getTempVDC().lower(),
        "temp_ward_no": gb.getTempWardNo(),

        "perm_district": gb.getPermDistrict().lower(),
        "perm_house_no": gb.getPermHouseNo(),
        "perm_vdc": gb.getPermVDC().lower(),
        "perm_ward_no": gb.getPermWardNo(),

        "signature":gb.getSignature(image_name),
        "fingerprint":gb.getFingerPrints(image_name)
        }
    return data


def main():
    createData(cv2.imread("Forms/Aligned_Image1.jpg"))

if __name__ == "__main__":
    main()