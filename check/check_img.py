#-*- coding:utf-8 -*-
import os
import sys
from PIL import Image
sys.path.append("..")
from preprocess.tools import get_files
# def is_valid_jpg(file_path):
# 	with open(file_path,'rb') as f:
# 		f.seek(-2, 2) 
# 		return f.read() == '\xff\xd9'
def is_valid_jpg(path):
    try:
        Image.open(path).load()	
    except:
        return False
    else:
        return True
def find_invalid_jpgs(data_path):
	print("start to check!")
	imgs = get_files(data_path, 'jpg')
	print("there are %d files !" %len(imgs))
	for img in imgs:
		if not is_valid_jpg(img):
			print(img)

if __name__ == "__main__":
	data_path = r'Y:\thesis\data'
	find_invalid_jpgs(data_path)