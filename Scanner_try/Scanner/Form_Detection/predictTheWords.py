import tensorflow as tf
import numpy as np
import cv2

# model = tf.keras.models.load_model('Form_Detection/my_model.h5')
model = tf.keras.models.load_model('my_model.h5')
arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "d", "e", "f", "g", "h", "n", "q", "r", "t"]

def pre_process_img(img):
  bin_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 11)
  bin_img = cv2.GaussianBlur(bin_img, (3,3), 1)
  resized_image = cv2.resize(bin_img, (28, 28))
  return resized_image

def seperate_words(img):
  # Apply thresholding to create a binary image
  _, binary_image = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

  # Find contours in the binary image
  contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  return contours

def image_prediction(img):

  reshaped_image = img.reshape((1, 28, 28, 1))

  prediction = model.predict(reshaped_image)

  ans = np.argmax(prediction)

  word = arr[ans]

  return word

def num_predictions(img):

  reshaped_image = img.reshape((1, 28, 28, 1))

  prediction = model.predict(reshaped_image)

  ans = np.argmax(prediction)

  word = arr[ans]

  return word