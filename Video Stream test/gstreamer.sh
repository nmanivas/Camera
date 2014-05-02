#!/bin/bash

DEVICE=
HOST=
PORT=
SRC=udpsrc
EXEC=

launch() {
	if [ "$EXEC" == "server" ]; then
		server_launch
	else
		client_launch
	fi
}

usage() {
	if [ -z "$EXEC" ]; then
		usage_base
	elif [ "$EXEC" == "server" ]; then
		usage_server
	else
		usage_client
	fi
}

usage_base() {
	echo -e "$0 [server|client] [-d <device>] [-h <host-ip>] [-p <port>]"
}

usage_server() {
	echo -e "$0 $EXEC [-p <port>]"
}

usage_client() {
	echo -e "$0 client [-d <device>] [-h <host-ip>] [-p <port>]"
}

client_launch() {
	gst-launch 						\
	v4l2src device=$DEVICE do-timestamp=true		\
	! videorate						\
	! 'video/x-raw-yuv,width=640,height=480,framerate=30/1'	\
	! jpegenc						\
	! udpsink host=$HOST port=$PORT
}

server_launch() {
	echo "using port: $PORT"
	gst-launch 				\
	$SRC port=$PORT 			\
	! jpegdec 				\
	! tee name=muxtee			\
	! queue2				\
	! videorate				\
	! 'video/x-raw-yuv,framerate=30/1'	\
	! ffmpegcolorspace			\
	! jpegenc				\
	! avimux				\
	! filesink location=test.avi muxtee.	\
	! queue					\
	! xvimagesink sync=false
}

if [ $# -lt 1 ]; then
	usage_base
	exit 1
fi

if [ "$1" == "server" ] || [ "$1" == "client" ]; then
	EXEC=$1
else
	echo "Unknown option $1"
	usage_base
	exit 1
fi

while getopts ":d:h:p:s:" opt ${@:2}; do
	case $opt in
		d)
			DEVICE=$OPTARG
		;;
		h)
			HOST=$OPTARG
		;;
		p)
			PORT=$OPTARG
		;;
		s)	SRC=$OPTARG
		;;

		\?)
			echo "Unknown argument -$OPTARG" >&2
			usage
			exit 1;
		;;
		:)
			echo "-$OPTARG requires an argument!" >&2
			usage
			exit 1;
		;;
	esac
done

if [ -z "$DEVICE" ] && [ "$EXEC" == "client" ]; then
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


if [ "$EXEC" ]; then
	launch
fi
