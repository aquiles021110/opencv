import cv2
import os
pikabnw=cv2.imread('pokemon.png',0)
cv2.imshow('Pika B/W',pikabnw)
cv2.waitKey(0)
cv2.destroyAllWindows()
savedirec='C:/Users/chris/Desktop/OpenCV'
os.chdir(savedirec)
cv2.imwrite('pikab/w.png',pikabnw)
print('success save')