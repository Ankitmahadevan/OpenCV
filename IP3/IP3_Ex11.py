import cv2
import numpy as np

def sketch(image):
    #Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #Cleanup image using gaussian blur
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)

    #Extract Edges
    canny_edges = cv2.Canny(img_gray_blur, 10, 70)

    #Do an invert binarize the image
    ret, mask = cv2.threshold(canny_edges,70,255,cv2.THRESH_BINARY)
    return mask

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('Our Live Sketch', sketch(frame))
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()