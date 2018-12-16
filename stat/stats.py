#-*- coding:utf-8 -*-
import os
from preprocess.tools import get_files
import xml.etree.cElementTree as ET
import sys
import numpy as np
import cv2
def get_stats(path):
    xmls = get_files(path)
    labels = {}
    for xml in xmls:
            tree = ET.ElementTree(file=xml)
            names = [k.text for k in tree.findall("/object/name")]
            for name in names:
                    if name not in labels:
                            labels[name] = 1
                    else:
                            labels[name] += 1
    for key, value in labels.items():
            print(key, "\t", value)
def _sum_rgb(imgs):
    r = 0
    g = 0
    b = 0
    for img in imgs:
           img_mat = cv2.imread(img)
           b_chanel, g_chanel, r_chanel = cv2.split(img_mat)
           b += b_chanel.sum()
           g += g_chanel.sum()
           r += r_chanel.sum()
    return r, g, b

def get_mean_of_rgb(path, njob=1):
    imgs = get_files(path,'jpg')
    nums_img = len(imgs)
    block = nums_img // njob
    pool = Pool(processes=njob)
    res = []
    for k in njob:
            if k != njob - 1:
                   #imgs_tmp = nums_img[k*block:(k+1)*block]
                  res.append( pool.apply_async(_sum_rgb, (imgs[k*block:(k+1)*block], )))
            else:
                  res.append(pool.apply_async(_sum_rgb, (imgs[k*block:], )))
    if len(res) != njob:
            raise ValueError("some error!")
    r = 0
    g = 0
    b = 0
    for k in res:
            r += k[0]
            g += k[1]
            b += k[2]
    return r/nums_img, g/nums_img, b/nums_img

    
if __name__ == "__main__":
        get_stats(sys.argv[1])
