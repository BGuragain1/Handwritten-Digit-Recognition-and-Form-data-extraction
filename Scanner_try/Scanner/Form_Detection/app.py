import cv2
# from Form_Detection import form_process as fp
# from Form_Detection import createData as cj
import form_process as fp
import createData as cj

def predict_from_form(path):
    image = cv2.imread(path)
    output_image = fp.preprocess_image(image)
    data = cj.createData(output_image)
    print(data)
    return data

def main():
    path = "Forms/6.jpg"
    predict_from_form(path)

if __name__ == "__main__":
    main()