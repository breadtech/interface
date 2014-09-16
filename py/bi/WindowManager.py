##
# title: WindowManager.py
# by: Brian Kim
# description: the window manager object
# 

import pygtk
pygtk.require('2.0')
import gtk

class WindowManager():
  def __init__( self ):
  	self.window = gtk.Window()