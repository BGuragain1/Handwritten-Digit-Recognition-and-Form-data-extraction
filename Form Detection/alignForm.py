import cv2
import numpy as np

def alignForm(image1, image2):
    # Convert images to grayscale
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # Find keypoints and descriptors using SIFT
    orb = cv2.ORB_create()
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # Match features between the two images
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(descriptors1, descriptors2)

    matches = sorted(matches, key=lambda x: x.distance)

    # Select top matches
    num_good_matches = 50
    good_matches = matches[:num_good_matches]

    # Extract corresponding keypoints
    points1 = np.float32([keypoints1[match.queryIdx].pt for match in good_matches])
    points2 = np.float32([keypoints2[match.trainIdx].pt for match in good_matches])

    # Calculate transformation matrix
    transformation_matrix, _ = cv2.findHomography(points2, points1, cv2.RANSAC)


    # Apply transformation to form2
    aligned_image = cv2.warpPerspective(image2, transformation_matrix, (image1.shape[1], image1.shape[0]))

    # Show the result
    cv2.imshow('Aligned Image', aligned_image)
    cv2.imwrite('Forms/Aligned_Image2_8bit.jpg', aligned_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image1 = cv2.imread('Forms/output_image.jpg')
image2 = cv2.imread('Forms/output_image3.jpg')
alignForm(image1, image2)
