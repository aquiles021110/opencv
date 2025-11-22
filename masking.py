import cv2
import numpy as np
import time
raw_vid=cv2.VideoCapture('video.mp4')
time.sleep(1)
background=0
count=0
for i in range(60):
    return_val,background=raw_vid.read()
    if return_val==False:
        continue