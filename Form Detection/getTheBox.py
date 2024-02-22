import cv2
import RegionOfInterest as rn
import predictTheWords as pw

# # Load the image
# image = cv2.imread("Forms/Aligned_Image2_8bit.jpg")
# image = cv2.resize(image, (650*2, 700*2))

class getTheWords():

    def __init__(self,image):
        self.image = image
        self.image = cv2.resize(self.image, (650 * 2, 700 * 2))

    def getFirstName(self):
        final_word = []
        for points in rn.ROI_first_name:
            point1 = points[0]
            point2 = points[1]

            x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
            x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]
            word = pw.image_prediction(cropped_image)
            final_word.append(word)
            # cv2.imshow("Image",cropped_image)
            # cv2.waitKey(0)

        return ''.join(final_word)

def getMiddleName(self):
    final_word = []
    for points in rn.ROI_middle_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)
#
def getLastName(self):
    final_word = []
    for points in rn.ROI_last_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)
#
def getCitizenNo(self):
    final_word = []
    for points in rn.ROI_CN:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)
#
def getEmail(self):
    final_word = []
    for points in rn.ROI_email_first:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getIssuedDistrict(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getIssuedDate(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getNFirstName(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getNMiddleName(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getNLastName(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getNCitizenNo(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

# def getSignature(self):
#
#
# def getFingerPrints(self):


def getTempDistrict(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getTempVDC(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getTempHouseNo(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getTempWardNo(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getPermDistrict(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)
def getPermVDC(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getPermHouseNo(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)

def getPermWardNo(self):
    final_word = []
    for points in rn.ROI_first_name:
        point1 = points[0]
        point2 = points[1]

        x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
        x2, y2 = min(self.image.shape[1], point2[0] - 5), min(self.image.shape[0], point2[1] - 5)

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        word = pw.image_prediction(cropped_image)
        final_word.append(word)
        # cv2.imshow("Image",cropped_image)
        # cv2.waitKey(0)

    return ''.join(final_word)


