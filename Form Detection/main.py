import cv2
import numpy as np

# Load the image
image = cv2.imread("Forms/output_image.jpg")

# Resize the image to a manageable size
# image = cv2.resize(image, (1000, 1500))

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 1)

# Perform edge detection using Canny
edges = cv2.Canny(blurred, 100, 100)

# Find contours in the edge-detected image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Find the contour with the maximum area
max_contour = max(contours, key=cv2.contourArea)

# Get the bounding box coordinates of the largest contour
x, y, w, h = cv2.boundingRect(max_contour)

# Define the margin to remove (in this case, 20 pixels)
margin = 20

# Adjust the bounding box coordinates
x += margin
y += margin
w -= 2 * margin
h -= 2 * margin

# Crop the region of interest (ROI) from the original image
cropped_image = image[y:y+h, x:x+w]

cropped_image = cv2.resize(cropped_image,(700,700))
# Display the cropped image
cv2.imshow("Cropped Image", cropped_image)
cv2.imwrite("Forms/finalImage.jpg", cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
