import cv2
trucks=cv2.imread('sunsetplane.png')
edges=cv2.Canny(trucks,80,50)
cv2.imshow('EDGEDetection',edges)

plane=cv2.imread('sunsetplane.png')
(row,col)=plane.shape[0:2]
m=cv2.getRotationMatrix2D((col/2,row/2),45,1)
final=cv2.warpAffine(plane,m,(col,row))
cv2.imshow('Planebutsideways',final)
cv2.waitKey(0)
cv2.destroyAllWindows()