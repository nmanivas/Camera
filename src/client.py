'''
Created on May 6, 2014

@author: guru
'''

import socket
import struct
import time

server="127.0.0.1"
port=30000


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

header_size = 16
buffer_size = 64000 - 16
message = "Hello World"
for frame_id in range(0, 100):
    for seq_id in range(0, 4):
        data = message + "-" + str(frame_id) + "(" + str(seq_id) + ")"
        header = struct.pack("!QQ" + str(buffer_size) + "s", frame_id, seq_id, data)
        sock.sendto(header, (server, port))
        time.sleep(0.02)
        