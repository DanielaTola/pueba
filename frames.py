import cv2
import os

folder_name = "F:/Nuevos videos/videos" 

files = os.listdir(folder_name)
video_files = [f for f in files if f.endswith(".mp4") or f.endswith(".avi")]

frames_folder = "F:/Nuevos videos/videos/Frames"

for file in video_files:
    file_path = os.path.join(folder_name, file)

    video = cv2.VideoCapture(file_path)
    count = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        if count % 8 != 0:
            count += 1
            continue
        frame_file_name = "IMG-0%d.jpg" % count
        frame_file_path = os.path.join(frames_folder, frame_file_name)
        cv2.imwrite(frame_file_path, frame)
        count += 1
    video.release()
