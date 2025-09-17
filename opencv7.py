import cv2
image=cv2.imread('plane.png')
border=cv2.copyMakeBorder(image,25,25,25,25,cv2.BORDER_REFLECT,value=1)
cv2.imshow('Work of art',border)
cv2.waitKey(0)
cv2.destroyAllWindows()