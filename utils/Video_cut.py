import cv2

def capture_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        cv2.imshow('Video', frame)

        if cv2.waitKey(50) & 0xFF == 27:  # ESC key
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_path = '/home/ma/桌面/remote_shoot_videos/remoteshoot.mp4'
    
    output_path = '/home/ma/桌面/remote_shoot_videos/cut.mp4'
    capture_video(input_path, output_path)