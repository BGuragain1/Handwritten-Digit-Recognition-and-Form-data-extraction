import cv2
from Form_Detection import RegionOfInterest as rn
from Form_Detection import predictTheWords as pw
import numpy as np
import matplotlib.pyplot as plt

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
            if np.sum(cropped_image) < 250000:
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
            print(np.sum(cropped_image))
            if np.sum(cropped_image) < 250000:
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

    def getEmail(self):
        final_word = []
        point1 = rn.ROI_email_first[0][0]
        point2 = rn.ROI_email_first[0][1]
        points3 = rn.ROI_email_second[0][0]
        points4 = rn.ROI_email_second[0][1]

        x1, y1 = max(0, point1[0]), max(0, point1[1])
        x2, y2 = min(self.image.shape[1], point2[0]), min(self.image.shape[0], point2[1])

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        # Apply thresholding to create a binary image
        _, binary_image = cv2.threshold(cropped_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through each contour
        for contour in contours:
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y-1:y+h+1, x-1:x+w+1]
            word = pw.image_prediction(last_image)
            final_word.append(word)
            # Display the segmented characters
            # cv2.imshow('Segmented Characters', last_image)
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

    def getSignature(self):
        return

    def getFingerPrints(self):
        return

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

            x1, y1 = max(0, point1[0]), max(0, point1[1] )
            x2, y2 = min(self.image.shape[1], point2[0]), min(self.image.shape[0], point2[1])

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]
            word = pw.image_prediction(cropped_image)
            final_word.append(word)
            # cv2.imshow("Image",cropped_image)
            # cv2.waitKey(0)

        return ''.join(final_word)

    def getTempHouseNo(self):
        final_word = []
        point1 = rn.ROI_T_House_no[0][0]
        point2 = rn.ROI_T_House_no[0][1]

        x1, y1 = max(0, point1[0]), max(0, point1[1])
        x2, y2 = min(self.image.shape[1], point2[0]), min(self.image.shape[0], point2[1])

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        # Apply thresholding to create a binary image
        _, binary_image = cv2.threshold(cropped_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through each contour
        for contour in contours:
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y - 1:y + h + 1, x - 1:x + w + 1]
            word = pw.image_prediction(last_image)
            final_word.append(word)
            # Display the segmented characters
            # cv2.imshow('Segmented Characters', last_image)
            # cv2.waitKey(0)
        return ''.join(final_word)

    def getTempWardNo(self):
        final_word = []
        point1 = rn.ROI_T_Ward_no[0][0]
        point2 = rn.ROI_T_Ward_no[0][1]

        x1, y1 = max(0, point1[0]), max(0, point1[1])
        x2, y2 = min(self.image.shape[1], point2[0]), min(self.image.shape[0], point2[1])

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]
        plt.imshow(cropped_image)
        # Apply thresholding to create a binary image
        _, binary_image = cv2.threshold(cropped_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # contours = sort_contours(contours, method="left-to-right")[0]
        # Iterate through each contour
        for contour in contours:
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y + h, x:x + w]
            word = pw.image_prediction(last_image)
            final_word.append(word)
            # Display the segmented characters
            plt.imshow(last_image)
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
        point1 = rn.ROI_P_House_no[0][0]
        point2 = rn.ROI_P_House_no[0][1]

        x1, y1 = max(0, point1[0]), max(0, point1[1])
        x2, y2 = min(self.image.shape[1], point2[0]), min(self.image.shape[0], point2[1])

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        # Apply thresholding to create a binary image
        _, binary_image = cv2.threshold(cropped_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through each contour
        for contour in contours:
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y + h , x:x + w]
            word = pw.image_prediction(last_image)
            final_word.append(word)
            # Display the segmented characters
            # cv2.imshow('Segmented Characters', last_image)
            # cv2.waitKey(0)
        return ''.join(final_word)

    def getPermWardNo(self):
        final_word = []
        point1 = rn.ROI_P_Ward_no[0][0]
        point2 = rn.ROI_P_Ward_no[0][1]

        x1, y1 = max(0, point1[0]), max(0, point1[1])
        x2, y2 = min(self.image.shape[1], point2[0]), min(self.image.shape[0], point2[1])

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        # Apply thresholding to create a binary image
        _, binary_image = cv2.threshold(cropped_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Find contours in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate through each contour
        for contour in contours:
            # Get bounding box coordinates
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y + h, x:x + w]
            word = pw.image_prediction(last_image)
            final_word.append(word)
            # Display the segmented characters
            # cv2.imshow('Segmented Characters', last_image)
            # cv2.waitKey(0)
        return ''.join(final_word)

def main():
    image = cv2.imread("Forms/Aligned_Image1_8bit.jpg")
    getter = getTheWords(image)
    print(getter.getEmail())

if __name__ == "__main__":
    main()