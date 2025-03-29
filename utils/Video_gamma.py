import cv2
import numpy as np
final_gamma=0
def adjust_gamma(image, gamma):
    if (gamma < 100):
        inv_gamma=gamma/100
    else:
        inv_gamma=1+(gamma-100)/100
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

def write_video(final_gamma):
     cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
     while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            writer.write(adjust_gamma(frame,final_gamma))
        else:
            break


def nothing(x): pass
cv2.namedWindow("Trackbars")
cv2.createTrackbar("gamma", "Trackbars", 0, 800, nothing)

input_path = "/home/ma/桌面/remote_shoot_videos/lo.mp4"
output_path = "/home/ma/桌面/remote_shoot_videos/cut.mp4"

cap = cv2.VideoCapture(input_path)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
writer= cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while True:
    ret,image = cap.read()
    if not ret or image is None:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret,image = cap.read()
    gamma = cv2.getTrackbarPos("gamma", "Trackbars")
    adjust_gamma(image, gamma)
    cv2.imshow("Gamma", adjust_gamma(image, gamma))

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            final_gamma=gamma
            write_video(final_gamma)
            break
cap.release()
writer.release()
cv2.destroyAllWindows()
print("Write success")
