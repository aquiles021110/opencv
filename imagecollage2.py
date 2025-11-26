import cv2
from PIL import Image
import os
os.chdir('c:\\Users\\chris\\Desktop\\VSCODE\\OpenCV\\images2')
path='c:\\Users\\chris\\Desktop\\VSCODE\\OpenCV\\images2'
meanheight=0
meanwidth=0
numimages=len(os.listdir('.'))
for image in os.listdir('.'):
    img=Image.open(os.path.join(path,image))
    width,height=img.size
    meanwidth+=width
    meanheight+=height
meanwidth=meanwidth//numimages
meanheight=meanheight//numimages
for image in os.listdir('.'):
    if image.endswith('.jpg') or image.endswith('.jpeg') or image.endswith('.png'):
        img=Image.open(os.path.join(path,image))
        width,height=img.size
        print(width,height)
        resizedimage=img.resize((meanwidth,meanheight),Image.LANCZOS)
        resizedimage.save(image,'JPEG',quality=95)
        print(img.filename.split('\\')[-1],'is resized')
def VideoGenerator():
    vidname='Collage.avi'
    os.chdir('c:\\Users\\chris\\Desktop\\VSCODE\\OpenCV\\images2')
    images=[]
    for image in os.listdir('.'):
        if image.endswith('.jpg') or image.endswith('.jpeg') or image.endswith('.png'):
            images.append(image)
    print(images)
    frame=cv2.imread(os.path.join('.',images[0]),0)
    height,width=frame.shape
    video=cv2.VideoWriter(vidname,0,1,(width,height))
    for image in images: 
        video.write(cv2.imread(os.path.join('.',image)))
    cv2.destroyAllWindows()
    video.release()
VideoGenerator()