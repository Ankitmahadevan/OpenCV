# image Blurring
import cv2
import numpy as np

img = cv2.imread("lena.jpg")
cv2.imshow('Original Image',img)
cv2.waitKey(0)

#Averaging done by convolving the image with a normalize box filter
#This takes the pixels under the box and replace the central element
#Box size needs to odd and positive
blur = cv2.blur(img, (3,3))
cv2.imshow('Blur Image',blur)
cv2.waitKey(0)

#Insted of using Box filter use gaussinan kernel
Gaussian = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('Gaussian Blur Image',Gaussian)
cv2.waitKey(0)

#Take median of all the pixels under kernel area and central
#element is replaced with this median value
median = cv2.medianBlur(img, 5)
cv2.imshow('Median Blur Image',median)
cv2.waitKey(0)

#Bilateral is very effective in nose removal
bilateral = cv2.bilateralFilter(img, 9, 75, 75)
cv2.imshow('Bilateral Blur Image',bilateral)
cv2.waitKey(0)

cv2.destroyAllWindows()



