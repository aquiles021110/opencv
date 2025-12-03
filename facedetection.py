import cv2
import os
haar_face='haarcascade_frontalface_default.xml'
facecascade=cv2.CascadeClassifier(haar_face) #
personal_dataset=input('Enter the name of your personal dataset\n')
personal_dataset.strip()
dataset_path='datasets'
if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)
personal_folder=os.path.join(dataset_path,personal_dataset)
if not os.path.exists(personal_folder):
    os.makedirs(personal_folder)
cam=cv2.VideoCapture(0)
count=0
print('Face the camera. Stay centered and well-lit.')
