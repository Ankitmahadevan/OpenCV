# create a black image
import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)

img_1 = np.zeros((512,512), np.uint8)

img_2 = 255* (np.ones((512,512), np.uint8))

cv2.imshow('Black Rectangle (Color)', img)
cv2.imshow('Black Rectangle (B&W)', img_1)
cv2.imshow('Black Rectangle (B&W)', img_2)

cv2.waitKey(0)
cv2.destroyAllWindows()