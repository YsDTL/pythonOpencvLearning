# -*- coding: utf-8 -*-
# 图像的创建以及图像的复制

import cv2
import numpy as np

# 新的OpenCV的接口中没有CreateImage接口。即没有cv2.CreateImage这样的函数。
# 如果要创建图像，需要使用numpy的函数（现在使用OpenCV-Python绑定，numpy是必装的）

# 读取图片
img = cv2.imread("F:/Python/pythonWorkspace/ShawOpencvLearning/pythonOpencvLearning/lena.bmp")
emptyImg = np.zeros(img.shape, np.uint8)
# 复制原有的图像来获得一副新图像
emptyImg2 = img.copy()
# 将图像转换为灰度图
emptyImg3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("EmptyImage", emptyImg)
cv2.imshow("Image", img)
cv2.imshow("EmptyImage2", emptyImg2)
cv2.imshow("EmptyImage3", emptyImg3)

cv2.waitKey(0)
cv2.destoryAllWindows()
