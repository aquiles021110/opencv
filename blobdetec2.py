import cv2
import numpy as np
image=cv2.imread('stickmen.jpg',0)
param=cv2.SimpleBlobDetector_Params()
param.filterByArea=True
param.minArea=100 
param.filterByCircularity=True
param.minCircularity=0.9
param.filterByConvexity=True 
param.minConvexity=0.2
param.filterByInertia=True 
param.minInertiaRatio=0.01
detector=cv2.SimpleBlobDetector_create(param)
keypoints=detector.detect(image) 
blank=np.zeros((1,1))
blobs=cv2.drawKeypoints(image,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
numbrofblobs=len(keypoints)
text='People:'+str(numbrofblobs)
cv2.putText(blobs,text,(20,550),cv2.FONT_HERSHEY_DUPLEX,1,(255,225,255),2)
cv2.imshow('People',blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()