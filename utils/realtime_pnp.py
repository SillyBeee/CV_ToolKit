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


camera_matrix = np.array([[1.01807009e+03,0.00000000e+00 ,6.34366118e+02],
                        [0.00000000e+00 ,1.01298212e+03, 3.06666555e+02],
                        [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

dist_coeffs = np.array([[ 5.85300629e-02 ,-5.14895013e-01 ,-1.33529702e-04 ,-9.09679581e-03, 9.21326154e-01]])
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

mask_in_reailty = [(0,0),(450,0),(0,700),(450,700)]
mask_in_camera = [(0,0),(0,0),(0,0),(0,0)]

cap = cv2.VideoCapture(0)
while True: 
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1024,960))
    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        

        # _,thres = cv2.threshold(gray, 190, 255, cv2.THRESH_BINARY)
        cv2.imshow("thres", mask)
        cv2.waitKey(1)
        

