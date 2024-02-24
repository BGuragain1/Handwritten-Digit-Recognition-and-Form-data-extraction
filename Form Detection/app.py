import cv2
import form_process as fp
import createJSON as cj

def predict_from_form(path):
    image = cv2.imread(path)
    output_image = fp.preprocess_image(image)
    jsonData = cj.createJSON(output_image)
    print(jsonData)

def main():
    path = "Forms/2.jpg"
    predict_from_form(path)

if __name__ == "__main__":
    main()