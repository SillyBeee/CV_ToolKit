import cv2
import numpy as np
def nothing(x): pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 35, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 50, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 50, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 85, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)

cap = cv2.VideoCapture("/home/ma/桌面/remote_shoot_videos/longer.mp4")

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("L-H", "Trackbars")
    ls = cv2.getTrackbarPos("L-S", "Trackbars")
    lv = cv2.getTrackbarPos("L-V", "Trackbars")
    uh = cv2.getTrackbarPos("U-H", "Trackbars")
    us = cv2.getTrackbarPos("U-S", "Trackbars")
    uv = cv2.getTrackbarPos("U-V", "Trackbars")
    lower = np.array([lh, ls, lv])
    upper = np.array([uh, us, uv])
    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow("Mask", mask)
    cv2.waitKey(100)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break