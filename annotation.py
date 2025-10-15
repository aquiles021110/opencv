import cv2
#line
image=cv2.imread('ilfaittarpinchaud.png')
image2=cv2.imread('truck.JPG')
spoint=(0,0)
epoint=(250,250)
colour=(255,255,255)
thickness=5
'image=cv2.line(image,spoint,epoint,colour,thickness)'
#rectangle & circle
'''image2=cv2.circle(image2,(500,500),30,(14,62,0),6)
image2=cv2.rectangle(image2,(0,100),(400,300),(0,0,0),-5)'''
#  +thickness=lines -thickness=fill
#text
font=cv2.FONT_HERSHEY_DUPLEX
image=cv2.putText(image,'IL FAIT TARPIN CHAUD',(780,200),font,1,(100,100,100),5,cv2.LINE_AA)
'''cv2.imshow('Line',image)
cv2.imshow('Rect',image2)
cv2.imshow('Circle',image2)'''
cv2.imshow('Text',image)
cv2.waitKey(0)
cv2.destroyAllWindows()