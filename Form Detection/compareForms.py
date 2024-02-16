import cv2
import numpy as np

# Load the two images
image1 = cv2.imread('Forms/output_image.jpg')
image2 = cv2.imread('Forms/output_image1.jpg')

# Convert images to grayscale
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# Find keypoints and descriptors using SIFT
sift = cv2.SIFT_create()
keypoints1, descriptors1 = sift.detectAndCompute(gray1, None)
keypoints2, descriptors2 = sift.detectAndCompute(gray2, None)

# Match descriptors between the two images
bf = cv2.BFMatcher()
matches = bf.knnMatch(descriptors1, descriptors2, k=2)

# Apply ratio test
good_matches = []
for m, n in matches:
    if m.distance < 0.75 * n.distance:
        good_matches.append(m)

# Extract matched keypoints
src_pts = np.float32([keypoints1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
dst_pts = np.float32([keypoints2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

# Find homography matrix
H, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

# Warp second image to align with the first one
aligned_image = cv2.warpPerspective(image2, H, (image1.shape[1], image1.shape[0]))

# Show the result
cv2.imshow('Aligned Image', aligned_image)
cv2.imwrite('Forms/Aligned_Image1.jpg', aligned_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
