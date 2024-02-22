import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model('my_model.h5')
arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "d", "e", "f", "g", "h", "n", "q", "r", "t"]

def image_preprocess(input_img):

  resized_image = cv2.resize(input_img, (28, 28))

  # gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

  # normalized_image = np.array(resized_image) / 255.0

  reshaped_image = resized_image.reshape((1, 28, 28, 1))

  return reshaped_image

def image_prediction(img):

  image = image_preprocess(img)

  prediction = model.predict(image)

  ans = np.argmax(prediction)

  word = arr[ans]

  return word
