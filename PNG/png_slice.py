#!/usr/bin/python
# -*- coding=utf-8 -*-
# 查找图集.png对应的.xml文件并解析，根据解析到的信息切割图集中的icon
import os
from xml.etree import ElementTree as ET
from PIL import Image


def search_file():
	p_count = 0
	sucess = 0
	for f in os.listdir(rootdir):
		folder = os.path.join(rootdir, f)
		if os.path.isdir(folder):
			pass
		else:
			f_ext = os.path.splitext(f)[1]
			if f_ext == '.png':
				f_png = os.path.splitext(f)[0]
				p = os.path.join(rootdir, f_png)
				if not os.path.exists(p):#若不存在对应的存储路径 则创建
					os.mkdir(p)
					# print(p)
					p_count = p_count + 1
					print('创建第： %s 个，文件夹名称：%s' % p_count, f_png)
					pass
				for file in os.listdir(rootdir): # 找到.png文件后  需要再遍历该目录以查找对应的.xml文件
					f_info = os.path.splitext(file)[0]
					f_infoe = os.path.splitext(file)[1]
					if f_info == f_png and f_infoe == '.xml':
						if len(os.listdir(p)) == 0:
							with Image.open(f) as im: #存在匹配的.png 和 .xml文件才开始打开.png文件
								tree = ET.parse(file)
								root = tree.getroot()
								for node in root.iter('SubTexture'):
									x = int(node.attrib['x'])
									y = int(node.attrib['y'])
									w = int(node.attrib['width'])
									h = int(node.attrib['height'])
									name = node.attrib['name']
									rect = (x, y, x+w , y+h)
									# print(rect)
									img = im.crop(rect)
									img.save('%s/%s.png' % (p, name))
								sucess = sucess + 1
								print('裁剪成功：%s 个' % sucess)
							pass
						else:
							print('%s 目录下已经存在文件，请检查' % p)


if __name__ == '__main__':
	rootdir = os.getcwd()
	print ('当前文件夹：%s' % rootdir)
	search_file()
	
