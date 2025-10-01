import cv2
car=cv2.imread('vroom.png')
edges=cv2.Canny(car,100,200)
cv2.imwrite('Coolcar.jpg',edges)
cv2.imshow('EDGEDetection',edges)
cv2.waitKey(0)
cv2.destroyAllWindows()