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

    # remove the relief
    y.props.relief = gtk.RELIEF_NONE

    # make colors
    map = y.get_colormap()
    blk = map.alloc_color("black")
    wht = map.alloc_color("white")

    # set the color style on the label
    label = y.get_child()
    style = label.get_style().copy()
    style.fg[gtk.STATE_NORMAL] = wht
    label.set_style(style)
     
    # set the color style on the button
    style = y.get_style().copy()
    style.bg[gtk.STATE_NORMAL] = blk
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
