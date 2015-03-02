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
  
    # hook up the button actions
    self.tl.connect( "clicked", self.tl_clicked )
    self.tm.connect( "clicked", self.tm_clicked )
    self.tr.connect( "clicked", self.tr_clicked )
    self.bl.connect( "clicked", self.bl_clicked )
    self.bm.connect( "clicked", self.bm_clicked )
    self.br.connect( "clicked", self.br_clicked )

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
    msg = gtk.MessageDialog( type=gtk.MESSAGE_INFO, 
                             flags=gtk.DIALOG_MODAL,
                             buttons=gtk.BUTTONS_OK)
                             
    info = 'Button Layout\n\ntop-left: '+self.tl_label()+' : '
    info += self.tl_info()
    info += '\ntop-right: '+self.tr_label()+' : '
    info += self.tr_info()
    info += '\nbottom-left: '+self.bl_label()+' : '
    info += self.bl_info()
    info += '\nbottom-middle: '+self.bm_label()+' : '
    info += self.bm_info()
    info += '\nbottom-right: '+self.br_label()+' : '
    info += self.br_info()
    msg.set_markup( info )
    msg.run()
    msg.destroy()

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

    #
    # set the color style on the label
    # MUST BE DONE EVERY SINGLE TIME THE LABEL IS SET
    # HOW STUPID IS THAT????
    label = self.tl.get_child()
    style = label.get_style().copy()
    style.fg[gtk.STATE_NORMAL] = gtk.gdk.color_parse('#FFFFFF')
    style.fg[gtk.STATE_PRELIGHT] = gtk.gdk.color_parse('#FFFFFF')
    self.tl.get_child().set_style(style)
    self.tm.get_child().set_style(style)
    self.tr.get_child().set_style(style)
    self.bl.get_child().set_style(style)
    self.bm.get_child().set_style(style)
    self.br.get_child().set_style(style)
     
    self.view.update()

  def clear( self ):
    pass

  def stop( self ):
    self.frame.hide_all()
  
