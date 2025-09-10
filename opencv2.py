import cv2
umbrella=cv2.imread('umbrella.png',)
print(umbrella.shape)
b,g,r=cv2.split(umbrella)
print('='*50)
print(b.shape)
cv2.imshow('Blue',b)
cv2.imshow('Red',r)
cv2.imshow('Green',g)
#if cv2.waitKey(0):
    #cv2.destroyAllWindows()
