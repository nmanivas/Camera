#!/usr/bin/env python

import sys, os
import pygtk, gtk, gobject
import pygst
pygst.require("0.10")
import gst

class GTK_Main:
	
	def __init__(self):
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("Vorbis-Player")
		window.set_default_size(500, 200)
		window.connect("destroy", gtk.main_quit, "WM destroy")
		vbox = gtk.VBox()
		window.add(vbox)
		self.entry = gtk.Entry()
		vbox.pack_start(self.entry, False)
		self.button = gtk.Button("Start")
		vbox.add(self.button)
		self.button.connect("clicked", self.start_stop)
		window.show_all()
		
		self.player = gst.Pipeline("player")
		source = gst.element_factory_make("filesrc")
		src_pad = gst.PadTemplate("src", gst.PAD_SRC, gst.PAD_ALWAYS)
		player.srcpad = src_pad
		player.add_pad(player.src_pad)
		player.srcpad.push("000000")
		udpsink = gst.element_factory_make("udpsink")
		
		self.player.add(source, udpsink)

				self.player.set_state(gst.STATE_PLAYING)
GTK_Main()
gtk.gdk.threads_init()
gtk.main()

