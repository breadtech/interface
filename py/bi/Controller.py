##
# title = Controller.py
# by = Brian Kim
# description = the breadinterface controller
#  manages a frame (view) and the actions that should
#  trigger changes in some model
#

class Controller():
  def __init__( self, window, title, frame_info=Frame.DefaultFrameInfo, main_view=DefaultView ):
  	self.title = title 
    self.frame = Frame( window, title, frame_info )
    self.gtk()

  def gtk( self ):
    self.frame.gtk(window)

  def segue( self, mode, target ):