#-*- coding:utf-8 -*-
import os
import sys
sys.path.append("..")
from preprocess.tools import get_files

def check(data_dir):
	imgs = get_files(data_dir, 'jpg')
	xmls = get_files(data_dir, 'xml')

	xmls_set = set([xml.replace(".xml", "") for xml in xmls])
	imgs_set = set([img.replace(".jpg", "") for img in imgs])

	diff = imgs_set.difference(xmls_set)
	print(len(diff))
	#print('\n'.join(list(diff)[0:5]))

if __name__ == "__main__":
	data_dir = r"Y:\thesis\data"
	check(data_dir)
