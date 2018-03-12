import os
from PIL import Image


def resize_icon():
	for f in files:
		path = os.path.join(rootdir, f)
		f_ex = os.path.splitext(path)[1]
		f_n = os.path.splitext(f)[0]
		r = os.path.join(rootdir, 'result')
		if os.path.isdir(path):
			print('存在文件夹')
			pass
		if not os.path.exists(r):
			os.mkdir(r)
			print('创建文件夹')
			pass
		if f_ex == '.png':
			h = f_n[0 : 1]
			name = f_n[-1] 
			# print(h)
			if name == 'a':
				name = '1'
			elif name == '0':
				name = '10'
			elif name == 'j':
				name = '11'
			elif name == 'q':
				name = '12'
			elif name == 'k':
				name = '13'

			f_name = format_str(h, name)
			with Image.open(f) as img:
				res = img.resize((60, 90), Image.ANTIALIAS)
				res.save('%s/%s.png' % (r, f_name))
			pass
		pass

	pass

def format_str(h, n):
	if h == 's':
		return f('1', n)
	elif h == 'h':
		return f('2', n)
	elif h == 'c':
		return f('3', n)
	elif h == 'd':
		return f('4', n)
	pass

def f(num, n):
	if int(n) >= 10:
		return num + n
	else:
		return  num +'0' + n		
	pass

if __name__ == '__main__':
	rootdir = os.getcwd()
	files = os.listdir(rootdir)
	resize_icon()

# index = len('src_images_gamelayer_ba_betarea_language')
# for f in files:
# 	f_e = os.path.splitext(f)[1]
# 	if f_e == '.png':
# 		name = f[index : ]
# 		# print(name)
# 		with Image.open(f) as img:
# 		    icon = img.crop((17, 47, 17 + 177, 47 + 40))
# 		    icon.save(name)
# 		pass
	
# 	pass


