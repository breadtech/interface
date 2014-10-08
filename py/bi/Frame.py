##
# title: Frame.py
# by: Brian Kim
# description: 
#  - class that defines the container for the bars
#  - defines subclasses called BareFrame (one bar),
#     MenuFrame (two bar), and ActionFrame (three bar)
#

import pygtk
pygtk.require('2.0')
import gtk

from breadinterface import lifecycle
from GtkWrapper import GtkWrapper

class Frame(lifecycle,GtkWrapper):

  ##
  # inner info class
  #
  class Info():
    def __init__( self, bars ):
      self.n = len(bars)
      if self.n < 1 or self.n > 3:
        raise Execption( 'invalid number of bar infos provided' )
      
      self.bars = bars

  ##
  # constructing the frame
  #
  def __init__( self, frame_info ):

    GtkWrapper.__init__( self, gtk.VBox() )
    
    # number of bars
    self.n = frame_info.n
  
    # list of bars
    self.bars = {}
    for i in range( self.n ):
      self.bars.append( Bar(frame_info.bars[i]) )
    
    # setup the gtk stuff
    self.gtk()

  ##
  # setting up the frame with gtk
  #
  def gtk( self ):
    for bar in self.bars:
      bar.gtk()
      self.obj.add( bar.obj )

  ##
  # cleanup 
  # 
  def cleanup( self ):
    for bar in self.bars:
      bar.cleanup()
    self.bars = None
    self.obj = None

  ##
  # start
  #
  def start( self ):
    for bar in self.bars:
      bar.start()

  ##
  # stop
  # 
  def stop( self ):
    for bar in self.bars:
      bar.stop()

  ##
  # pause
  #
  def pause( self ):
    for bar in self.bars:
      bar.pause()

  ##
  # resume
  #
  def resume( self ):
    for bar in self.bars:
      bar.resume()

  ##
  # update
  #
  def update( self ):
    for bar in self.bars:
      bar.update()

##
# BareFrame: the one bar frame class
# - use this for views that only need two
#   or less buttons
# - left button should be back or close
# - right button should be a confirmation
#
class BareFrame( Frame ):

  ##
  # inner info class
  #
  class BareFrameInfo( Frame.FrameInfo ):
    def __init__( self, left_button, title_button, center_button ):
      info = Bar.BarInfo( left_button, title_button, center_button )
      Frame.FrameInfo.__init__( self, 1, [ info, None, None ] )

  def __init__( self, window, title, left_button_info, right_button_info ):
    pass
    
