import cv2
from Form_Detection import RegionOfInterest as rn
from Form_Detection import predictTheWords as pw
import numpy as np
import matplotlib.pyplot as plt


class getTheWords1():

    def __init__(self,image):
        self.image = image
        self.image = cv2.resize(self.image, (1000*2, 1500*2),cv2.INTER_CUBIC)
    
    def getFirstName(self):
        final_word = []
        x1,y1 = rn.roi_first_name[0][0],rn.roi_first_name[0][1]
        x2,y2 = rn.roi_first_name[1][0],rn.roi_first_name[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # plt.imshow(final_image)
                # plt.show()
        return ''.join(final_word)

    def getMiddleName(self):
        final_word = []
        x1,y1 = rn.roi_middle_name[0][0],rn.roi_middle_name[0][1]
        x2,y2 = rn.roi_middle_name[1][0],rn.roi_middle_name[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # plt.imshow(final_image)
                # plt.show()
        return ''.join(final_word)

        
    def getLastName(self):
        final_word = []
        x1,y1 = rn.roi_last_name[0][0],rn.roi_last_name[0][1]
        x2,y2 = rn.roi_last_name[1][0],rn.roi_last_name[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            
            # print(np.sum(final_image))
            if (np.sum(final_image) > 10000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # plt.imshow(final_image)
                # plt.show()
        return ''.join(final_word)

    def getCitizenno(self):
        final_word = []
        for points in rn.roi_citizenNumber:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)
            if np.sum(final_image) > 10000:
                word = pw.num_predictions(final_image)
                final_word.append(word)
                # plt.imshow(final_image,cmap="gray")
                # plt.show()

        return ''.join(final_word)

    def getPhoneNumber(self):
        final_word = []
        for points in rn.roi_phonenumber:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)
            if np.sum(final_image) > 10000:
                word = pw.num_predictions(final_image)
                final_word.append(word)
                # plt.imshow(final_image,cmap="gray")
                # plt.show()

        return ''.join(final_word)

    def getEmail1(self):
        final_word = []
        x1,y1 = rn.roi_email1[0][0],rn.roi_email1[0][1]
        x2,y2 = rn.roi_email1[1][0],rn.roi_email1[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            # print(np.sum(final_image))
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # plt.imshow(final_image)
                # plt.show()
        return ''.join(final_word)
        
    def getEmail2(self):
        final_word = []
        x1,y1 = rn.roi_email2[0][0],rn.roi_email2[0][1]
        x2,y2 = rn.roi_email2[1][0],rn.roi_email2[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            # print(np.sum(final_image))
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
                # plt.imshow(final_image)
                # plt.show()
        return ''.join(final_word)
        
    def getDOB(self):
        final_word = []
        for points in rn.roi_dob:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)
            if np.sum(final_image) > 10000:
                word = pw.num_predictions(final_image)
                final_word.append(word)
                # plt.imshow(final_image,cmap="gray")
                # plt.show()

        ans = ''.join(final_word)
        dob_str = str(ans)
        year = dob_str[4:8]
        month = dob_str[2:4]
        day = dob_str[:2]
        formatted_dob = f"{day}/{month}/{year}"
        return formatted_dob

        
    def getGender(self):
        final_word = []
        for points in rn.roi_gender:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]
            cropped_image = self.image[y1:y2, x1:x2]
            final_image = pw.pre_process_img(cropped_image)
            final_word.append(np.sum(final_image))
        
        ans = np.argmax(final_word)
        if ans == 0:
            return "Male"
        elif ans == 1:
            return "Female"
        else:
            return "Others"
        
    def getcourse(self):
        final_word = []
        for points in rn.roi_gender:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]
            cropped_image = self.image[y1:y2, x1:x2]
            final_image = pw.pre_process_img(cropped_image)
            final_word.append(np.sum(final_image))
        
        ans = np.argmax(final_word)
        if ans == 0:
            return "Bsc Computer Science"
        elif ans == 1:
            return "IMBA"
        elif ans == 2:
            return "BIBM"

    def gettempProvince(self):
        final_word = []
        x1,y1 = rn.roi_tempProvince[0][0],rn.roi_tempProvince[0][1]
        x2,y2 = rn.roi_tempProvince[1][0],rn.roi_tempProvince[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
        
    def gettempDistrict(self):
        final_word = []
        x1,y1 = rn.roi_tempDistrict[0][0],rn.roi_tempDistrict[0][1]
        x2,y2 = rn.roi_tempDistrict[1][0],rn.roi_tempDistrict[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
        
    def gettempMunici(self):
        final_word = []
        x1,y1 = rn.roi_tempMuni[0][0],rn.roi_tempMuni[0][1]
        x2,y2 = rn.roi_tempMuni[1][0],rn.roi_tempMuni[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
        
    def gettempWard(self):
        final_word = []
        x1,y1 = rn.roi_tempWard[0][0],rn.roi_tempWard[0][1]
        x2,y2 = rn.roi_tempWard[1][0],rn.roi_tempWard[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.num_predictions(final_image)
                final_word.append(word)
        return ''.join(final_word)

    def gettempTole(self):
        final_word = []
        x1,y1 = rn.roi_tempTole[0][0],rn.roi_tempTole[0][1]
        x2,y2 = rn.roi_tempTole[1][0],rn.roi_tempTole[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)

    def getpermProvince(self):
        final_word = []
        x1,y1 = rn.roi_permProvince[0][0],rn.roi_permProvince[0][1]
        x2,y2 = rn.roi_permProvince[1][0],rn.roi_permProvince[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
    
    def getpermDistrict(self):
        final_word = []
        x1,y1 = rn.roi_permDistrict[0][0],rn.roi_permDistrict[0][1]
        x2,y2 = rn.roi_permDistrict[1][0],rn.roi_permDistrict[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
    
    def getpermMunici(self):
        final_word = []
        x1,y1 = rn.roi_permMuni[0][0],rn.roi_permMuni[0][1]
        x2,y2 = rn.roi_permMuni[1][0],rn.roi_permMuni[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
    
    def getpermWard(self):
        final_word = []
        x1,y1 = rn.roi_permWard[0][0],rn.roi_permWard[0][1]
        x2,y2 = rn.roi_permWard[1][0],rn.roi_permWard[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.num_predictions(final_image)
                final_word.append(word)
        return ''.join(final_word)
    
    def getpermTole(self):
        final_word = []
        x1,y1 = rn.roi_permTole[0][0],rn.roi_permTole[0][1]
        x2,y2 = rn.roi_permTole[1][0],rn.roi_permTole[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
    
    
    def savePhoto(self,image_name):
        point1 = rn.roi_photo[0]
        point2 = rn.roi_photo[1]
        
        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        cropped_image_first = self.image[y1:y2, x1:x2]
        cv2.imwrite('media/uploads/photo/P_'+image_name+'.jpg', cropped_image_first)
        return


class getTheWords2():
        
    def __init__(self,image):
        self.image = image
        self.image = cv2.resize(self.image, (1000*2, 1500*2),cv2.INTER_CUBIC)

    def saveSignature(self,image_name):
        point1 = rn.roi_signature[0]
        point2 = rn.roi_signature[1]
        
        x1, y1 = point1[0],point1[1]
        x2, y2 = point2[0],point2[1]

        cropped_image_first = self.image[y1:y2, x1:x2]
        cv2.imwrite('media/uploads/signature/S_'+image_name+'.jpg', cropped_image_first)
        return

    def getGfirstname(self):
        final_word = []
        x1,y1 = rn.roi_gfirstname[0][0],rn.roi_gfirstname[0][1]
        x2,y2 = rn.roi_gfirstname[1][0],rn.roi_gfirstname[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)
        
    def getGmiddlename(self):
        final_word = []
        x1,y1 = rn.roi_gmiddlename[0][0],rn.roi_gmiddlename[0][1]
        x2,y2 = rn.roi_gmiddlename[1][0],rn.roi_gmiddlename[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word) 
    
    def getGlastname(self):
        final_word = []
        x1,y1 = rn.roi_glastname[0][0],rn.roi_glastname[0][1]
        x2,y2 = rn.roi_glastname[1][0],rn.roi_glastname[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)


    def getGphone(self):
        final_word = []
        for points in rn.roi_gphonenumber:
            point1 = points[0]
            point2 = points[1]
            
            x1, y1 = point1[0],point1[1]
            x2, y2 = point2[0],point2[1]
            cropped_image = self.image[y1:y2, x1:x2]

            final_image = pw.pre_process_img(cropped_image)
            if np.sum(final_image) > 10000:
                word = pw.num_predictions(final_image)
                final_word.append(word)
                # plt.imshow(final_image,cmap="gray")
                # plt.show()

        return ''.join(final_word)
    
    def getRelation(self):
        final_word = []
        x1,y1 = rn.roi_grelation[0][0],rn.roi_grelation[0][1]
        x2,y2 = rn.roi_grelation[1][0],rn.roi_grelation[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)

        return ''.join(final_word)

    def getSschool(self):
        final_word = []
        x1,y1 = rn.roi_sSchool[0][0],rn.roi_sSchool[0][1]
        x2,y2 = rn.roi_sSchool[1][0],rn.roi_sSchool[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)

    def getSGraduation(self):
        final_word = []
        x1,y1 = rn.roi_sgradyear[0][0],rn.roi_sgradyear[0][1]
        x2,y2 = rn.roi_sgradyear[1][0],rn.roi_sgradyear[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.num_predictions(final_image)
                final_word.append(word)
        return ''.join(final_word)

    def getSmuni(self):
        final_word = []
        x1,y1 = rn.roi_smuni[0][0],rn.roi_smuni[0][1]
        x2,y2 = rn.roi_smuni[1][0],rn.roi_smuni[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)

    def getSCGPA(self):
        final_word = []
        x1,y1 = rn.roi_sgpa[0][0],rn.roi_sgpa[0][1]
        x2,y2 = rn.roi_sgpa[1][0],rn.roi_sgpa[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.num_predictions(final_image)
                final_word.append(word)
            return ''.join(final_word)
            
    def getSDistrict(self):
        final_word = []
        x1,y1 = rn.roi_sdistrict[0][0],rn.roi_sdistrict[0][1]
        x2,y2 = rn.roi_sdistrict[1][0],rn.roi_sdistrict[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
          
    def getSward(self):
        final_word = []
        x1,y1 = rn.roi_swardno[0][0],rn.roi_swardno[0][1]
        x2,y2 = rn.roi_swardno[1][0],rn.roi_swardno[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.num_predictions(final_image)
                final_word.append(word)
        return ''.join(final_word)
               
    def getHGschool(self):
        final_word = []
        x1,y1 = rn.roi_hSchool[0][0],rn.roi_hSchool[0][1]
        x2,y2 = rn.roi_hSchool[1][0],rn.roi_hSchool[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
               
    def getHSGraduation(self):
        final_word = []
        x1,y1 = rn.roi_hgraduatedy[0][0],rn.roi_hgraduatedy[0][1]
        x2,y2 = rn.roi_hgraduatedy[1][0],rn.roi_hgraduatedy[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.num_predictions(final_image)
                final_word.append(word)
        return ''.join(final_word)
                
    def getHSMuni(self):
        final_word = []
        x1,y1 = rn.roi_hmuni[0][0],rn.roi_hmuni[0][1]
        x2,y2 = rn.roi_hmuni[1][0],rn.roi_hmuni[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
               
    def getHSCGPA(self):
        final_word = []
        x1,y1 = rn.roi_hgpa[0][0],rn.roi_hgpa[0][1]
        x2,y2 = rn.roi_hgpa[1][0],rn.roi_hgpa[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.num_predictions(final_image)
                final_word.append(word)
        return ''.join(final_word)
               
    def getHSDistrict(self):
        final_word = []
        x1,y1 = rn.roi_hdistrict[0][0],rn.roi_hdistrict[0][1]
        x2,y2 = rn.roi_hdistrict[1][0],rn.roi_hdistrict[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)
                
    def getHSWard(self):
        final_word = []
        x1,y1 = rn.roi_hwardno[0][0],rn.roi_hwardno[0][1]
        x2,y2 = rn.roi_hwardno[1][0],rn.roi_hwardno[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.num_predictions(final_image)
                final_word.append(word)
        return ''.join(final_word)
    
    def HFaculty(self):
        final_word = []
        x1,y1 = rn.roi_hfaculty[0][0],rn.roi_hfaculty[0][1]
        x2,y2 = rn.roi_hfaculty[1][0],rn.roi_hfaculty[1][1]

        cropped_image = self.image[y1:y2, x1:x2]
        contours = pw.seperate_words(cropped_image)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            last_image = cropped_image[y:y+h, x:x+w]
            final_image = pw.pre_process_seperated_img(last_image)
          
            if (np.sum(final_image) > 1000):
                word = pw.image_prediction(final_image)
                final_word.append(word)
        return ''.join(final_word)

def main():
    image = cv2.imread("Forms/output2.jpg")
    image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    getter = getTheWords1(image)
    ans = getter.getGfirstname()
    print("Answer is : ",ans)

if __name__ == "__main__":
    main()