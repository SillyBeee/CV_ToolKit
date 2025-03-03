import cv2
import numpy as np

def adjust_gamma(image, gamma):
    if (gamma < 100):
        inv_gamma=gamma/100
    else:
        inv_gamma=1+(gamma-100)/100
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)
def nothing(x): pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar("gamma", "Trackbars", 0, 300, nothing)
cap = cv2.VideoCapture("/home/ma/桌面/remote_shoot_videos/looong.mp4")
while True:
    _,image = cap.read()
    if image is None:
        break
    gamma = cv2.getTrackbarPos("gamma", "Trackbars")
    adjust_gamma(image, gamma)
    cv2.imshow("Gamma", adjust_gamma(image, gamma))
    cv2.waitKey(100)
    
    
