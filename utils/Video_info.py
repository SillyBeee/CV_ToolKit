import cv2
import os

def get_video_info(video_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"The file {video_path} does not exist.")

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Unable to open video file {video_path}.")

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps if fps > 0 else 0
    bitrate = cap.get(cv2.CAP_PROP_BITRATE)
    codec = int(cap.get(cv2.CAP_PROP_FOURCC))
    codec_str = "".join([chr((codec >> 8 * i) & 0xFF) for i in range(4)])

    cap.release()

    video_info = {
        "Width": width,
        "Height": height,
        "FPS": fps,
        "Frame Count": frame_count,
        "Duration (s)": duration,
        "Bitrate": bitrate,
        "Codec": codec_str,
        "Resolution": f"{width}x{height}"
    }

    return video_info

def print_video_info(video_path):
    try:
        info = get_video_info(video_path)
        for key, value in info.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    video_path = "/home/ma/Hero_ws/videos/shoot2.mkv"
    print_video_info(video_path)