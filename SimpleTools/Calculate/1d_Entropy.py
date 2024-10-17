import numpy as np
import cv2
import math
from tqdm import tqdm
import argparse
import os
import scipy

para = argparse.ArgumentParser()
para.add_argument('-p', '--path', type=str, dest='path', help='测算信息熵的图像目录')
para.add_argument('-s', '-save_path', type=str, dest='save_path', help='数据输出的目录')
para.add_argument('--f', '--format', type=str, dest='format', default='txt', help='保存的数据文件类型\n支持txt,mat')
opt = para.parse_args()


def entropy(img):
    ent = 0
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    num_of_gray = np.zeros(256)
    p_of_gray = np.zeros(256)
    width = img.shape[1]
    height = img.shape[0]
    for w in range(width):
        for h in range(height):
            num_of_gray[gray_img[h, w]] = num_of_gray[gray_img[h, w]] + 1
    k = width * height
    for i in range(len(num_of_gray)):
        p_of_gray[i] = num_of_gray[i] / k
        if p_of_gray[i] == 0:
            ent = ent
        else:
            ent = ent - p_of_gray[i] * math.log(p_of_gray[i]) / math.log(2.0)
    return ent


if __name__ == '__main__':
    ent_dic = {}
    mean_ent = 0
    for f in tqdm(os.listdir(opt.path)):
        if os.path.isdir(opt.path + '\\' + f):
            continue
        temp_ent = entropy(cv2.imread(opt.path + '\\' + f))
        ent_dic.update({f: temp_ent})
        mean_ent = mean_ent + temp_ent  # 1.求和
    mean_ent = mean_ent / len(ent_dic)  # 2.均值
    print('mean entropy:', mean_ent)
    print('结果已保存')
    if not os.path.exists(opt.save_path):
        os.mkdir(opt.save_path)
    if opt.format == 'txt':
        with open(opt.save_path + r'\entropy_res.txt', 'w') as file:
            for key in ent_dic:
                file.writelines('"' + str(key) + '": ' + str(ent_dic[key]))
            file.write('\n Mean Calculate : ' + str(mean_ent))
            file.close()
    elif opt.format == 'mat':
        scipy.io.savemat(opt.save_path + r'\entropy_res.mat', {'entropy': ent_dic, 'mean_entropy': mean_ent})
