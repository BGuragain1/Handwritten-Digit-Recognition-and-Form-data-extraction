import cv2
import RegionOfInterest as rn

# Load the image
image = cv2.imread("Forms/Aligned_Image2_8bit.jpg")
image = cv2.resize(image, (650*2, 700*2))

# first_name = []
# last_name = []

def getFirstName():
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

# def getMiddleName():
# def getLastName():
# def getCitizenNo():
# def getEmail():
# def getIssuedDistrict():
# def getIssuedDate():
# def getNFirstName():
# def getNMiddleName():
# def getNLastName():
# def getNCitizenNo():
# def getSignature():
# def getFingerPrints():
# def getTempDistrict():
# def getTempVDC():
# def getTempHouseNo():
# def getTempWardNo():
# def getPermDistrict():
# def getPermVDC():
# def getPermHouseNo():
# def getPermWardNo():

# Process each ROI
for points in rn.ROI_CN:
    point1 = points[0]
    point2 = points[1]

    x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
    x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

    # Crop the rectangular region from the image
    cropped_image = image[y1:y2, x1:x2]
    cv2.imshow("Image",cropped_image)
    cv2.waitKey(0)

