# -*- coding: utf-8 -*-
import cv2

# 读取图片
img = cv2.imread("F:/Python/pythonWorkspace/ShawOpencvLearning/pythonOpencvLearning/lena.bmp")
# 创建窗口并显示图片
cv2.namedWindow("Image")
cv2.imshow("Image", img)
# 不添这一句，在IDLE中执行窗口直接无响应。在命令行中执行的话，则是一闪而过。
cv2.waitKey(0)
# 释放窗口
cv2.destroyAllWindows() 