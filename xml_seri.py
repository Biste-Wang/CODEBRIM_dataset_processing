#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import xml.etree.ElementTree as ET # 导入ElementTree模块


def prettyXml(element, indent, newline, level=0):  # elemnt为传进来的Elment类，参数indent用于缩进，newline用于换行
    if element:  # 判断element是否有子元素
        if element.text == None or element.text.isspace():  # 如果element的text没有内容
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
            # else:  # 此处两行如果把注释去掉，Element的text也会另起一行
    # element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
    temp = list(element)  # 将elemnt转成list
    for subelement in temp:
        if temp.index(subelement) < (len(temp) - 1):  # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            subelement.tail = newline + indent * level
        prettyXml(subelement, indent, newline, level=level + 1)  # 对子元素进行递归操作
    return element


ann_root = r'./VOCdevkit/VOC2007'
ann_path = os.path.join(ann_root, 'Annotations_trans')  # xml文件所在路径
ann_save_path = os.path.join(ann_root, 'Annotations_seri') # 美化后xml文件保存地址

for filename in os.listdir(ann_path):
    xml_path = os.path.join(ann_path, filename)
    xml_save_path = os.path.join(ann_save_path, filename)

    tree = ET.parse(xml_path) # 解析xml文件
    root = tree.getroot() # 得到根元素，Element类
    root = prettyXml(root, '\t', '\n') # 执行美化方法
    # ET.dump(root)  # 打印美化后的结果
    tree = ET.ElementTree(root)  # 转换为可保存的结构
    tree.write(xml_save_path)  # 保存美化后的结果
