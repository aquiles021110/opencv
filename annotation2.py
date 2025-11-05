import cv2
image3=cv2.imread('hehe.jpg')
image3=cv2.rectangle(image3,(100,100),(200,200),(255,255,255),5)
image3=cv2.line(image3,(100,100),(150,50),(255,255,255),5)
image3=cv2.line(image3,(200,100),(150,50),(255,255,255),5)
cv2.imshow('Thing',image3)
cv2.waitKey(0)
cv2.destroyAllWindows()