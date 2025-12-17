import cv2
vid=cv2.VideoCapture('hwy.mp4')
carcascade=cv2.CascadeClassifier('cars.xml')
while True:
    ret,frame=vid.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=carcascade.detectMultiScale(grey,1.3,1)
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Video2',frame)
    if cv2.waitKey(33)==27:
        break
cv2.destroyAllWindows()