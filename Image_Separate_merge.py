# -*- coding: utf-8 -*-
# 分离真彩图的三个通道并合并
import cv2
import numpy as np

# 读入图片
img = cv2.imread("F:/Python/pythonWorkspace/ShawOpencvLearning/pythonOpencvLearning/lena.bmp")
# 分离三通道
b,g,r = cv2.split(img)
print(type(b))

cv2.imshow("Red", r)
cv2.imshow("Green", g)
cv2.imshow("Blue", b)
# 合并三通道
# 蓝色通道 img[:,:,0]
# 绿色通道 img[:,:,1]    
# 红色通道 img[:,:,2]
# merge函数中b,g,r 顺序不能变，如果变了，和不成原来的图像
merge = cv2.merge([b,g,r])
cv2.imshow("Merge", merge)
cv2.waitKey(0)