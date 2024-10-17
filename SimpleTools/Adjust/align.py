import cv2
import os
import argparse
from tqdm import tqdm

para = argparse.ArgumentParser()
para.add_argument('-rpath', type=str, dest='rpath', help='尺寸对齐的参照目录')
para.add_argument('-ppath', type=str, dest='ppath', help='待处理图片的目录')
para.add_argument('-opath', type=str, dest='opath', default='origin', help='对其后图片的输出目录，默认在处理目录的aligned目录下')
opt = para.parse_args()


def size_align(rpath, ppath, opath):
    if opath == 'origin':
        opath = ppath + '\\' + 'aligned'
    if not os.path.exists(opath):
        os.mkdir(opath)
    for f in tqdm(os.listdir(rpath)):
        if os.path.isdir(rpath + '\\' + f) or os.path.isdir(ppath + '\\' + f):
            continue
        rimg = cv2.imread(rpath + '\\' + f)
        pimg = cv2.imread(ppath + '\\' + f)
        pimg = cv2.resize(pimg, (rimg.shape[1], rimg.shape[0]))
        cv2.imwrite(opath + '\\' + f, pimg)
        print(f)
        print('rfile ', str(rimg.shape[0]), str(rimg.shape[1]))
        print('pfile ', str(pimg.shape[0]), str(pimg.shape[1]))


if __name__ == '__main__':
    print('参照目录:', opt.rpath, '处理目录:', opt.ppath, '输出目录:', opt.opath)
    size_align(opt.rpath, opt.ppath, opt.opath)
