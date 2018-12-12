#-*- coding:utf-8 -*-
import os
from preprocess.tools import get_files
import xml.etree.cElementTree as ET

def check_bboxes(path):
	tree = ET.ElementTree(file=path)
	width = float(tree.find('./size/width').text)
	height = float(tree.find('./size/height').text)
	objs = tree.findall('./object')
	invalid_bboxes = []
	for obj in objs:
		xmin = float(obj.find('./bndbox/xmin').text)
		xmax = float(obj.find('./bndbox/xmax').text)
		ymin = float(obj.find('./bndbox/ymin').text)
		ymax = float(obj.find('./bndbox/ymax').text)
		if xmin < 0.0 or xmax > width or ymin < 0 or ymax >height:
			# print([xmin, xmax, ymin, ymax])
			invalid_bboxes.append([xmin, xmax, ymin, ymax])
	return invalid_bboxes, [width,height]
def format_bbox(bndbox):
	return '\t'.join([str(k) for k in bndbox])
def find_invalid_xmls(data_dir):
	xmls = get_files(data_dir,suffix='xml')
	print("there are %d files need to check"%len(xmls))
	#valid_xmls = []
	for xml in xmls:
		invalid_bboxes,info = check_bboxes(xml)
		if len(invalid_bboxes) > 0:
			print(xml)
			print(info)
			#print(len(invalid_bboxes))
			for bndbox in invalid_bboxes:
				print(format_bbox(bndbox))
			
if __name__ == "__main__":
	data_dir = r'Y:\thesis\data'
	print("satrt to check bouding box")
	find_invalid_xmls(data_dir)
	# valid_xmls = find_valid_xmls(data_dir)
	# for xml in valid_xmls:
	# 	print(xml)

