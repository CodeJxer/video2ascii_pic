# -*- coding=UTF-8 -*-

from PIL import Image
im = Image.open('in.jpg')                                           #打开图片
width = im.size[0]                                                     
height = im.size[1]
print width, height

new_width = width / 8
new_height = height / 8

im = im.convert('L').resize((new_width, new_height), Image.ANTIALIAS);       #将原图改为灰度图并重设大小
im.save('res.jpg')                                                           #存下处理后的图片
charset = '.,_+!:"<>(){}?/;[]^F\*@#$A'
#print len(charset)
txt = ''

for m in range(0, new_height):
    for n in range(0, new_width):
        pixel = im.getpixel((n, m))
        txt += charset[pixel / 10]
        txt += charset[pixel / 10]
    txt += '\n'

print txt