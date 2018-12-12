#-*- coding:utf-8 -*-
import sys
sys.path.append("..")
import os
from preprocess.tools import get_files
import xml.etree.cElementTree as ET
def rename_file(data_dir):
	xmls = get_files(data_dir, 'xml')
	print("there are %d xmls" % len(xmls))

	for xml in xmls:
		tree = ET.ElementTree(file=xml)
		name = os.path.split(xml)[-1].replace(".xml", '.jpg')
		print(name)
		tree.find('./filename').text = name

		tree.write(xml)
if __name__ == "__main__":
	data_dir = r"Y:\thesis\data"
	rename_file(data_dir)