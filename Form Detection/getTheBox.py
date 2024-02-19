import cv2
import RegionOfInterest as rn
import predictTheWords as pw
# Load the image
image = cv2.imread("Forms/Aligned_Image2_8bit.jpg")
image = cv2.resize(image, (650*2, 700*2))
def getFirstName():
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getMiddleName():
    for points in rn.ROI_middle_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getLastName():
    for points in rn.ROI_last_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getCitizenNo():
    for points in rn.ROI_CN:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getEmail():
    for points in rn.ROI_email_first:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

    for points in rn.ROI_email_second:
            point1 = points[0]
            point2 = points[1]

            x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
            x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

            # Crop the rectangular region from the image
            cropped_image = image[y1:y2, x1:x2]
            pw.image_prediction(cropped_image)
            cv2.imshow("Image", cropped_image)
            cv2.waitKey(0)

def getIssuedDistrict():
    for points in rn.ROI_CN_District:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getIssuedDate():
    for points in rn.ROI_CN_date:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getNFirstName():
    for points in rn.ROI_N_firstname:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getNMiddleName():
    for points in rn.ROI_N_middlename:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getNLastName():
    for points in rn.ROI_N_lastname:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getNCitizenNo():
    for points in rn.ROI_N_CN:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getSignature():
    for points in rn.ROI_signature_first:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getFingerPrints():
    for points in rn.ROI_fingerprint_left:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getTempDistrict():
    for points in rn.ROI_T_District:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getTempVDC():
    for points in rn.ROI_T_Municipality:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getTempHouseNo():
    for points in rn.ROI_T_House_no:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getTempWardNo():
    for points in rn.ROI_T_Ward_no:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getPermDistrict():
    for points in rn.ROI_P_District:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getPermVDC():
    for points in rn.ROI_P_Municipality:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getPermHouseNo():
    for points in rn.ROI_P_House_no:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)

def getPermWardNo():
    for points in rn.ROI_P_Ward_no:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 4), max(0, point1[1] + 4)
        x2, y2 = min(image.shape[1], point2[0] - 4), min(image.shape[0], point2[1] - 4)

        # Crop the rectangular region from the image
        cropped_image = image[y1:y2, x1:x2]
        pw.image_prediction(cropped_image)
        cv2.imshow("Image",cropped_image)
        cv2.waitKey(0)


