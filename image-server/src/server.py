'''
Created on May 6, 2014

@author: guru
'''

import socket
import struct

port = 30000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("127.0.0.1", port))

cur_frame_id = 0
cur_seq_id = 0
while True:
    message = sock.recv(64000)
    header = message[0:16]
    data = message[16:64000]
    frame_id, seq_id = struct.unpack("!QQ", header)
    if frame_id != cur_frame_id or seq_id != cur_seq_id:
        if frame_id < cur_frame_id:
            # Old frame..we don't care about it
            print 'Discarded packet :%d(%d)' % (frame_id, seq_id)
            continue
        elif frame_id == cur_frame_id:
            # We did not receive a particular seq
            print 'Did not receive %d(%d)' % (cur_frame_id, cur_seq_id)
            cur_seq_id += 1
        else:
            # We moved whole frame(s) forward
            print 'Did not receive frame :%d' % cur_frame_id
            cur_frame_id = frame_id
            cur_seq_id = 0
    else:
        if cur_seq_id == 3:
            cur_frame_id += 1
            cur_seq_id = 0
            print 'Received full frame :%d' % frame_id
        else:
            cur_seq_id += 1