##
# title = bi.Controller.py
# by = Brian Kim
# description = this module contains all classes
#   related to the breadinterface controller
#

class BIController():
  def segue( self, mode, target ):

  def __init__( self, title, frameInfo, mainView ):
    self._title = title
    self._frame = BIFrame( frameInfo )
    self._main = mainView