##
# title = bi.Bar
# by = Brian Kim
# description = the view that contains the bars
#

import pygtk
pygtk.require('2.0')
import gtk

from breadinterface import lifecycle
from GtkWrapper import GtkWrapper

class Bar( lifecycle, GtkWrapper ):

  def __init__( self, left_button=None, middle_button=None, right_button=None ):
    GtkWrapper.__init__( self, gtk.Hbox() )

    # set the number of buttons
    self.n = 0
    if not left_button == None:
      self.n = self.n + 1 
    if not middle_button == None:
      self.n = self.n + 1 
    if not right_button == None:
      self.n = self.n + 1 
    
    # set the buttons
    self.left = left_button
    self.middle = middle_button
    self.right = right_button

    self.obj.set_size_request( 480, 88 )

  def gtk( self ):
    self.obj.pack_start( self.left.obj )
    self.obj.pack_start( self.middle.obj )
    self.obj.pack_start( self.right.obj )
  
  def cleanup( self ):
    self.left.cleanup()
    self.middle.cleanup()
    self.right.cleanup()
    self.obj = None

