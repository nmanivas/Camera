#!/usr/bin/env python

import sys, os
import pygtk, gtk, gobject
import pygst
pygst.require("0.10")
import gst
import time

is_init=False
player = gst.Pipeline("player")
source = gst.element_factory_make("filesrc")
source.set_property("location", "/home/anas/abc.jpg")
udpsink = gst.element_factory_make("udpsink")
udpsink.set_property('port', 30000)
player.set_state(gst.STATE_PLAYING)
while True:
	time.sleep(0.05)
