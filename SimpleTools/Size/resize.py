import cv2
import os
import argparse
from tqdm import tqdm


para = argparse.ArgumentParser()
para.add_argument('-path', type=str, dest= 'path', help='想要调整尺寸的图片目录')
para.add_argument('-Size', type=int, dest= 'Size', default=500, help='调整的图片尺寸宽度，默认500')
opt = para.parse_args()


def resize(path, height):
    if not os.path.exists(path+'\\'+'resized'):
        os.mkdir(path+'\\'+'resized')
    for f in tqdm(os.listdir(path)):
        if os.path.isdir(path + '\\' + f):
            continue
        img = cv2.imread(path + '\\' + f)
        width = int(height * img.shape[0] / img.shape[1])
        img = cv2.resize(img, (height, width))
        cv2.imwrite(path+'\\'+'resized\\'+f, img)


if __name__ == '__main__':
    print(opt.path, opt.size)
    resize(opt.path, opt.size)
