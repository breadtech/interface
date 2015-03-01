##
# title: BreadInterface.Controller.py
# by: Brian Kim
# description: the bread and butter of BreadInterface.
#   Developers will subclass the Controller to utilitize
#   the familiar BreadInterface button layout in addition
#   to their own app-specific functionality
#

import pygtk
pygtk.require('2.0')
import gtk

from ButtonLayout import ButtonLayout
from Lifecycle import Lifecycle

##
# controller class
#
class Controller( ButtonLayout, Lifecycle ):

  #
  # breadinterface lifecycle methods
  #

  def __init__( self, view, title='BreadInterface' ):
    self.title = title
  
    # controller
    self.frame = gtk.VBox()
  
    # frame
    self.top = gtk.HBox()
    self.view = view
    self.bottom = gtk.HBox()

    # bar
    self.tl = ButtonLayout.gtk_button(self.tl_label())
    self.tm = ButtonLayout.gtk_button(self.tm_label())
    self.tr = ButtonLayout.gtk_button(self.tr_label())
    self.bl = ButtonLayout.gtk_button(self.bl_label())
    self.bm = ButtonLayout.gtk_button(self.bm_label())
    self.br = ButtonLayout.gtk_button(self.br_label())
  
    # fixing the size of the buttons
    self.tl.set_size_request( 44, 44 )
    self.tr.set_size_request( 44, 44 )
    self.bl.set_size_request( 44, 44 )
    self.br.set_size_request( 44, 44 )

    # remove the borders
    self.tl.props.relief = gtk.RELIEF_NONE
    self.tm.props.relief = gtk.RELIEF_NONE
    self.tr.props.relief = gtk.RELIEF_NONE
    self.bl.props.relief = gtk.RELIEF_NONE
    self.bm.props.relief = gtk.RELIEF_NONE
    self.br.props.relief = gtk.RELIEF_NONE

    # hook up the button actions
    self.tl.connect( "clicked", self.tl_clicked )
    self.tm.connect( "clicked", self.tm_clicked )
    self.tr.connect( "clicked", self.tr_clicked )
    self.bl.connect( "clicked", self.bl_clicked )
    self.bm.connect( "clicked", self.bm_clicked )
    self.br.connect( "clicked", self.br_clicked )

    # creating the button info dictionary
    self.button_info_dict = {}
    self.button_info_dict['tl'] = 'None'
    self.button_info_dict['tr'] = 'None'
    self.button_info_dict['bl'] = 'None'
    self.button_info_dict['bm'] = 'None'
    self.button_info_dict['br'] = 'None'

    # build the view
    self.top.pack_start( self.tl,False)
    self.top.pack_start( self.tm,True)
    self.top.pack_start( self.tr,False)

    self.bottom.pack_start( self.bl,False)
    self.bottom.pack_start( self.bm,True)
    self.bottom.pack_start( self.br,False)

    self.frame.pack_start( self.top,False)
    self.frame.pack_start( self.view,True)
    self.frame.pack_start( self.bottom,False)

  #
  # breadinterface button layout
  # - defaulting the top-middle label to be the title
  # - making the default button click to display button info
  #
  def tm_label( self ):
    return self.title

  def tm_clicked( self, v ):
    msg = gtk.MessageDialog( parent=None,
                             flags=0,
                             type=gtk.MESSAGE_INFO,
                             buttons=gtk.BUTTONS_NONE,
                             message_format=None )
    info = 'Button Layout\n\ntop-left: '+self.tl_label()+' : '
    info += self.button_info_dict['tl']
    info += '\ntop-right: '+self.tr_label()+' : '
    info += self.button_info_dict['tr']
    info += '\nbottom-left: '+self.bl_label()+' : '
    info += self.button_info_dict['bl']
    info += '\nbottom-middle: '+self.bm_label()+' : '
    info += self.button_info_dict['bm']
    info += '\nbottom-right: '+self.br_label()+' : '
    info += self.button_info_dict['br']
    info += '\n\nPress ESC twice to close this popup'
    msg.set_markup( info )
    msg.run()

  def start( self ):
    self.frame.show_all()
    self.update()

  def update( self ):
    self.tl.set_label( self.tl_label() )
    self.tm.set_label( self.tm_label() )
    self.tr.set_label( self.tr_label() )
    self.bl.set_label( self.bl_label() )
    self.bm.set_label( self.bm_label() )
    self.br.set_label( self.br_label() )
    self.view.update()

  def clear( self ):
    pass

  def stop( self ):
    self.frame.hide_all()
  
