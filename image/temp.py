# -*- coding=UTF-8 -*-

from PIL import Image
openpath = ''
savepath = ''
for i in range(0, 505):
	openpath = 'image' + str(i) + '.jpg'
	savepath = 'image' + str(i) + '.txt'

	im = Image.open(openpath)                                           #打开图片
	width = im.size[0]    												#获取原图宽度                                                 
	height = im.size[1]													#获取原图高度
	#print width, height 												

	new_width = width / 9												#计算新的宽度
	new_height = height / 9												#计算新的高度

	im = im.resize((new_width, new_height), Image.ANTIALIAS);     	    #将原图重设大小
	#im.save('res.jpg')                                                 #存下处理后的图片
	charset = '.,_+!:"<>(){}?/;[]^F\*@#$A'								#字符集
	#print len(charset)
	txt = ''		

	for m in range(0, new_height):										#遍历图片的每个像素点
	    for n in range(0, new_width):
	        pixel = im.getpixel((n, m))									#获取像素值
	       	pp = int(0.3 * pixel[0] + 0.6 * pixel[1]+ 0.1 * pixel[2])	#计算亮度
	        txt += charset[pp / 10]										#根据亮度映射到字符
	        txt += charset[pp / 10]		
	    txt += '\n'

	f = open(savepath, 'w')
	f.write(txt)
	f.close()