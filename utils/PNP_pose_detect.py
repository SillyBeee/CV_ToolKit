import cv2
import numpy as np
import os
camera_matrix = np.array([[1.01807009e+03,0.00000000e+00 ,6.34366118e+02],
                        [0.00000000e+00 ,1.01298212e+03, 3.06666555e+02],
                        [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])

dist_coeffs = np.array([[ 5.85300629e-02 ,-5.14895013e-01 ,-1.33529702e-04 ,-9.09679581e-03, 9.21326154e-01]])


def find_corner_points(image):
    