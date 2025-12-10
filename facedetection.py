import cv2
import os
haar_face='haarcascade_frontalface_default.xml'
facecascade=cv2.CascadeClassifier(haar_face) 
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
while count<30:
    ret,frame=cam.read()
    if not ret:
        continue
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=facecascade.detectMultiScale(grey,1.3,5)
    for (x,y,w,h) in faces:
        face=grey[y:y+h,x:x+w]
        #crop the face from the greyscale image
        count+=1
        filename=os.path.join(personal_folder,f'{count}.jpg')
        cv2.imwrite(filename,face)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,f'Image {count}/30',(x,y-10),cv2.FONT_HERSHEY_DUPLEX,0.8,(255,0,0),5)
        print('Saved!')
    cv2.imshow('datasetcreator(press esc to exit)',frame)
    key=cv2.waitKey(1)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()
print('Dataset creation complete')
