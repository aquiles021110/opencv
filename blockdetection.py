import cv2
import numpy as np
image=cv2.imread('blobs.png',0)
param=cv2.SimpleBlobDetector_Params()
param.filterByArea=True
#area based filtering;smaller than a certain size ignored
param.minArea=100 #blobs of >100 pixels
param.filterByCircularity=True #only detects the blobs that are close to cirlces
param.minCircularity=0.9
param.filterByConvexity=True #how convex a blob is
param.minConvexity=0.2
param.filterByInertia=True #mesures how elongated a shape is
param.minInertiaRatio=0.01
detector=cv2.SimpleBlobDetector_create(param)
keypoints=detector.detect(image) #list keypoint will give diameter and cooridinates
blank=np.zeros((1,1)) #this image will be  blank: size of 1x1
blobs=cv2.drawKeypoints(image,keypoints,blank,(0,0,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
numbrofblobs=len(keypoints)
text='Blobs:'+str(numbrofblobs)
cv2.putText(blobs,text,(20,550),cv2.FONT_HERSHEY_DUPLEX,1,(0,225,0),2)
cv2.imshow('Blobs',blobs)
cv2.waitKey(0)
cv2.destroyAllWindows()