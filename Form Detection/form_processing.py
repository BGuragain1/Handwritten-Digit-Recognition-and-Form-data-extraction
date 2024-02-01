import cv2
import numpy as np
import utils

heightImg = 1500
widthImg = 1500

img = cv2.imread("Forms/base.jpg")

#resizing the image
img = cv2.resize(img,(widthImg,heightImg))

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

imgBlur = cv2.GaussianBlur(imgGray,(11, 11), 0)

kernel = np.ones((5,5))
opening = cv2.morphologyEx(imgBlur, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)

img2 = cv2.Canny(closing, 50, 50)
_, imgThreshold = cv2.threshold(img2, 150, 255, cv2.THRESH_BINARY)

# #copying images
imgContours = img.copy()
imgBigContour = img.copy()

# #finding contours
contours,hierarchy = cv2.findContours(imgThreshold,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imgContours,contours,-1,(255,0,0),5)

biggest = np.array([])
max_area = 0  # Initialize max_area to a small value
for cnt in contours:
    # Approximate the contour with a polygon
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    area = cv2.contourArea(cnt)
    # Check if the approximation has 4 sides (indicating a box)
    if len(approx) == 4 and area > max_area:
        max_area = area
        biggest = approx

print(biggest)
#find biggest contours
# biggest,maxArea = utils.biggestContour(contours)
# print(biggest)
biggest = utils.reorder(biggest)
cv2.drawContours(imgBigContour, biggest, -1 , (255,0,0),20)
imgBigContour = utils.drawRectangle(imgBigContour, biggest,2)

pts1 = np.float32(biggest)  # PREPARE POINTS FOR WARP
pts2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])  # PREPARE POINTS FOR WARP
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

# REMOVE 20 PIXELS FORM EACH SIDE
imgWarpColored = imgWarpColored[20:imgWarpColored.shape[0] - 20, 20:imgWarpColored.shape[1] - 20]
imgWarpColored = cv2.resize(imgWarpColored, (widthImg, heightImg))

# Convert the warped colored image to grayscale
imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding with a lower block size
# and a higher constant value to decrease the number of dots
imgAdaptiveThre = cv2.adaptiveThreshold(imgWarpGray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 7)

# Invert the binary image
imgAdaptiveThre = cv2.bitwise_not(imgAdaptiveThre)

# Apply median blur with a larger kernel size to remove noise
imgAdaptiveThre = cv2.medianBlur(imgAdaptiveThre, 3)

cv2.imshow("Contour",imgContours)
cv2.imshow("Big",imgBigContour)
# cv2.imshow("Image",imgAdaptiveThre)
cv2.waitKey(0)