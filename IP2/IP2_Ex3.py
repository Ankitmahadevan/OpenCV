import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv2.imshow('Original Image', img)
cv2.rectangle(img,(100,100),(300,250),(0,255,0), -1)  #-1

cv2.imshow('Rectangle',img)

cv2.waitKey(0)
cv2.destroyAllWindows()