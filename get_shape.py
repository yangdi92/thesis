#-*- coding:utf-8 -*-
import cv2
import os
import sys
from preprocess.tools import get_files
import xml.etree.cElementTree as ET

def get_shape(img_path):
	imgs = get_files(img_path, 'jpg')
	print("there are %d imgages in total !"%len(imgs))
	#img_shape = {}
	for img in imgs:
		height, width, _ = cv2.imread(img).shape
		print(img)
		xml_path = img.replace('jpg','xml')
		tree = ET.ElementTree(file=xml_path)
		tree.find('./size/width').text = str(int(width))
		tree.find('./size/height').text = str(int(height))
		tree.write(xml_path)

if __name__ == "__main__":
	img_path = r"Y:\thesis\data"
	get_shape(img_path)





