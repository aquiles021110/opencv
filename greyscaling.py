import cv2
planet=cv2.imread('planet.jpg')
cv2.imshow('Original image',planet)
greyscale=cv2.cvtColor(planet,cv2.COLOR_BGR2GRAY)
cv2.imshow('Greyscale image',greyscale)
#greyscale on different image
weather=cv2.imread('ilfaittarpinchaud.png')
noweather=cv2.cvtColor(weather,cv2.COLOR_BGR2GRAY)
cv2.imshow('ITS HOT',noweather)
#using averaging of pixels method to greyscale the image
img=cv2.imread('truck.JPG')
(row,col)=img.shape[0:2]
for i in range(row):
    for j in range(col):
        #find the average of the bgr pixel values
        img[i,j]=sum(img[i,j])*0.33
cv2.imshow('Greyscaled',img)
#rotating an image
car=cv2.imread('vroom.png')
(row,col)=car.shape[0:2]
m=cv2.getRotationMatrix2D((col/2,row/2),45,1)
final=cv2.warpAffine(car,m,(col,row))
cv2.imshow('Car',final)
cv2.waitKey(0)
cv2.destroyAllWindows()