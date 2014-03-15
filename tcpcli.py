#!/usr/bin/env python

import socket
#from socket import *
import numpy as np
from array import*
import pickle
import cv
import cv2
import sys

capture = cv.CaptureFromCAM(0)
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
#MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
frame = cv.QueryFrame(capture)
img=np.asarray(frame[:,:])
#print sys.getsizeof(img)
L=pickle.dumps(img)
s.send(L)
data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
