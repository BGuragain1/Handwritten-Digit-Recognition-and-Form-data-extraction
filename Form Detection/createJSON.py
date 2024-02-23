from getTheBox import getTheWords
import json

def createJSON(image):
    gb = getTheWords(image)

    data = {
        "personal_info": {
            "first_name": gb.getFirstName(),
            "middle_name": gb.getMiddleName(),
            "last_name": gb.getLastName(),
            "citizenship_no": gb.getCitizenNo(),
            "email": gb.getEmail(),
            "issued_district": gb.getIssuedDistrict(),
            "issued_date": gb.getIssuedDate()
        },
        "nominee_info": {
            "first_name": gb.getNFirstName(),
            "middle_name": gb.getNMiddleName(),
            "last_name": gb.getNLastName(),
            "citizenship_no": gb.getNCitizenNo()
        },
        "temporary_address": {
            "district": gb.getTempDistrict(),
            "house_no": gb.getTempHouseNo(),
            "vdc": gb.getTempVDC(),
            "ward_no": gb.getTempWardNo()
        },
        "permanent_address": {
            "district": gb.getPermDistrict(),
            "house_no": gb.getPermHouseNo(),
            "vdc": gb.getPermVDC(),
            "ward_no": gb.getPermWardNo()
        },
        "biometric_info": {
            "signature": gb.getSignature(),
            # "left_thumb": left_thumb,
            # "right_thumb": right_thumb
        }
    }

    # Convert data to JSON format
    json_data = json.dumps(data, indent=4)
    return json_data
