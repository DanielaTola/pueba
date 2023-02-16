import cv2
import os

pathVideo='F:/Nuevos videos/videos/VID_20220806_090030.mp4'
# Crear la carpeta para guardar los frames
folder_name = "F:/Nuevos videos/videos/Frames"

video = cv2.VideoCapture(pathVideo)
count = 0

while True:
    ret, frame = video.read()
    if not ret:
        break

    if count % 8 != 0:
        count += 1
        continue
    file_name = "IMG-011-%d.jpg" % count
    file_path = os.path.join(folder_name, file_name)

    cv2.imwrite(file_path, frame)
    count += 1
    
video.release()
