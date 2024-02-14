import cv2
import numpy as np

# Load and preprocess the image
img = cv2.imread("Forms/baseimage1.jpeg")
img = cv2.resize(img, (500, 500))
img_another = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.equalizeHist(img)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((4, 4), np.uint8)
img1 = cv2.GaussianBlur(gray, (5, 5), 1)

# Apply Canny edge detection
edges = cv2.Canny(img1, 100, 100)  # Adjust thresholds if needed
contours, hierarchy = cv2.findContours(edges, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Filter for box-like contours
box_contours = []
for cnt in contours:
    # Approximate the contour with a polygon
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

    # Check if the approximation has 4 sides (indicating a box)
    if len(approx) == 4 and cv2.contourArea(cnt) > 10000:
        box_contours.append(cnt)

# Sort box contours based on their areas in descending order
box_contours.sort(key=cv2.contourArea, reverse=True)

biggest_contours = box_contours[:1]

# Save the cropped segments corresponding to the biggest contours as individual images
for idx, cnt in enumerate(biggest_contours):
    # Get bounding box coordinates
    x, y, w, h = cv2.boundingRect(cnt)
    x_max = x + w
    y_max = y + h

    box_image = img_another[y:y_max,x:x_max]

    cv2.imshow("Image", box_image)
    cv2.waitKey(0)

# Optional: Draw the biggest contours on the original image
cv2.drawContours(img, biggest_contours, -1, (0, 255, 0), 2)  # Green outline for biggest contours

# Display the image with biggest contours
cv2.imshow("Image", img)
cv2.waitKey(0)
