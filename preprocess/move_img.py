#-*- coding:utf-8 -*-
import os
import shutil
from tools import get_files, get_datetime
import sys
LOCATION_MAP = {"T0006":"hebei", "T0002":"henan", "T0001":"shandong",
                "XAM02":"neimenggu/XAM02","XAM03":"neimenggu/XAM03", "XAM05":"neimenggu/XAM05"}
def _mkdirs_by_time(name):
    year = name[0:4]
    month = name[4:6]
    day = name[6:]
    return os.path.join(year, month, day)
def move_img_by_day(xmls, data_path):
    files = get_files(data_path)
    names = [os.path.split(file)[-1].split('.')[0] for file in files]
    name_path = dict(zip(names,files))
    for xml in xmls:
            name = os.path.split(xml)[-1].replace(".xml","")
            location = xml.split('_')[0]
            if name not in name_path:
                    raise ValueError("your name of xml must consistent with your picture!")
            img_path = name_path[name]
            datetime = get_datetime(name)
            date_path = os.path.join(datetime[0:4], datetime[4:6], datetime[6:])
            location_path = LOCATION_MAP[location]
            save_path = os.path.join(save_dir, location_path, date_path)
            if not os.path.exists(save_path):
                    os.makedirs(save_path)
            print("move img  %s"% name_path[name])
            shutil.copy(name_path[name],save_path)
            print("move xml  %s"%xml)
            shutil.copy(xml, save_path)
def main(argvs):
    xml_path = argvs[1]
    img_path = argvs[2]
    xmls = get_files(xml_path, 'xml')
    move_img_by_day(xmls, img_path)
if __name__ == "__main__":
        argvs = sys.argv
        main(argvs)
