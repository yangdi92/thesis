#-*- coding:utf-8 -*-
#import os
import xml.etree.cElementTree as ET

class Xml(object):
	def __init__(self):
		self.root = generate_base_xml()
	def add_bdbox(self, label, box):
		obj = ET.Element("object")
		name = ET.Element("name")
		name.text = label
		pose = ET.Element("pose")
		pose.text = "Unspecified"
		truncated = ET.Element("truncated")
		truncated.text = "0"
		difficult = ET.Element("diffcult")
		difficult.text = '0'
		bndbox = ET.Element("bndbox")
		xmin = ET.Element("xmin")
		xmin.text = str(box[0])
		xmax = ET.Element("xmax")
		xmax.text = str(box[2])
		ymin = ET.Element("ymin")
		ymin.text = str(box[1])
		ymax = ET.Element("ymax")
		ymax.text = str(box[3])
		bndbox.extend([xmin, xmax, ymin, ymax])
		obj.extend([name, pose, truncated, difficult, bndbox])
		self.root.append(obj)
def generate_base_xml():
	#tree = ET.ElementTree()
    root = ET.Element("annotation")
    folder = ET.Element("folder")
    filename = ET.Element('filename')
    path = ET.Element("path")
    source = ET.Element("source")
    database = ET.Element("database")
    database.text = "Unknown"
    source.append(database)
    size = ET.Element("size")
    width = ET.Element("width")
    #width.text = 0
    size.append(width)
    height = ET.Element("height")
    #height.text = 0
    size.append(height)
    depth = ET.Element("depth")
    size.append(depth)
    #depth.text = 0
    segmented = ET.Element("segmented")
    segmented.text = 0
    
    root.extend([folder, filename, path, source, size, segmented])
    #root.find("filename").text = "test.jpg"
    return root