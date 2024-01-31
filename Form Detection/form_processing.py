import cv2
import numpy as np
import utils

heightImg = 500
widthImg = 500

img = cv2.imread("Forms/base.jpg")
#resizing the image
img = cv2.resize(img,(widthImg,heightImg))
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5), 0.1)
kernel = np.ones((5,5))
img2 = cv2.Canny(imgBlur, 100, 100)
imgDial = cv2.dilate(img2,kernel,iterations=2) #apply dilation
# imgThreshold = cv2.erode(img2,kernel,iterations=1) #apply erosion

#find contours
imgContours = img.copy()
imgBigContour = img.copy()
contours,hierarchy = cv2.findContours(img2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgContours,contours,-1,(255,0,0),2)

box1 = np.zeros((4, 2))  # Initialize box1 as a numpy array of shape (4, 2)
box2 = []

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    box2.append(w * h)

len = np.max(box2)

# Assuming you want to find the bounding box of the contour with area equal to the length of box2
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if w * h == (len):
        print(x,y,w,h)
        # Assigning corner coordinates to box1
        box1[0] = [x, y]
        box1[1] = [x + w, y]
        box1[2] = [x + w, y + h]
        box1[3] = [x, y + h]
        break

print(box1)

# peri = cv2.arcLength(box1, True)
# biggest = cv2.approxPolyDP(box1, 0.02 * peri, True)

#find biggest contours
# biggest,maxArea = utils.biggestContour(contours)
# print(maxArea)
biggest = utils.reorder(box1)
print(biggest)
# cv2.drawContours(imgBigContour, biggest, -1 , (255,0,0),20)
# imgBigContour = utils.drawRectangle(imgBigContour, biggest,2)

# pts1 = np.float32(biggest)  # PREPARE POINTS FOR WARP
# pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])  # PREPARE POINTS FOR WARP
# matrix = cv2.getPerspectiveTransform(pts1, pts2)
# imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

# # REMOVE 20 PIXELS FORM EACH SIDE
# imgWarpColored = imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
# imgWarpColored = cv2.resize(imgWarpColored, (widthImg, heightImg))
#
# # APPLY ADAPTIVE THRESHOLD
# imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
# imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, 1, 1, 7, 2)
# imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)
# imgAdaptiveThre = cv2.medianBlur(imgAdaptiveThre, 3)

# cv2.imshow("BaseImage",imgAdaptiveThre)
cv2.imshow("Contours",imgContours)
cv2.waitKey(0)