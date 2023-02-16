import os
import random
import shutil

src_dir = 'F:/Nuevos videos/videos/TrainResNet/data completa/NewTrain-Img/TEST&TRAIN/TRAIN/ETAPA4'
dst_dir = 'F:/Nuevos videos/videos/TrainResNet/data completa/NewTrain-Img/TEST&TRAIN/TEST/ETAPA4'

def move_10_percent_files(src_directory, dst_directory):
    files = os.listdir(src_directory)
    number_of_files = len(files)
    ten_percent_files = int(number_of_files * 0.1)
    selected_files = random.sample(files, ten_percent_files)
    for file in selected_files:
        src_path = os.path.join(src_directory, file)
        dst_path = os.path.join(dst_directory, file)
        shutil.move(src_path, dst_path)

move_10_percent_files(src_dir, dst_dir)