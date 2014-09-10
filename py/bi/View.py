##
# title = bi.View.py
# by = Brian Kim
# description = this module contains all classes
#   related to the breadinterface view
#

import pygtk
pygtk.require('2.0')
import gtk

class BIButtonInfo():
  def __init__( self, label, action ):
    self.label = label
    self.action = action

class BIBarInfo():
  def __init__( self, left, center, right ):
    self.left = left
    self.center = center
    self.right = right

class BIFrameInfo():
  def __init__( self, width=480, height=640, nbars, top, middle, bottom ):
    self.nbars = nbars

    self.top    = top
    self.middle = middle
    self.bottom = bottom

    self.width  = width
    self.height = height

class BIButton( gtk.Button ):
  def __init__( self, info ):
    gtk.Button.__init__( self, info.label )
    self.info = info
    self.set_border_width = 0

class BIBar( gtk.Fixed ):
  def __init__( self, info ):
    self._left   = BIButton( info.left.label )
    self._center = BIButton( info.center.label )
    self._right  = BIButton( info.right.label )

class BIFrame( gtk.Fixed ):
  def __init__( self, info ):
    self.set_request_size( info.width, info.height )

    nbars = frameInfo['nbars']
    if nframes >= 1:
      self._top = BIBar( )
    self._middle = None
    self._bottom = None

    self._tl = None
    self._tc = None
    self._tr = None
    self._ml = None
    self._mc = None
    self._mr = None
    self._bl = None
    self._bc = None
    self._br = None
    
  def topBar( self ):
    return _top
  def middleBar( self ):
    return _middle
  def bottomBar( self ):
    return _bottom

  def tl( self ):
    return self._tl
  def tc( self ):
    return self._tc
  def tr( self ):
    return self._tr
  def ml( self ):
    return self._ml
  def mc( self ):
    return self._mc
  def mr( self ):
    return self._mr
  def bl( self ):
    return self._bl
  def bc( self ):
    return self._bc
  def br( self ):
    return self._br
