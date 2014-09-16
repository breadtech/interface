##
# title: Frame.py
# by: Brian Kim
# description: 
#  - class that defines the container for the bars
#  - defines subclasses called BareFrame (one bar),
#     MenuFrame (two bar), and ActionFrame (three bar)
#

import GtkWrapper

class Frame(breadinterface,GtkWrapper):

  ##
  # the inner info class
  #
  class FrameInfo():
    def __init__( self, n_bars, bars ):
      self.n_bars = n_bars
      self.top = bar_info[0]
      self.middle = bar_info[1]
      self.bottom = bar_info[2]

  ##
  # constructing the frame
  #
  def __init__( self, window, title, frame_info ):

    GtkWrapper.__init__( self, window, )
    self.n = frame_info.n_bars
    self.top = Bar( frame_info.top )
    if self.frame_info.middle:
      self.middle = Bar( frame_info.middle )
    if self.frame_info.bottom:
      self.bottom = Bar( frame_info.bottom )
    self.gtk()

  ##
  # setting up the frame with gtk
  #
  def gtk( self ):
    self.top.gtk()
    if self.middle:
      self.middle.gtk()
    if self.bottom:
      self.bottom.gtk()

  ##
  # cleanup 
  # 
  def cleanup( self ):
    pass

  ##
  # start
  #
  def start( self ):
    pass

  ##
  #



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
    
