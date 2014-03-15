import cv
import cv2
import numpy as np
import os
from subprocess import call
#import pickel
import re
#import msvcrtile
while(1):
	stream=os.popen("ls /dev/video*")
	a= stream.read()
	#print a[1]

	b= a.split('\n')
	#arlen=len(b)
	i=0
	List=[]
	for device in b:
		x=re.findall(r'\d+',device)
		List=List+x

	print "Available Video Devices:\n"

	print List
	print "Type merge if you wanna use 2 streams"
	option=raw_input("Choose the Stream: ")
	if option in List:
		cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
		capture = cv.CaptureFromCAM(int(option))
		while(1):
			k=0
			frame = cv.QueryFrame(capture)
			img=np.asarray(frame[:,:])
			cv2.imshow('w1',img)
			k=cv2.waitKey(30)
			if k==27:
				del capture
				cv2.destroyAllWindows()
				break
			elif k==-1:
				continue
			else:
				print k


	

    	
    		
			
	







	












