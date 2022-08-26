#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import xml.etree.ElementTree as ET  # 读取xml
import os


def parse_rec(filename):
    """
    解析xml文件 获取object节点的信息
    """
    tree = ET.parse(filename)  # 解析读取xml函数
    root = tree.getroot()
    objects = []
    for obj in root.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        obj_struct['difficult'] = int(obj.find('difficult').text)

        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text),
                              int(bbox.find('ymin').text),
                              int(bbox.find('xmax').text),
                              int(bbox.find('ymax').text)]

        defect = obj.find('Defect') # 背景 裂缝 剥落 风化 露筋 腐蚀（色斑）
        defect_list = list(filter(None,['Background' if int(defect.find('Background').text)==1 else None,
                                'Crack' if int(defect.find('Crack').text)==1 else None,
                                'Spallation' if int(defect.find('Spallation').text)==1 else None,
                                'Efflorescence' if int(defect.find('Efflorescence').text) == 1 else None,
                                'ExposedBars' if int(defect.find('ExposedBars').text) == 1 else None,
                                'CorrosionStain' if int(defect.find('CorrosionStain').text) == 1 else None]))
        obj_struct['defect'] = defect_list

        objects.append(obj_struct)
    return objects


def renew_xml(objects,filename):
    tree = ET.parse(filename)  # 解析读取xml函数
    root = tree.getroot()

    # 删除原object节点
    for object in root.findall('object'):
        root.remove(object)

    # 新增新object节点
    for i in objects:
        for j in range(len(i['defect'])):
            obj_proj = ET.Element('object')

            obj_name = ET.Element('name')
            obj_name.text = str(i['defect'][j])

            obj_diff = ET.Element('difficult')
            obj_diff.text = str(i['difficult'])

            obj_bbox = ET.Element('bndbox')
            box_xmin = ET.Element('xmin')
            box_xmin.text = str(i['bbox'][0])
            box_ymin = ET.Element('ymin')
            box_ymin.text = str(i['bbox'][1])
            box_xmax = ET.Element('xmax')
            box_xmax.text = str(i['bbox'][2])
            box_ymax = ET.Element('ymax')
            box_ymax.text = str(i['bbox'][3])
            obj_bbox.extend([box_xmin,box_ymin,box_xmax,box_ymax])

            obj_proj.extend([obj_name,obj_diff,obj_bbox])
            root.append(obj_proj)
    tree.write(filename,encoding='utf-8',xml_declaration=True)


ann_root = r'./VOCdevkit/VOC2007'
ann_path = os.path.join(ann_root, 'Annotations_trans')  # xml文件所在路径

for filename in os.listdir(ann_path):
    xml_path = os.path.join(ann_path, filename)
    my_object = parse_rec(xml_path)
    renew_xml(my_object,xml_path)