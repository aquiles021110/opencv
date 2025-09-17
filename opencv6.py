import cv2
import numpy as np
#$Erosion$#
pika=cv2.imread('pokemon.png')
plane=cv2.imread('plane.png')
cat=cv2.imread('cat.png')
#kernel
kernel=np.ones((5,5),np.uint8)
erode=cv2.erode(pika,kernel)
#blur
gaussian=cv2.GaussianBlur(cat,(13,13),0)
#median blur
median=cv2.medianBlur(cat,5)
#bilateral blur
bilateral=cv2.bilateralFilter(cat,9,75,75)
together=np.concatenate((median,gaussian,bilateral,cat),axis=1)
cv2.imshow('Pika',together)
cv2.waitKey(0)
cv2.destroyAllWindows()