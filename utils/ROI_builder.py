import cv2
import numpy as np


image = np.zeros((1024,1280), dtype=np.uint8)
test_image = cv2.imread("/home/ma/桌面/remote_shoot_videos/lo.mp4")
mid = (640, 512)
length = 200
height = 200

x_start = mid[0] - length//2
y_start = mid[1] - height//2
x_end = mid[0] + length//2
y_end = mid[1] + height//2

image = cv2.rectangle(image, (mid[0]-length//2, mid[1]-height//2), (mid[0]+length//2, mid[1]+height//2), (255, 255, 255), -1)
roiimage = image[y_start:y_end, x_start:x_end]
cv2.imshow("roiimage", roiimage)
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()