#-*- coding:utf-8 -*-
import os
import sys
import shutil
from tools import get_files

def make_dataset (path, save_dir):
    xmls = get_files(path,'xml')
    imgs = get_files(path,'jpg')
    if len(xmls) != len(imgs):
        raise ValueError("you should make sure that your quality of xmls is same as imgs!")
    for i in range(len(xmls)):
        save_xmls = os.path.join(save_dir, "Annotations")
        if not os.path.exists(save_xmls):
            os.makedirs(save_xmls)
        print(xmls[i])
        shutil.copy(xmls[i], save_xmls)
        save_imgs = os.path.join(save_dir, "JPEGImages")
        if not os.path.exists(save_imgs):
            os.makedirs(save_imgs)
        print(imgs[i])
        shutil.copy(imgs[i], save_imgs)

def main(argvs):
    path = argvs[1]
    save_dir = argvs[2]
    make_dataset(path, save_dir)

if __name__ == "__main__":
    argvs = sys.argv
    main(argvs)
