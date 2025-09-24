import cv2
planet=cv2.imread('planet.jpg')
cv2.imshow('Original image',planet)
cv2.waitKey(0)
greyscale=cv2.cvtColor(planet,cv2.COLOR_BGR2GRAY)
cv2.imshow('Greyscale image',greyscale)
cv2.waitKey(0)
cv2.destroyAllWindows()