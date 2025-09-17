import cv2
plane=cv2.imread('plane.png')
resize=cv2.resize(plane,(500,600))
cv2.imshow('Plen',resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
