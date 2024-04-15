import cv2
from Form_Detection import RegionOfInterest as rn
from Form_Detection import predictTheWords as pw
import numpy as np
import matplotlib.pyplot as plt

class getTheWords():

    def __init__(self,image):
        self.image = image
        self.image = cv2.resize(self.image, (1000 * 2, 1500 * 2))
    
    def getFirstName(self):
        final_word = []
        for points in rn.ROI_first_name:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # # print(np.sum(final_image))
            if np.sum(final_image) > 1000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)

    def getMiddleName(self):
        final_word = []
        for points in rn.ROI_middle_name:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # # print(np.sum(final_image))
            if np.sum(final_image) > 1000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getLastName(self):
        final_word = []
        for points in rn.ROI_last_name:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # # print(np.sum(final_image))
            if np.sum(final_image) > 1000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getCitizenNo(self):
        final_word = []
        for points in rn.ROI_CN:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # # print(np.sum(final_image))
            if np.sum(final_image) > 1000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getEmail1(self):
        final_word = []
        point1 = rn.ROI_email_first[0][0]
        point2 = rn.ROI_email_first[0][1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)
    
    def getEmail2(self):
        final_word = []
        point1 = rn.ROI_email_second[0][0]
        point2 = rn.ROI_email_second[0][1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)

        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)

    def getPhoneNumber(self):
        final_word = []
        for points in rn.ROI_phone:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # # print(np.sum(final_image))
            if np.sum(final_image) > 10000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)
    
    def getIssuedDistrict(self):
        final_word = []
        point1 = rn.ROI_CN_District[0][0]
        point2 = rn.ROI_CN_District[0][1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)

    def getIssuedDate(self):
        final_word = []
        for points in rn.ROI_CN_date:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # print(np.sum(final_image))
            if np.sum(final_image) > 10000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getNFirstName(self):
        final_word = []
        for points in rn.ROI_N_firstname:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # print(np.sum(final_image))
            if np.sum(final_image) > 10000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getNMiddleName(self):
        final_word = []
        for points in rn.ROI_N_middlename:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # print(np.sum(final_image))
            if np.sum(final_image) > 5000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getNLastName(self):
        final_word = []
        for points in rn.ROI_N_lastname:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # # print(np.sum(final_image))
            if np.sum(final_image) > 10000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getNCitizenNo(self):
        final_word = []
        for points in rn.ROI_N_CN:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)

            # plt.imshow(final_image,cmap="gray")
            # plt.show()

            # print(np.sum(final_image))
            if np.sum(final_image) > 10000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getSignature(self,image_name):
        point1 = rn.ROI_signature_first[0]
        point2 = rn.ROI_signature_first[1]
        
        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        point3 = rn.ROI_signature_second[0]
        point4 = rn.ROI_signature_second[1]
        
        x3, y3 = point3[0],point3[1]
        x4, y4 = point4[0],point4[1]

        cropped_image_first = self.image[y1:y2, x1:x2]
        cropped_image_second = self.image[y3:y4, x3:x4]
        cv2.imwrite('media/uploads/signature/S1_'+str(image_name)+ '.jpg', cropped_image_first)
        cv2.imwrite('media/uploads/signature/S2_'+str(image_name)+ '.jpg', cropped_image_second)

        return

    def getFingerPrints(self,image_name):
        point1 = rn.ROI_fingerprint_left[0]
        point2 = rn.ROI_fingerprint_left[1]
        
        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        point3 = rn.ROI_fingerprint_right[0]
        point4 = rn.ROI_fingerprint_right[1]
        
        x3, y3 = point3[0],point3[1]
        x4, y4 = point4[0],point4[1]

        cropped_image_left = self.image[y1:y2, x1:x2]
        cropped_image_right = self.image[y3:y4, x3:x4]

        cv2.imwrite('media/uploads/fingerprints/FL_'+str(image_name)+ '.jpg', cropped_image_left)
        cv2.imwrite('media/uploads/fingerprints/FR_'+str(image_name)+ '.jpg', cropped_image_right)
        return

    def getTempDistrict(self):
        final_word = []
        point1 = rn.ROI_T_District[0]
        point2 = rn.ROI_T_District[1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)

    def getTempVDC(self):
        final_word = []
        point1 = rn.ROI_T_Municipality[0]
        point2 = rn.ROI_T_Municipality[1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)
    
    def getTempHouseNo(self):
        final_word = []
        point1 = rn.ROI_T_House_no[0]
        point2 = rn.ROI_T_House_no[1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)

    def getTempWardNo(self):
        final_word = []
        point1 = rn.ROI_T_Ward_no[0]
        point2 = rn.ROI_T_Ward_no[1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)
     
    def getPermDistrict(self):
        final_word = []
        point1 = rn.ROI_P_District[0]
        point2 = rn.ROI_P_District[1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)


    def getPermVDC(self):
        final_word = []
        point1 = rn.ROI_P_Municipality[0]
        point2 = rn.ROI_P_Municipality[1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)

    def getPermHouseNo(self):
        final_word = []
        point1 = rn.ROI_P_House_no[0]
        point2 = rn.ROI_P_House_no[1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)

    def getPermWardNo(self):
        final_word = []
        point1 = rn.ROI_P_Ward_no[0]
        point2 = rn.ROI_P_Ward_no[1]

        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        # Crop the rectangular region from the image
        cropped_image = self.image[y1:y2, x1:x2]

        contours = pw.seperate_words(cropped_image)
        
        # Iterate through each contour
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                # plt.imshow(final_image,cmap="gray")
                # plt.show()
        return ''.join(final_word)

    
def main():
    image = cv2.imread("Forms/output_image.jpg")
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    getter = getTheWords(image)
    ans = getter.getNLastName()
    print("Answer is : ",ans)


if __name__ == "__main__":
    main()