import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

cv2.imshow('Original Image', img)
cv2.line(img,(0,0),(511,511),(255,127,0), 5)

cv2.imshow('Blue Line',img)

cv2.waitKey(0)
cv2.destroyAllWindows()