#Object detection using contours
import cv2

img = cv2.imread("imgae2.jpg")
cv2.imshow("Original",img)
cv2.waitKey(0)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.waitKey(0)

#Find Canny Edge
edged  =cv2.Canny(gray, 30, 200)
cv2.imshow("Canny edged",edged)
cv2.waitKey(0)

#Finding Contours
_,contours, hierarchy = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
cv2.imshow("Canny edged after contouring",edged)
cv2.waitKey(0)

print("Number of contours found", str(len(contours)))

#Draw All Contours
cv2.drawContours(img,contours, -1, (0,255,0), 3)
cv2.imshow('Contours', img)
cv2.waitKey(0)

cv2.destroyAllWindows()