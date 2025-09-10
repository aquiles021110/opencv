import cv2
#image=cv2.imread('pokemon.png',0)
image=cv2.imread('pokemon.png',cv2.IMREAD_COLOR)
cv2.imshow('Wow',image)
cv2.waitKey(0)
cv2.destroyAllWindows()