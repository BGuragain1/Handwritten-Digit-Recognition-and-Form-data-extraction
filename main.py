import cv2
import numpy as np

# Load and preprocess the image
img = cv2.imread("baseimage.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((4,4),np.uint8)
img1 = cv2.GaussianBlur(gray, (5, 5), 1)
# Apply Canny edge detection
edges = cv2.Canny(img1, 100, 100)  # Adjust thresholds if needed
contours, hierarchy = cv2.findContours(edges, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

# Filter for box-like contours
box_contours = []
for cnt in contours:
  # Approximate the contour with a polygon
  approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)

  # Check if they approximation has 4 sides (indicating a box)
  if len(approx) == 4 and cv2.contourArea(cnt) > 100000:
    box_contours.append(cnt)

# Apply Non-Maximal Suppression (NMS)
def nms(contours, area_thr=0.5):
    bounding_boxes = [cv2.boundingRect(cnt) for cnt in contours]

    # Get areas and scores (use area as a score here, adapt based on your needs)
    areas = [cv2.contourArea(cnt) for cnt in contours]
    scores = areas

    # Perform Non-Maximum Suppression (NMS)
    kept_indices = cv2.dnn.NMSBoxes(bounding_boxes, scores, 0.5, area_thr)

    # Return the kept contours based on indices
    return [contours[i] for i in kept_indices]

# Filter overlapping boxes with NMS
kept_box_contours = nms(box_contours)

# Process the identified box contours
print(f"Number of box contours after NMS: {len(kept_box_contours)}")

for cnt in kept_box_contours:
  # Get bounding box coordinates
  x, y, w, h = cv2.boundingRect(cnt)

  # Extract the image segment using NumPy slicing
  box_image = img[y:y+h, x:x+w]

  # Display the extracted box image (optional)
  cv2.imshow("another",box_image)
  cv2.waitKey(0)

# Optional: Draw the box contours on the original image
cv2.drawContours(img, kept_box_contours, -1, (255, 0, 0), 2)  # Red outline for boxes

# Display the image with box contours
cv2.imshow("Image",img)
cv2.waitKey(0)
