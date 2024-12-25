import cv2
import numpy as np
import os
pic = cv2.imread("img/src.jpg")
pic = cv2.resize(pic, (1024,960))
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7,7), 0)

_,thres = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow("thres", thres)
for contour in contours:
    if cv2.contourArea(contour) > 1000:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        cv2.drawContours(pic, [approx], -1, (0,255,0), 3)

cv2.imshow("output", pic)
cv2.waitKey(20000)
cv2.destroyAllWindows()