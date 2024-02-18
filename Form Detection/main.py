import cv2

import form_process as fp
import getTheBox as gb
import predictTheWords as pw

def main():
    image = fp.preprocess_image("Forms/6.jpg")
    boxes = gb.cropped_image(image)
