#import socket

import socket
import pickle
import cv
import cv2
import numpy as np
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
cv.NamedWindow("w1", cv.CV_WINDOW_AUTOSIZE)
conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    L = pickle.loads(data)
    cv2.imshow('Combine',L)
    #print "received data:", data
    conn.send(data)  # echo
conn.close()
