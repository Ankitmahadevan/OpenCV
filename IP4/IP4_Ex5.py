import cv2
import numpy as np

img = cv2.imread("image3.jpg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Original",img)
cv2.waitKey(0)

ret, thresh  = cv2.threshold(gray, 127, 255, 1)
_,contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for cnt in contours:

    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)

    if len(approx) == 3:
        shape_name = "Traiangle"
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)

        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(img, shape_name,(cx-50,cy),cv2.FONT_HERSHEY_SIMPLEX,
                    1,(0,0,0),1)
