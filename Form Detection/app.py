import cv2
import form_process as fp
from getTheBox import getTheWords
import createJSON as cj

image = cv2.imread("Forms/2.jpg")
output_image = fp.preprocess_image(image)
jsonData = cj.createJSON(output_image)
print(jsonData)