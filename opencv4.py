import cv2
import numpy as np
shade1=np.array([191,177,94])
shade2=np.array([164,199,187])
image1=np.full((300,300,3),shade1,dtype=np.uint8)
image2=np.full((300,300,3),shade2,dtype=np.uint8)
#res=cv2.add(image1,image2)
res=image1+image2
cv2.imshow('Shade',res)
cv2.waitKey(0)
cv2.destroyAllWindows()