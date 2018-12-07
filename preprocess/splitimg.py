#-*- coding:utf-8 -*-
"""
@author:yangdi
"""
import cv2
import numpy as np
import os
import sys
def splitImg(path, newPath):
    img = cv2.imread(path)
    x, y, _ = img.shape
    xmedian = int(x/2)
    ymedian = int(y/2)
    img1 = img[0:xmedian, 0:ymedian, :]
    img2 = img[xmedian:, 0:ymedian, :]
    img3 = img[0:xmedian, ymedian:, :]
    img4 = img[xmedian:, ymedian:, :]
    fileName = os.path.split(path)[-1]
    #print("file name is %s" %fileName)
    fileName = fileName.split(".")[0]
    imgs = [img1, img3, img2, img4]
    for k in range(4):
            subName = '_img%d'%(k+1)
            newName = fileName + subName + ".jpg"
            #print(newName)
            savePath = os.path.join(newPath,newName)
            #print(savePath)
            #raise ValueError("break")
            cv2.imwrite(savePath, imgs[k])

if __name__ == "__main__":
    path = sys.argv[1]
    newpath = sys.argv[2]
    splitImg(path,newpath)
