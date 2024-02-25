import tensorflow as tf
import numpy as np
import cv2

model = tf.keras.models.load_model('Form_Detection/my_model.h5')
arr = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "d", "e", "f", "g", "h", "n", "q", "r", "t"]
def image_prediction(img):

  resized_image = cv2.resize(img, (28, 28))

  denoised_box = cv2.medianBlur(resized_image, 5)

  _, binary_box = cv2.threshold(denoised_box, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

  reshaped_image = resized_image.reshape((1, 28, 28, 1))

  prediction = model.predict(reshaped_image)

  ans = np.argmax(prediction)

  word = arr[ans]

  return word
