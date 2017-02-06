# -*- coding=UTF-8 -*-

#author: 	codejxer
#email:		1055223464@qq.com
#date:		2017-2-6 18:40:09

import cv2
import numpy as np

c = 1
cap = cv2.VideoCapture('your_name.mp4')
while(cap.isOpened()):
	ret, frame = cap.read()

	cv2.imshow('capture', frame)
	cv2.imwrite('image//image' + str(c / 5) + '.jpg', frame)
	
	c += 1

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

