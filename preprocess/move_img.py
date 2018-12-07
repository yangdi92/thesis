#-*- coding:utf-8 -*-
import os
import shutil
from tools import get_files, get_datetime
import sys
LOCATION_MAP = {"T0006":"hebei", "T0002":"henan", "T0001":"shandong",
                "XAM02":"neimenggu/XAM02","XAM03":"neimenggu/XAM03", "XAM05":"neimenggu/XAM05"}
def _is_exist(save_dir, name,suffix = '.jpg'):
    tmp = os.path.join(save_dir, name, suffix)
    return os.path.exists(tmp)

def _mkdirs_by_time(name):
    year = name[0:4]
    month = name[4:6]
    day = name[6:]
    return os.path.join(year, month, day)
def move_img_by_day(xmls, data_path, save_dir):
    files = get_files(data_path,'jpg')
    print("there are %d images" % len(files))
    names = [os.path.split(file)[-1].split('.')[0] for file in files]
    name_path = dict(zip(names,files))
    print("start to move img")
    for xml in xmls:
            name = os.path.split(xml)[-1].replace(".xml","")
            location = name.split('_')[0]
            print(name)
            if name not in name_path:
                    raise ValueError("your name of xml must consistent with your picture!")
            img_path = name_path[name]
            datetime = get_datetime(name)
            date_path = os.path.join(datetime[0:4], datetime[4:6], datetime[6:])
            location_path = LOCATION_MAP[location]
            save_path = os.path.join(save_dir, location_path, date_path)
            if not os.path.exists(save_path):
                    os.makedirs(save_path)
            if not _is_exist(save_dir,name,'.jpg'):
                print("move img  %s"% name_path[name])
                shutil.copy(name_path[name],save_path)
            if not _is_exist(save_dir,name,'.jpg'):
                print("move xml  %s"%xml)
                shutil.copy(xml, save_path)
def main(argvs):
    print("this program is used for move image")
    xml_path = argvs[1]
    print(xml_path)
    img_path = argvs[2]
    print(img_path)
    save_dir = argvs[3]
    print(save_dir)
    if not os.path.exists(xml_path):
        raise ValueError("you must have xmls")
    #print("asdwsf")
    xmls = get_files(xml_path, 'xml')
    print("there are %d xmls " % len(xmls))
    move_img_by_day(xmls, img_path, save_dir)
if __name__ == "__main__":
        argvs = sys.argv
        main(argvs)
