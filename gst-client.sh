#!/bin/bash

DEVICE=
HOST=
PORT=

usage() {
	echo -e "$0 [-d <device>] [-h <host-ip>] [-p <port>]"
	exit 1
}

launch() {
	gst-launch 						\
	v4l2src device=$DEVICE 				\
	! 'video/x-raw-yuv,width=640,height=480' 		\
	!  x264enc pass=qual quantizer=20 tune=zerolatency 	\
	! rtph264pay						\
	! udpsink host=$HOST port=$PORT
}

while getopts ":d:h:p:" opt; do
	case $opt in
		d)
			$DEVICE=$OPTARG
		;;
		h)
			$HOST=$OPTARG
		;;
		p)
			$HOST=$OPTARG
		;;
		\?)
			echo "Unknown argument -$OPTARG" >&2
			usage
		;;
		:)
			echo "-$OPTARG requires an argument!" >&2
			usage
		;;
	esac
done

if [ -z "$DEVICE" ]; then
	echo "Using default device /dev/video0"
	DEVICE=/dev/video0
fi

if [ -z "$HOST" ]; then
	echo "host: 127.0.0.1"
	HOST=127.0.0.1
fi

if [ -z "$PORT" ]; then
	echo "port: 30000"
	PORT=30000
fi

launch
