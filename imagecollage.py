import cv2
from PIL import Image
#pil is a image processing library
import os
os.chdir('c:\\Users\\chris\\Desktop\\VSCODE\\OpenCV\\images')
path='c:\\Users\\chris\\Desktop\\VSCODE\\OpenCV\\images'
meanheight=0
meanwidth=0
#os.listdir('.') this lists all files and images in current directory
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
