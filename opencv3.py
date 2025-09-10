import cv2
mountain=cv2.imread('mountain.jpg')
planet=cv2.imread('planet.jpg')
res=cv2.addWeighted(mountain,0.4,planet,0.8,0)
res=cv2.add(mountain,planet)
sub=cv2.subtract(mountain,planet)
cv2.imshow('Combine',sub)
cv2.waitKey(0)
cv2.destroyAllWindows()