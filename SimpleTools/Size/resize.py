import cv2
import os
import argparse
from tqdm import tqdm


para = argparse.ArgumentParser()
para.add_argument('-path', type=str, dest='path', help='想要调整尺寸的图片目录')
para.add_argument('-save_path', type=str, dest='save_path', default='origin', help='调整后保存到的图片目录,'
                                                                                   'origin为保存到输入目录下的resized文件夹')
para.add_argument('-w', '--width', type=int, dest='width', default=500, help='调整的图片尺寸宽度，默认500,-1为根据宽度锁定比例')
para.add_argument('--height', type=int, dest='height', default=-1, help='调整的图片尺寸宽度，默认-1,意为根据高度锁定比例锁定比例')
opt = para.parse_args()


def resize(path, save_path, width, height):
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    for f in tqdm(os.listdir(path)):
        if os.path.isdir(path + '\\' + f):
            continue
        img = cv2.imread(path + '\\' + f)
        if opt.height == -1:
            height = int(width * img.shape[0] / img.shape[1])
        elif opt.width == -1:
            width = int(height * img.shape[1] / img.shape[0])
        if opt.height == -1 and opt.width == -1:
            print('目标图像宽高不能都设置为-1，请重新设置')
            break
        img = cv2.resize(img, (width, height))
        cv2.imwrite(save_path + '\\' + f, img)


if __name__ == '__main__':
    print(' 处理目录：', opt.path, '\n',
          '目标目录', opt.save_path, '\n',
          '目标尺寸', opt.width, opt.height)
    if opt.save_path == 'origin':
        opt.save_path = opt.path + '\\resized'
    resize(opt.path, opt.save_path, opt.width, opt.height)
