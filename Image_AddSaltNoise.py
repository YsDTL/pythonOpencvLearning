# -*- coding: utf-8 -*-
#给图像添加椒盐噪声

import cv2
import numpy as np
import sys


def AddSaltNoise(img, n):
    for k in range(n):
        # 产生随机行
        i = int(np.random.random() * img.shape[0])
        # 产生随机列
        j = int(np.random.random() * img.shape[1])
        # Python中灰度图的img.ndim = 2 而C++中灰度图图像的通道数img.channel() =1
        # 若为灰度图
        if img.ndim == 2:
            img[i,j] = 255
        # 若为真彩图，则每个通道都要赋值
        elif img.ndim == 3:
            img[i,j,0] = 255
            img[i,j,1] = 255
            img[i,j,2] = 255
    return img

if __name__ == '__main__':
    # 读取图片
    img = cv2.imread("C:/Users/Administrator/Pictures/2.bmp")
    # img.shape[0] 表示图像的高     img.shape[1]表示图像的宽
    # print(img.shape[0])
    # print(img.shape[1])
    saltImg = AddSaltNoise(img, 5000)
    cv2.imshow("SaltImage",saltImg)
    cv2.waitKey(0)
    cv2.destoryAllWindows()