#!/bin/bash
gst-launch 						\
v4l2src device=/dev/video0 				\
! 'video/x-raw-yuv,width=640,height=480' 		\
!  x264enc pass=qual quantizer=20 tune=zerolatency 	\
! rtph264pay						\
! udpsink host=127.0.0.1 port=1234
