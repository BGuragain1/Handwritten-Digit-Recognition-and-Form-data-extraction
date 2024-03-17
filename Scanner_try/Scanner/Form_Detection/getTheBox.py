import cv2
# from Form_Detection import RegionOfInterest as rn
# from Form_Detection import predictTheWords as pw
import numpy as np
import matplotlib.pyplot as plt
import RegionOfInterest as rn
import predictTheWords as pw

kernel1  = np.ones((3, 3), np.uint8)
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

            plt.imshow(final_image,cmap="gray")
            plt.show()

            print(np.sum(final_image))
            if np.sum(final_image) > 5000:
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

            plt.imshow(final_image,cmap="gray")
            plt.show()

            print(np.sum(final_image))
            if np.sum(final_image) > 5000:
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

            plt.imshow(final_image,cmap="gray")
            plt.show()

            print(np.sum(final_image))
            if np.sum(final_image) > 5000:
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

            plt.imshow(final_image,cmap="gray")
            plt.show()

            print(np.sum(final_image))
            if np.sum(final_image) > 5000:
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
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

            plt.imshow(final_image,cmap="gray")
            plt.show()

            print(np.sum(final_image))
            if np.sum(final_image) > 5000:
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
        return ''.join(final_word)

    def getIssuedDate(self):
        final_word = []
        for points in rn.ROI_CN_date:
            point1 = points[0]
            point2 = points[1]

            x1, y1 = max(0, point1[0]), max(0, point1[1])
            x2, y2 = min(self.image.shape[1], point2[0]), min(self.image.shape[0], point2[1])

            # Crop the rectangular region from the image
            cropped_image = self.image[y1:y2, x1:x2]
            
            bin_img = cv2.adaptiveThreshold(cropped_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 11)

            # bin_img = cv2.dilate(bin_img, kernel1, iterations=1)

            bin_img = cv2.GaussianBlur(bin_img, (3,3), 0)

            resized_image = cv2.resize(bin_img, (28, 28))
            
            plt.imshow(resized_image,cmap="gray")
            plt.show()
            print(np.sum(resized_image))
            if np.sum(resized_image) > 30000:
                word = pw.image_prediction(resized_image)
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

            plt.imshow(final_image,cmap="gray")
            plt.show()

            print(np.sum(final_image))
            if np.sum(final_image) > 5000:
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

            plt.imshow(final_image,cmap="gray")
            plt.show()

            print(np.sum(final_image))
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

            plt.imshow(final_image,cmap="gray")
            plt.show()

            print(np.sum(final_image))
            if np.sum(final_image) > 5000:
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

            plt.imshow(final_image,cmap="gray")
            plt.show()

            print(np.sum(final_image))
            if np.sum(final_image) > 5000:
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getSignature(self):
        return

    def getFingerPrints(self):
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
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
            last_image = cropped_image[y-2:y+h, x-2:x+w]
            final_image = pw.pre_process_img(last_image)
            
            print(np.sum(final_image))
            if (np.sum(final_image) > 30000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # Display the segmented characters
                plt.imshow(final_image,cmap="gray")
                plt.show()
        return ''.join(final_word)

    
def main():
    image = cv2.imread("Forms/Aligned_Image.jpg")
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    getter = getTheWords(image)
    ans = getter.getPhoneNumber()
    print("Answer is : ",ans)

if __name__ == "__main__":
    main()