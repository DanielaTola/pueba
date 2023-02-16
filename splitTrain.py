import os
import random
import cv2
import numpy as np
from PIL import Image

src_dir = 'F:/Nuevos videos/videos/TrainResNet/data completa/ETAPA4-NORMALIZE'
dst_dir = 'F:/Nuevos videos/videos/TrainResNet/data completa/NewTrain-Img/ETAPA4'


img_list = os.listdir(src_dir)

selected_imgs = random.sample(img_list, 122)
count=0

for img_name in selected_imgs:
    count=count+1
    img = Image.open(os.path.join(src_dir, img_name))
    # Renderizar la imagen
    #img = img.resize((256, 256), Image.ANTIALIAS)
    # Normalizar la imagen
    #img = (np.array(img) / 255.0).astype(np.float32)
    new_name = 'IMG-ETAPA-04-0'+str(count)+'.jpg'
    print("Image:"+new_name)
    img.save(os.path.join(dst_dir, new_name))
