'''
Created on May 6, 2014

@author: guru
'''

import socket
import struct
import math

header_size = 20

frame_id = 0

def send(data, server_ip, port):
    global frame_id
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    buffer_size = 64000 - header_size
    num_chunks  = math.ceil(len(data) / buffer_size)
    for chunk_id in range(0, num_chunks):
        header = struct.pack("!IQQ" + str(buffer_size) + "s", len(data), frame_id, chunk_id, data)
        sock.sendto(header, (server_ip, port))
    frame_id += 1
        
