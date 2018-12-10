#-*- coding:utf-8 -*-
import os
from preprocess.tools import get_files
import xml.etree.cElementTree as ET
import sys
def get_stats(path):
    xmls = get_files(path)
    labels = {}
    for xml in xmls:
            tree = ET.ElementTree(file=xml)
            names = [k.text for k in tree.findall("/object/name")]
            for name in names:
                    if name not in labels:
                            labels[name] = 1
                    else:
                            labels[name] += 1
    for key, value in labels.items():
            print(key, "\t", value)

if __name__ == "__main__":
        get_stats(sys.argv[1])
