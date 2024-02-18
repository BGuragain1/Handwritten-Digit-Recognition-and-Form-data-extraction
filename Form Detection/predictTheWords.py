import cv2
from tensorflow.keras.models import load_model
import numpy as np

model = load_model('characters_model.h5')

def predict(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
    img = cv2.resize(gray_image, (28, 28))
    img = img.reshape((1,28,28,1))
    processed_image = img.astype('float32') / 255.0  # Normalize to [0, 1]
    predictions = model.predict(processed_image)
    pr = np.argmax(predictions)
    print(pr)

def main():
    predict(image)

