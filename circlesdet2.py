import cv2
import numpy as np
image=cv2.imread('circles.png',cv2.IMREAD_COLOR)
imagegrey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#hough circle detection works only on single channel images
blurimage=cv2.blur(imagegrey,(3,3))
#to prevent false circle detections and smoothen
circles=cv2.HoughCircles(blurimage,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)
if circles is not None:
    circles=np.uint16(np.around(circles))
    for i in circles[0,:]:
        x1,y1,r=i[0],i[1],i[2]
        cv2.circle(image,(x1,y1),r,(0,0,255),2)
        cv2.circle(image,(x1,y1),1,(0,255,0),3)
        cv2.imshow('Circles',image)
        cv2.waitKey(0)
cv2.destroyAllWindows()
