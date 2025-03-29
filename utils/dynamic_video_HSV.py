import cv2
import numpy as np
def nothing(x): pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 32, 180, nothing)

cv2.createTrackbar("L-S", "Trackbars", 20, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 216, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 85, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 216, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 245, 255, nothing)

cap = cv2.VideoCapture("/home/ma/桌面/remote_shoot_videos/looong.mp4")

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
    frame = cv2.resize(frame, (640, 480))
    mask = cv2.resize(mask, (640, 480))
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.waitKey(100)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break