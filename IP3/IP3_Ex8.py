#Image Denoising Non-Local Denoising
import cv2
import numpy as np

img = cv2.imread("lena.jpg")
cv2.imshow('Original Image',img)
cv2.waitKey(0)

dst = cv2.fastNlMeansDenoisingColored(img, None, 6, 6, 7, 21)

cv2.imshow("Fast Mean Denosing",dst)
cv2.waitKey(0)

cv2.destroyAllWindows()