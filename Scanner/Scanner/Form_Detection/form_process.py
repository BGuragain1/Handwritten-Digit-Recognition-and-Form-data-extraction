import cv2
import numpy as np
from Form_Detection import alignForm as af
import matplotlib.pyplot as plt

# def preprocessImage(img):
#     # resizing the image
#     img = cv2.resize(img, (1500, 1200),cv2.INTER_CUBIC)

#     imgThres = img.copy()

#     # removing text from the image
#     img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel, iterations=3)

#     #remove the background or make the background black
#     mask = np.zeros(img.shape[:2],np.uint8)
#     bgdModel = np.zeros((1,65),np.float64)
#     fgdModel = np.zeros((1,65),np.float64)
#     rect = (10,10,img.shape[1]-20,img.shape[0]-20)
#     cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
#     mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
#     img = img*mask2[:,:,np.newaxis]

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     gray = cv2.GaussianBlur(gray, (11, 11), 0)
    
#     return gray, imgThres

# def EdgeDetection(gray):
#     # Edge Detection.
#     canny = cv2.Canny(gray, 0, 200)
#     canny = cv2.dilate(canny, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5)))

#     # Finding contours for the detected edges.
#     contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
#     # Keeping only the largest detected contour.
#     page = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

#     # Loop over the contours.
#     for c in page:
#         # Approximate the contour.
#         epsilon = 0.02 * cv2.arcLength(c, True)
#         corners = cv2.approxPolyDP(c, epsilon, True)
#         # If our approximated contour has four points
#         if len(corners) == 4 and cv2.contourArea(c) > 10000:
#             # plt.imshow(cv2.drawContours(gray, [corners], -1, (225, 0, 0), 3))
#             break
#     return corners

# def gettingform(corners,imgThres):
#     # Sorting the corners and converting them to desired shape.
#     corners = sorted(np.concatenate(corners).tolist())

#     biggest = reorder(np.array(corners))

#     pts1 = np.float32(biggest)  # PREPARE POINTS FOR WARP
#     pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])  # PREPARE POINTS FOR WARP
#     matrix = cv2.getPerspectiveTransform(pts1, pts2)
#     imgWarpColored = cv2.warpPerspective(imgThres, matrix, (widthImg, heightImg))

#     # REMOVE 20 PIXELS FORM EACH SIDE
#     imgWarpColored = imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
#     imgWarpColored = cv2.resize(imgWarpColored, (widthImg, heightImg),cv2.INTER_CUBIC)

#     #converting to black amd white
#     imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)

#     # #Apply adaptive thresholding with a lower block size and a higher constant value to decrease the number of dots
#     imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 21)

#     # Invert the binary image
#     imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)

#     return imgAdaptiveThre
    
def refine(img):
    imgWarpColored = cv2.resize(img, (1200, 1500),cv2.INTER_CUBIC)
    #converting to black amd white
    imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)

    #Apply adaptive thresholding with a lower block size and a higher constant value to decrease the number of dots
    imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 21)

    # Invert the binary image
    imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)

    return imgAdaptiveThre
    
# def reorder(myPoints):
#     myPoints = myPoints.reshape((4, 2))
#     myPointsNew = np.zeros((4, 1, 2), dtype=np.int32)
#     add = myPoints.sum(1)

#     myPointsNew[0] = myPoints[np.argmin(add)]
#     myPointsNew[3] = myPoints[np.argmax(add)]
#     diff = np.diff(myPoints, axis=1)
#     myPointsNew[1] = myPoints[np.argmin(diff)]
#     myPointsNew[2] = myPoints[np.argmax(diff)]

#     return myPointsNew


heightImg = 1500
widthImg = 1200
kernel = np.ones((5, 5), np.uint8)

def preprocess_image(image):
    # grayImage,imgThreshold = preprocessImage(image)
    # finalCorners = EdgeDetection(grayImage)
    # finalImage = gettingform(finalCorners,imgThreshold)
    # output_image = af.alignForm(finalImage)
    finalImage = refine(image)
    output_image = af.alignForm(finalImage)
    return output_image

def main():
    final = preprocess_image(cv2.imread("Forms/Form8.jpg"))
    cv2.imwrite("Forms/output_8.jpg",final)
    plt.imshow(final)
    plt.show()

if __name__ == "__main__":
    main()
