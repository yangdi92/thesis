#-*- coding:utf-8 -*-
import os
import xml.etree.cElementTree as ET
import copy
import sys
# def generateXml():
#     pass
def splitXml(path, save):
    tree = ET.ElementTree(file=path)
    filename = tree.find("filename").text.split(".")[0]
    template = ET.Element("annotation")
    tmp = [k for k in tree.getroot() if k.tag != "object"]
    template.extend(tmp)
    size = tree.find("size")
    x = int(size.find("width").text)
    y = int(size.find("height").text)
    xmid = int(x/2)
    ymid = int(y/2)
    points = [(0,0), (xmid, 0), (0, ymid), (xmid, ymid)]
    sizes = [(xmid-1, ymid), (x - xmid, ymid), (xmid,y - ymid), (x - xmid, y - ymid)]
    xml1 = []
    xml2 = []
    xml3 = []
    xml4 = []
    for obj in tree.findall("object"):
            xmin = int(obj.find("bndbox/xmin").text)
            xmax = int(obj.find("bndbox/xmax").text)
            ymin = int(obj.find("bndbox/ymin").text)
            ymax = int(obj.find("bndbox/ymax").text)
            if xmin >= 0 and xmax < xmid and ymin >= 0 and ymax < ymid:
                    xml1.append(obj)
            elif xmin >= xmid and xmax <= x and ymin >= 0 and ymax < ymid:
                    obj.find("bndbox/xmin").text = str(xmin - xmid)
                    obj.find("bndbox/xmax").text = str(xmax - xmid)
                    xml2.append(obj)
            elif xmin >= 0 and xmax < xmid and ymin >= ymid and ymax <= y:
                    obj.find("bndbox/ymin").text = str(ymin - ymid)
                    obj.find("bndbox/ymax").text = str(ymax - ymid)
                    xml3.append(obj)
            elif xmin >= xmid and xmax <= x and ymin >= ymid and ymax <= y:
                    obj.find("bndbox/xmin").text = str(xmin - xmid)
                    obj.find("bndbox/xmax").text = str(xmax - xmid)
                    obj.find("bndbox/ymin").text = str(ymin - ymid)
                    obj.find("bndbox/ymax").text = str(ymax - ymid)
                    xml4.append(obj)
            else:
                   pass
    xmls = [xml1, xml2, xml3, xml4]
    for k in range(len(xmls)):
            root = copy.deepcopy(template)
            tmpfile = filename + "_img%d"%(k+1) + ".jpg"
            root.find("filename").text = tmpfile
            width, height = sizes[k]
            root.find("size/width").text = str(width)
            root.find("size/height").text = str(height) 
            root.extend(xmls[k])
            newtree = ET.ElementTree(root)
            savedir = os.path.join(save, tmpfile.replace('.jpg', ".xml"))
            newtree.write(savedir)
def main(argvs):
    datapath = argvs[1]
    filenames = os.listdir(datapath)
    savepath = argvs[2]
    for filename in filenames:
            filename = os.path.join(datapath,filename)
            splitXml(filename, savepath)
if __name__ == "__main__":
    argvs = sys.argv
    main(argvs)
