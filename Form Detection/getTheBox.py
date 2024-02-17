import cv2

image = cv2.imread("Forms/Aligned_Image2_8bit.jpg")
image = cv2.resize(image,(650*2,700*2))
roi = [[(70, 230), (112, 274)], [(114, 228), (154, 274)], [(154, 230), (194, 276)], [(194, 230), (234, 278)], [(234, 228), (276, 278)], [(276, 228), (316, 276)], [(312, 226), (356, 274)], [(356, 226), (396, 274)], [(394, 228), (434, 274)]]
for points in roi:
    point1 = points[0]
    point2 = points[1]

    x1, y1 = max(0, point1[0] + 5), max(0, point1[1] + 5)
    x2, y2 = min(image.shape[1], point2[0] - 5), min(image.shape[0], point2[1] - 5)

    # Crop the rectangular region from the image
    cropped_image = image[y1:y2, x1:x2]

    # Display the cropped image
    cv2.imshow("Cropped Image", cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
