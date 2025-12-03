import cv2
import numpy as np
import time
raw_vid=cv2.VideoCapture('idkwhatybroisdoing.mp4')
time.sleep(1)
background=0
count=0
for i in range(60):
    return_val,background=raw_vid.read()
    if return_val==False:
        continue
background=np.flip(background,axis=1)
#flip horizontaly
while raw_vid.isOpened():
    return_val,img=raw_vid.read()
    if not return_val:
        break
    #reading will fail at end of vid\
    count+=1
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #hsv color detection is easier
    #Hue Saturation=intensity Value=brightness
    lower_range=np.array([35,80,40])
    #color blue 
    upper_range=np.array([70,255,255])
    masking1=cv2.inRange(hsv,lower_range,upper_range)
    #mask created :selcts the pixels, detected=white , not=black
    lower_range=np.array([70,80,40])
    upper_range=np.array([90,255,255])
    #red
    masking2=cv2.inRange(hsv,lower_range,upper_range)
    masking1=masking1+masking2
    #refine masking
    masking1=cv2.morphologyEx(masking1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8),iterations=2)
    masking1=cv2.dilate(masking1,np.ones((3,3),np.uint8),iterations=1)
    masking2=cv2.bitwise_not(masking1)
    #creating an inveresed mask in masking2
    res1=cv2.bitwise_and(background,background,mask=masking1)
    #replace background with background
    res2=cv2.bitwise_and(img,img,mask=masking2)
    #show real image
    final=cv2.addWeighted(res1,1,res2,1,0)
    cv2.imshow('Invisible Man',final)
    k=cv2.waitKey(10)
    if k==27:
        break
    
