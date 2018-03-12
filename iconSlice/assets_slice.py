#!/usr/bin/python
# -*- coding=utf-8 -*-
# 查找图集.png文件对应的.xml 或 .html文件并解析，根据解析到的信息切割图集中的icon

# pip 安装模块的问题
# 如 pip install Pillow  默认安装在 python2.7的目录下 python3就无法使用
# 解决：
# 运行 python3 -m pip install Pillow

import os
import json
from xml.etree import ElementTree as ET
from PIL import Image
from html.parser import HTMLParser


# class WPHTMLParser(HTMLParser):
#     """docstring for WPHTMLParser"""
# 	def __init__(self):
# 		HTMLParser.__init__(self)
# 		self.rects = []
# 	def handle_starttag(self, tag, attrs):
# 		if tag == 'char':
# 			rect = {}
# 			if len(attrs) == 0:
# 				pass
# 			else:
# 				for k, v in attrs:
# 					if k == 'id':
# 						rect['name'] = v
# 					if k == 'x':
# 						rect['x'] = int(v)
# 					if k == 'y':
# 						rect['y'] = int(v)
# 					if k == 'width':
# 						rect['w'] = int(v)
# 					if k == 'height':
# 						rect['h'] = int(v)
# 			self.rects.append(rect)
# 			pass
# 		pass


def search_file():
	for f in os.listdir(rootdir):
		folder = os.path.join(rootdir, f)
		if os.path.isdir(folder):
			pass
		else:
			f_ext = os.path.splitext(f)[1]
			if f_ext == '.atlas':
				modify_atlas(f)
				pass
			if f_ext == '.png':
				f_png = os.path.splitext(f)[0]
				p = os.path.join(rootdir, f_png)
				if not os.path.exists(p):#若不存在对应的存储路径 则创建
					os.mkdir(p)
					# print(p)
					pass
				cut_round(p, f)
				# for file in os.listdir(rootdir): # 找到.png文件后  需要再遍历该目录以查找对应的配置文件
				# 	f_info = os.path.splitext(file)[0]
				# 	f_infoe = os.path.splitext(file)[1]
				# 	if f_info == f_png and f_infoe == '.xml':
				# 		xml_parser(p, f, file)
				# 		pass
				# 	if f_info == f_png and f_infoe == '.html':
				# 		html_parser(p, f, file)
				# 		pass
				# 	if f_info == f_png and f_infoe == '.json':
				# 		json_parser(p, f, file)
				# 		pass
# 手动计算图标区域 直接裁剪
def cut_round(p, f):
	print('目标存储路径：%s' % (os.listdir(p)))
	if len(os.listdir(p)) > 1:
		print('%s 目录下已经存在.png文件，请检查' % p)
	else:
		print('正在裁剪：%s ...' % f)
		with Image.open(f) as im:
			for i in range(0,10):
				x = 14 + 140*i
				rect = (x, 14, x + 114, 14 + 114)
				img = im.crop(rect)
				img.save('%s/%s.png' % (p, i+1))
				pass
			
	pass

def xml_parser(p, f, file):
	print('目标存储路径：%s' % (os.listdir(p)))
	if len(os.listdir(p)) > 1:
		print('%s 目录下已经存在.png文件，请检查' % p)
	else:
		print('正在裁剪：%s ...' % f)
		with Image.open(f) as im:
			tree = ET.parse(file)
			root = tree.getroot()
			for node in root.iter('SubTexture'):
				name = node.attrib['name']
				img = im.crop(icon_rect(node))
				img.save('%s/%s.png' % (p, name))


def html_parser(p, f, file):
	print('目标存储路径：%s' % (os.listdir(p)))
	if len(os.listdir(p)) > 1:
		print('%s 目录下已经存在.png文件，请检查' % p)
	else:
		print('正在裁剪：%s ...' % f)
		with Image.open(f) as im:
			with open(file) as data:
				html_p.feed(data.read())
				for r in html_p.rects:
					rect = (r['x'], r['y'], r['x'] + r['w'], r['y'] + r['h'])
					# print(rect)
					img = im.crop(rect)
					img.save('%s/%s.png' % (p, r['name']))
					pass
	pass

def json_parser(p, f, file):
	print('目标存储路径：%s' % (os.listdir(p)))
	if len(os.listdir(p)) > 1:
		print('%s 目录下已经存在.png文件，请检查' % p)
	else:
		print('正在裁剪：%s ...' % f)
		with Image.open(f) as im:
			with open(file, 'r') as f_json:
				d = json.loads(f_json.read())
				for k, value in d['res'].items():
					# v = value['frame']
					rect = (value['x'], value['y'], value['x'] + value['w'], value['y'] + value['h'])
					img = im.crop(rect)
					print(p, k)
					img.save('%s/%s.png' % (p, k))
					pass

	pass

def icon_rect(node):
	x = int(node.attrib['x'])
	y = int(node.attrib['y'])
	w = int(node.attrib['w'])
	h = int(node.attrib['h'])
	rect = (x, y, x+w , y+h)
	# print(rect)
	return rect
	pass

# Laya 引擎图集动画.atlas文件默认情况下每一张图片的位置x、y都是0；
# 如果每张图片大小不一样，动画播放过程中会产生向右或下伸缩的现象；
# 该函数实现将每一张图片都居中的功能
def modify_atlas(file):
	with open(file, 'r') as json_file:
		d = json.loads(json_file.read())
		for k, value in d['frames'].items():
			w = value['spriteSourceSize']['w']
			# x = 250 - (w - 67) 荷官往左伸手
			x = 250 - 67 #荷官往左伸手
			value['spriteSourceSize']['x'] = x
			pass
		save_json_file(file, d)		
	pass

def save_json_file(file, data):
	with open(file, 'w') as json_file:
		json_file.write(json.dumps(data))
	pass

if __name__ == '__main__':
	rootdir = os.getcwd()
	print ('当前文件夹：%s' % rootdir)
	# html_p = WPHTMLParser()
	search_file()
	# html_p.close()
	print('************** 裁剪完成 *************')

	
	
