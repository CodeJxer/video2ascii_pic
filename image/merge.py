openpath = ''
savepath = ''
txt = ''
for i in range(400, 505):
	openpath = 'image' + str(i) + '.txt'
	fo = open(openpath, 'r')
	txt += fo.read()
	fo.close()

savepath = 'merge4.txt'
f = open(savepath, 'w')
f.write(txt)
f.close()