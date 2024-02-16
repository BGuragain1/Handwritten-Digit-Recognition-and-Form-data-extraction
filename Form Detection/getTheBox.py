import cv2

image = cv2.imread("Forms/Aligned_Image.jpg")
# image = cv2.imread("Boxes/844.jpg")
image = cv2.resize(image,(650*2,700*2))
# image = cv2.resize(image,(422*2,78*2))
roi = [[(14, 152), (416, 210)], [(446, 150), (848, 200)], [(870, 146), (1274, 196)], [(22, 256), (404, 314)], [(474, 254), (772, 308)], [(848, 246), (1274, 294)], [(24, 356), (430, 408)], [(454, 356), (806, 406)], [(846, 346), (1272, 398)], [(26, 570), (422, 622)], [(450, 564), (856, 620)], [(884, 562), (1274, 612)], [(22, 680), (430, 732)], [(80, 926), (432, 984)], [(460, 926), (816, 984)], [(840, 924), (906, 984)], [(956, 924), (1070, 986)], [(80, 1062), (436, 1118)], [(458, 1058), (812, 1114)], [(844, 1058), (910, 1112)], [(966, 1060), (1078, 1112)], [(102, 1200), (302, 1382)], [(336, 1192), (546, 1376)], [(676, 1190), (888, 1374)], [(916, 1188), (1122, 1378)]]
# roi = [[(12, 44), (88, 142)], [(90, 40), (166, 142)], [(172, 42), (244, 132)], [(252, 38), (324, 132)], [(328, 40), (412, 134)], [(410, 34), (492, 136)]]
for points in roi:
    point1 = points[0]
    point2 = points[1]

    x1, y1 = max(0, point1[0] - 20), max(0, point1[1] - 20)
    x2, y2 = min(image.shape[1], point2[0] + 20), min(image.shape[0], point2[1] + 20)

    # x1,y1,x2,y2= point1[0]-20, point1[1]-20,point2[0]+20,point2[1]+20
    # x1,y1,x2,y2= point1[0], point1[1],point2[0],point2[1]

    # Crop the rectangular region from the image
    cropped_image = image[y1:y2, x1:x2]

    # Display the cropped image
    cv2.imshow("Cropped Image", cropped_image)
    cv2.imwrite("Boxes/"+str(point1[0])+".jpg",cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
