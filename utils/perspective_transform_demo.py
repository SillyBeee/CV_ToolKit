import cv2
import numpy as np
import os
def calculate_length(point1 , point2):
    return np.sqrt(np.sum(np.square(point1 - point2)))

def auto_sort(point1 , point2 , point3 , point4):
    len1 = calculate_length(point1 , point2)
    len3 = calculate_length(point2 , point3)
    if len1 > len3:
        return [point2 , point3 , point1 , point4]
    else:
        return [point2 , point1 , point3 , point4]

mask_in_reailty = [(0,0),(400,0),(0,850),(400,850)]
mask_in_camera = [(0,0),(0,0),(0,0),(0,0)]

pic = cv2.imread("img/src.jpg")
pic = cv2.resize(pic, (1024,960))
gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7,7), 0)

_,thres = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cv2.imshow("thres", thres)
for contour in contours:
    if cv2.contourArea(contour) > 1000:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        mask_in_camera = auto_sort(approx[0][0], approx[1][0], approx[2][0], approx[3][0])
        M = cv2.getPerspectiveTransform(np.float32(mask_in_camera), np.float32(mask_in_reailty))
        result = cv2.warpPerspective(pic, M, (400,850))
        cv2.drawContours(pic, [approx], -1, (0,255,0), 3)

cv2.imshow("output", pic)
cv2.imshow("result", result)
cv2.waitKey(20000)
cv2.destroyAllWindows()