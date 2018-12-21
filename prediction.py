#-*- coding:utf-8 -*-
import os
import math
import random

import numpy as np
import tensorflow as tf
import cv2
import xml.etree.cElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sys
sys.path.append('../')

from nets import ssd_vgg_300, ssd_common, np_methods
from preprocessing import ssd_vgg_preprocessing
from notebooks import visualization
from xml_template import Xml
slim = tf.contrib.slim

gpu_options = tf.GPUOptions(allow_growth=True)
config = tf.ConfigProto(log_device_placement=False, gpu_options=gpu_options)
#yangdi
#isess = tf.InteractiveSession(config=config)
sess = tf.Session(config=config)

#_CLASS_MAP = {}
def process_image(img, select_threshold=0.5, nms_threshold=.45, net_shape=(300, 300)):
    # Run SSD network.
    rimg, rpredictions, rlocalisations, rbbox_img = sess.run([image_4d, predictions, localisations, bbox_img],
                                                              feed_dict={img_input: img})
    # Get classes and bboxes from the net outputs.
    rclasses, rscores, rbboxes = np_methods.ssd_bboxes_select(
            rpredictions, rlocalisations, ssd_anchors,
            select_threshold=select_threshold, img_shape=net_shape, num_classes=21, decode=True)
    
    rbboxes = np_methods.bboxes_clip(rbbox_img, rbboxes)
    rclasses, rscores, rbboxes = np_methods.bboxes_sort(rclasses, rscores, rbboxes, top_k=400)
    rclasses, rscores, rbboxes = np_methods.bboxes_nms(rclasses, rscores, rbboxes, nms_threshold=nms_threshold)
    # Resize bboxes to original image shape. Note: useless for Resize.WARP!
    rbboxes = np_methods.bboxes_resize(rbbox_img, rbboxes)
    return rclasses, rscores, rbboxes

def pred_by_xml(img_path, savepath):
	img = cv2.imread(img_path)
	filename = os.path.split(img_path)[-1]
	height, width, depth = img.shape
	shape = img.shape
	xml_obj = Xml()
	xml_obj.root.find("./size/width").text = str(int(width))
	xml_obj.root.find("./size/height").text = str(int(height))
	xml_obj.root.find("./size/depth").text = str(int(depth))
	xml_obj.root.find("./folder").text = "test"
	xml_obj.root.find("./filename").text = filename
	xml_obj.root.find("./path").text = img_path
	rclasses, _, rbboxes = process_image(img)
	for label, box in zip(rclasses, rbboxes): 
		ymin, xmin = (int(bbox[0] * shape[0]), int(bbox[1] * shape[1]))
		ymax, xmax = (int(bbox[2] * shape[0]), int(bbox[3] * shape[1]))
		xml_obj.add_bdbox(str(label), [xmin, xmax, ymin, ymax])
	tree = ET.ElementTree(xml_obj.root)
	xml_name = filename.replace(".jpg", ".xml")
	save_path = os.path.join(savepath, xml_name)
	tree.write(save_path)
	#return tree
def pred_by_drawing(img_path, save_path):
	img = cv2.imread(img_path)
	*_, img_name = os.path.split(img_path)
	rclasses, rscores, rbboxes =  process_image(img)
	visualization.bboxes_draw_on_img(img, rclasses, rscores, rbboxes, visualization.colors_plasma)
	visualization.plt_bboxes(img, rclasses, rscores, rbboxes)
