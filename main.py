# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 19:14:31 2022

@author: 42208
"""

import cv2 #opencv读取的格式是BGR
import numpy as np
import matplotlib.pyplot as plt#Matplotlib是RGB

def cv_show(name,img): #定义一个展示图片的函数
    cv2.imshow(name,img) 
    cv2.waitKey(0) 
    cv2.destroyAllWindows()    
img=cv2.imread('example.png',cv2.IMREAD_COLOR) #读入图片

lower_color = (0, 60, 60)
upper_color = (6, 255, 255) #设置颜色过滤的阈值
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #将rgb图片转换为hsv图片
mask_img = cv2.inRange(hsv_img, lower_color, upper_color) #对转换的hsv图片进行颜色通道过滤
kernel = np.ones((3,3),np.uint8)          #设置膨胀操作所需的3x3矩阵
mask_img = cv2.dilate(mask_img,kernel,iterations = 5)  #对二值图片进行膨胀操作
#cv_show('img',mask_img)
contours, hierarchy = cv2.findContours(mask_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE) #寻找区域最小外接矩形
x,y,w,h = cv2.boundingRect(contours[0]) #得出横、纵坐标和矩阵的宽、高
X=x-w/2
Y=y+h/2
text = "X:"+str(X)+" " + "Y:"+str(Y) + " "
cv2.putText(img, text, (40, 50), cv2.FONT_HERSHEY_PLAIN, 2.0, (0, 0, 255), 2)#将文字打印在图片上
img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
#cv_show('img',img)
cv2.imwrite("output.png",img)

