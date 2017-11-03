#!/usr/bin/python
# -*- coding=utf-8 -*-
# 老虎机滚动gif效果制作


import os
import random
from PIL import Image


def get_infos(s):
	global width
	i = 0
	for f in files:
		fl = os.path.join(rootdir, f)
		f_e = os.path.splitext(fl)[1];
		if os.path.isdir(fl):
			pass
		elif f_e == '.png' and s == 0:
			with Image.open(f) as img:
				w = img.size[0]
				hs.append(img.size[1])
				if w > width:
					width = w
					pass
		elif f_e == '.png' and s == 1:
			with Image.open(f) as img:
				img_w = int(img.size[0])
				img_h = int(img.size[1])
				re = img.crop((0, 0, img_w, img_h))
				x = int(comp.size[0]/2 - img_w/2)
				y = 20 * i + sum(hs[:i])
				middle = y + img_h/2
				cutIndexs.append(y)
				cutIndexs.append(middle)
				comp.paste(re, (x, y))
			i = i + 1
	pass


def cut(img):
	num = 50
	for x in range(0, len(cutIndexs)):
		index = int(cutIndexs[x])
		if index + 410 <= img.size[1]:
			icon = img.crop((0, index, img.size[0], index + 410))
			icon.save('%s/%s.png' % (result_dir, num))
			num = num - 1
			pass
		pass
	pass


if __name__ == '__main__':
	rootdir = os.getcwd()
	files = os.listdir(rootdir)
	for x in range(1,6):
		width = 0
		hs = []
		cutIndexs = []
		random.shuffle(files)  
		dir = '%s/ani_%s' % (rootdir, x)
		os.mkdir(dir)
		result_dir = dir
		get_infos(0)		
		h = sum(hs) + (len(hs) - 1) * 20
		comp = Image.new('RGBA', (width, h), (225, 0, 0, 0))
		get_infos(1)
		cut(comp)
		pass
	
	
