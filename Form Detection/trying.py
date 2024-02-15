import cv2
import numpy as np

def preprocessImage(img):
    # resizing the image
    img = cv2.resize(img, (heightImg, widthImg))

    imgThres = img.copy()

    # removing text from the image
    img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=3)

    #remove the background or make the background black
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (10,10,img.shape[1]-20,img.shape[0]-20)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]

    return img, imgThres


heightImg = 600
widthImg = 600
kernel = np.ones((5,5),np.uint8)

image = cv2.imread("Forms/3.jpg")
grayImage,imgThreshold = preprocessImage(image)
finalCorners = EdgeDetection(grayImage,imgThreshold)
finalImage = gettingform(finalCorners,imgThreshold)

cv2.imshow("second",grayImage)
# cv2.imshow("second",imgThreshold)
cv2.waitKey(0)

