##
# title: BreadInterface.ButtonLayout
# by: Brian Kim
# description: the class that defines the content
#   and functionality of BreadInterface buttons
#

import pygtk
pygtk.require('2.0')
import gtk

class ButtonLayout():

  @staticmethod
  def gtk_button( text, scale=1 ):
    """ returns a properly styled gtk button for breadinterface """
    # create the button
    y = gtk.Button( text )

    # set the size
    size = 44 * scale
    y.set_size_request( size, size )

    # set the color style on the button
    style = y.get_style().copy()
    style.bg[gtk.STATE_NORMAL] = gtk.gdk.color_parse('#000000')
    style.bg[gtk.STATE_PRELIGHT] = gtk.gdk.color_parse('#555555')
    y.set_style(style)

    # return the button
    return y
    
  # text labels
  def tl_label( self ):
    return ''

  def tm_label( self ):
    return ''

  def tr_label( self ):
    return ''

  def bl_label( self ):
    return ''

  def bm_label( self ):
    return ''

  def br_label( self ):
    return ''

  # clicked actions
  def tl_clicked( self, widget ):
    print 'tl clicked'

  def tm_clicked( self, widget ):
    print 'tm clicked'

  def tr_clicked( self, widget ):
    print 'tr clicked'

  def bl_clicked( self, widget ):
    print 'bl clicked'

  def bm_clicked( self, widget ):
    print 'bm clicked'

  def br_clicked( self, widget ):
    print 'br clicked'

  # button infos
  def tl_info( self ):
    return "tl button"

  def tm_info( self ):
    return "tm button"

  def tr_info( self ):
    return "tr button"

  def bl_info( self ):
    return "bl button"

  def bm_info( self ):
    return "bm button"

  def br_info( self ):
    return "br button"

"""
ZZ: create a ButtonDescriptionWindow class
    to show and respond to certain button presses

  # description string
  def tl_description( self, widget ):

  @staticmethod
  def show_button_description():
    w = gtk.Window()
    w.connect('delete-event', ButtonLayout.button_description_close
"""
