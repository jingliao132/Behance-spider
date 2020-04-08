## This script formats different images 
# such as PNG, GIF, RAW, BMP to JPEG
# and transform the color space to RBG
## Author: Chen Zitong, Liao Jing
## 2020-04-08

# !/usr/bin/env python
# coding: utf-8

from PIL import Image
import numpy as np
import imageio
import os

# --- func definition
def gif2png(im):
    try:
        i = 0
        while 1:
            im.seek(i) #加载gif图像序列中的第i帧
            imframe = im.copy()
            if i == 0:
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass

# convert all images in image_dir and save to image_dir_convert
def converimage(image_dir, image):
    im = Image.open(os.path.join(image_dir, image))  #返回一个Image对象
    image_name, _ = os.path.splitext(image)
    convert_dir = image_dir + '_convert'
    
    if not os.path.exists(convert_dir):
        print('Create diretory:  ' + convert_dir)
        os.mkdir(convert_dir)
    
    img_format = im.format  # 色彩空间转换之后，image.format会变成None
    if im.mode != 'RGB':
        im = im.convert('RGB') 

    if img_format == 'PNG':
        im.save(os.path.join(convert_dir, image_name +'.jpg'))
        
    elif img_format == 'RAW':
        rawData = np.fromfile(os.path.join(image_dir, image), dtype=np.float32)
        jpgData = rawData.astype(np.uint8)
        imageio.imwrite(os.path.join(convert_dir, image_name +'.jpg'), jpgData)
        
    elif img_format == 'GIF':
        gifimg = Image.open(os.path.join(image_dir, image))
        
        for i, frame in enumerate(gif2png(gifimg)):
            if i == 0: #只转换第一帧
                frame = frame.convert('RGB')
                frame.save(os.path.join(convert_dir, image_name + '.jpg'))
                
    elif img_format == 'BMP' or img_format == 'JPEG':
        im.save(os.path.join(convert_dir, image_name +'.jpg'))
        
    else:
        print('Dismiss Undefined Format ', image, im.format)

# --- end func definition

# --- script
image_dir = '/path/to/images'  # change to your directory of images

for root, dirs, files in os.walk(image_dir):
    # compatible with MacOS, remove hidden files such as .DS_store 
    image_files = list(filter(lambda f: not f.startswith('.'), files))
    for f in image_files:
        converimage(image_dir, f)
        
print("Done!")
