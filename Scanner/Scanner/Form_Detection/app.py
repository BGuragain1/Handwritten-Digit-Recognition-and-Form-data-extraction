import cv2
from Form_Detection import form_process as fp
from Form_Detection import createData as cj

def predict_from_form(path1,path2,image_name):
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    output_image1 = fp.preprocess_image(img1,1)
    output_image2 = fp.preprocess_image(img2,2)
    data = cj.createData(output_image1,output_image2,image_name)
    return data

def main():
    path1 = "Forms/Form1.jpg"
    path2 = "Forms/Form2.jpg"
    predict_from_form(path1,path2,"image_name")

if __name__ == "__main__":
    main()