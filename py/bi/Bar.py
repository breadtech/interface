##
# title = BI.Bar.py
# by = Brian Kim
# description = the view that contains the bars
#

import pygtk
pygtk.require('2.0')
import gtk

class BIBar( gtk.Fixed )
  def __init__( self ):
    self.set_size_request( 480, 88 )
    pass
