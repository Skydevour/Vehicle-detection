#-*- coding:utf-8 -*- 
# @Time : 2021/2/10 22:12 
# @Author : 万志杨
# @File : jpgM.py 
# @Software: PyCharm

import glob

import cv2

print(glob.glob(r"./images/*.jpg"))

import os
img_prefix = ['jpg', 'jpeg', 'png']

def read():
    files = os.listdir("D:\学习\深度学习从入门到实践\吴恩达深度学习\汽车检测\images")
    for file in files:
        index = file.find(".")
        prefix = file[index + 1:]
        if prefix in img_prefix:
            print(file)

read()
