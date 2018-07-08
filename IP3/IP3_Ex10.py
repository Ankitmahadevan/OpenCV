#Edge Detection
import cv2
import numpy as np

img = cv2.imread("lena.jpg",0)


height,width = img.shape


#Extract slop edges
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)


cv2.imshow('Original Image',img)
cv2.waitKey(0)

cv2.imshow('Sobel X Image',sobel_x)
cv2.waitKey(0)

cv2.imshow('Sobel Y Image',sobel_y)
cv2.waitKey(0)

sobel_Or = cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('Sobel or Image',sobel_Or)
cv2.waitKey(0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('Laplacian Image',laplacian)
cv2.waitKey(0)

#Canny Edge detection uses gradiant values as thresholds
canny = cv2.Canny(img, 20, 170)
cv2.imshow('Canny Edge', canny)
cv2.waitKey(0)

cv2.destroyAllWindows()
