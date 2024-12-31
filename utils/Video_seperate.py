import cv2
import os

# 视频文件路径
video_path = "/home/ma/yolov5/bottle.mp4"

# 保存帧的文件夹
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

# 打开视频文件
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("无法打开视频文件！")
    exit()

frame_count = 0
while True:
    # 读取一帧
    ret, frame = cap.read()
    if not ret:  # 如果没有更多帧
        break

    # 保存帧到文件
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)
    print(f"保存帧 {frame_count} 到 {frame_filename}")
    frame_count += 1

# 释放视频捕获对象
cap.release()
print("视频帧提取完成！")
