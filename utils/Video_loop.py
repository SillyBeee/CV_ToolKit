import cv2
import numpy as np

def video_loop(video_path , output_path , repeat_time):
    cap = cv2.VideoCapture(video_path)
    total_fps = int(cap.get(cv2.CAP_PROP_FPS));
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    Video_writer = cv2.VideoWriter(output_path, fourcc, total_fps, (frame_width, frame_height))
    for i in range(repeat_time):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                Video_writer.write(frame)
            else:
                break
    cap.release()
    Video_writer.release()
if __name__ == '__main__':
    video_path = "/home/ma/桌面/remote_shoot_videos/cut.mp4"
    output_path = "/home/ma/桌面/remote_shoot_videos/lo.mp4"
    repeat_time = 4
    video_loop(video_path, output_path, repeat_time)
