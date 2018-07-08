import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)


cv2.putText(img, 'Vishwajeet', (55,290), cv2.FONT_HERSHEY_COMPLEX,
            2, (100,170,0), 3)

cv2.imshow('Text',img)

cv2.waitKey(0)
cv2.destroyAllWindows()