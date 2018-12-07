#-*- coding:utf-8 -*-
import os
from tools import get_files
from splitimg import splitImg
from splitxml import splitXml

def _split(img_path, xml_path):
	xmls = get_files(xml_path, 'xml')
	imgs = get_files(img_path, 'jpg')

	if len(xmls) != len(imgs):
		raise ValueError("the quality of images and xml must be same!")
	for i in range(len(xmls)):
		save_dir = "/".join(os.path.split(xmls[i])[0:-1])
		save_dir = save_dir.replace("data",'splitdata')
		if not os.path.exists(save_dir):
			os.makedirs(save_dir)
		print(xmls[i])
		splitXml(xmls[i],save_dir)

		save_dir = "/".join(os.path.split(imgs[i])[0:-1])
		save_dir = save_dir.replace("data",'splitdata')
		#print(save_dir)
		#raise ValueError("break")
		if not os.path.exists(save_dir):
			os.makedirs(save_dir)
		print(imgs[i])
		#print(save_dir)
		splitImg(imgs[i],save_dir)
		

if __name__ == "__main__":
	img_path = "Y:\\thesis\\data"
	xml_path = "Y:\\thesis\\data"
	_split(img_path, xml_path)

