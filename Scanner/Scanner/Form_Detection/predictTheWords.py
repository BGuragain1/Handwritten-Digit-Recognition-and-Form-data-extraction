import tensorflow as tf
import numpy as np
import cv2
import matplotlib.pyplot as plt

letter_model = tf.keras.models.load_model('Form_Detection/model/letters_model.h5')
digit_model = tf.keras.models.load_model('Form_Detection/model/digit_model.h5')

arr_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
arr_letters = ["","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def pre_process_img(img):
  kernel1  = np.ones((3, 3), np.uint8)
  bin_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 21)
  bin_img = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel1)
  bin_img = cv2.GaussianBlur(bin_img, (5,5), 1)
  bin_img = cv2.bilateralFilter(bin_img, 9, 75, 75) 
  dilated_image = cv2.dilate(bin_img, kernel1, iterations=1)
  resized_image = cv2.resize(dilated_image , (28, 28))
  return resized_image


def pre_process_seperated_img(img):
  kernel1  = np.ones((3, 3), np.uint8)
  bin_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 21)
  bin_img = addPadding_seperated(bin_img)
  bin_img = cv2.morphologyEx(bin_img, cv2.MORPH_OPEN, kernel1)
  bin_img = cv2.GaussianBlur(bin_img, (5,5), 1)
  bin_img = cv2.bilateralFilter(bin_img, 9, 75, 75) 
  bin_img = addPadding(bin_img)
  resized_image = cv2.resize(bin_img , (28, 28))
  return resized_image

def image_prediction(img):

  img = img.reshape(-1,28,28,1)

  prediction = letter_model.predict(img)

  ans = np.argmax(prediction)

  word = arr_letters[ans]

  return word

def num_predictions(img):

  reshaped_image = img.reshape(-1,28, 28, 1)

  prediction = digit_model.predict(reshaped_image)

  ans = np.argmax(prediction)

  word = arr_digits[ans]

  return word

def addPadding_seperated(img):
  h, w = img.shape

  # Define the size of the new image with black surface
  new_h = h + 5 # Add some padding (adjust as needed)
  new_w = w + 5  # Add some padding (adjust as needed)

  # Create a blank black image
  black_surface = np.zeros((new_h, new_w), dtype=np.uint8)

  # Calculate the position to place the cropped image on the black surface
  x_offset = (new_w - w) // 2
  y_offset = (new_h - h) // 2

  # Place the cropped image onto the black surface
  black_surface[y_offset:y_offset+h, x_offset:x_offset+w] = img

  return black_surface

def addPadding(img):
  h, w = img.shape

  # Define the size of the new image with black surface
  new_h = h + 8 # Add some padding (adjust as needed)
  new_w = w + 8  # Add some padding (adjust as needed)

  # Create a blank black image
  black_surface = np.zeros((new_h, new_w), dtype=np.uint8)

  # Calculate the position to place the cropped image on the black surface
  x_offset = (new_w - w) // 2
  y_offset = (new_h - h) // 2

  # Place the cropped image onto the black surface
  black_surface[y_offset:y_offset+h, x_offset:x_offset+w] = img

  return black_surface

def seperate_words(img):
  _, binary_image = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

  contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  filtered_contours = []
  min_area = 100  
  max_area = 10000 
  for contour in contours:
      area = cv2.contourArea(contour)
      if min_area < area < max_area:
          filtered_contours.append(contour)

  filtered_contours.sort(key=lambda cnt: cv2.boundingRect(cnt)[0])

  return filtered_contours
