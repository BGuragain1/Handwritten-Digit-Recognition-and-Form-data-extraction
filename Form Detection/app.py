import cv2
import form_process as fp
from getTheBox import getTheWords

image = cv2.imread("Forms/1.jpg")
output_image = fp.preprocess_image(image)
getter = getTheWords(output_image)
first_name = ''.join(getter.getFirstName())
print(first_name)