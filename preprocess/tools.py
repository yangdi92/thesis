#-*- coding:utf-8 -*-
import os

def get_files(path,suffix="xml"):
    files = []
    for root, dirs, files in os.walk(path):
            if len(files) > 0:
                    for file in files:
                            if file.endswith(suffix):
                                    tmp = os.path.join(root,file)
                                    files.append(tmp)
    return files

def get_datetime(names):
    return names.split("_")[-2][0:8]

