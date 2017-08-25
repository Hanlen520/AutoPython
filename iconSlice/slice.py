# 说明
# 在该文件夹下必须有要切的图集.png 和与其对应的.json文件
# 生成的icon自动保存到该目录下

import json
import os, sys
from PIL import Image

path = os.getcwd()
files = os.listdir(path) #列出文件夹下所有的目录与文件
for i in range(0,len(files)):
       p = os.path.join(path,files[i])
       f = files[i]
       if os.path.isfile(p):
       	n = os.path.splitext(p)[1]
       	if n == '.png':
       		im = Image.open(f)
       		pass
       	if n == '.json':
       		jsonFile = open(f,'r')
       		content = jsonFile.read()
       		dic = json.loads(content)
       		pass
# 取出所有图标的信息
# print(dic.keys())
info = dic['res']
for icon in info:
       x = info[icon]['x']
       y = info[icon]['y']
       w = info[icon]['w']
       h = info[icon]['h']
       region = (x, y, x + w, y + h)
       img = im.crop(region)
       img.save('%s.png' % (icon))
im.close()
jsonFile.close()


