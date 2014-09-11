##
# title: breadinterface.py
# by: Aaron Philips, Brian Kim
# description: sets up the whole interface with nonfunctional inputs
#

import pygtk
pygtk.require( '2.0' )
import gtk

class breadinterface():
  # app
  w = gtk.Window()

  # controller
  frame = gtk.VBox()

  # frame
  top = gtk.HBox()
  bottom = gtk.HBox()
  tree = gtk.TreeView()

  # button labels
  tl_label = unichr(9776)     # menu
  tm_label = "breadinterface" # title
  tr_label = "i"				# info
  bl_label = unichr(2212)		  # remove
  bm_label = "these buttons don't do anything"
  br_label = "+"				# add

  """
  button_dict = {
    tl_label : "clicking the menu button opens a subframe of menu items",
    tm_label : "clicking the title button does not do anything",
    tr_label : "clicking the info button will display more information about this (nothing)",
    bl_label : "clicking the remove button will remove nothing",
    bm_label : "clicking the bottom middle button will do absolutely nothing",
    br_label : "clicking the add button will add nothing"
  }
  """

  # bar
  tl = gtk.Button(tl_label)
  tm = gtk.Button(tm_label)
  tr = gtk.Button(tr_label)
  bl = gtk.Button(bl_label)
  bm = gtk.Button(bm_label)
  br = gtk.Button(br_label)

  def init( self ):
    self.w.set_size_request( 320, 480)
    self.w.connect("delete-event", gtk.main_quit)

    self.tl.set_size_request( 44, 44 )
    self.tr.set_size_request( 44, 44 )
    self.bl.set_size_request( 44, 44 )
    self.br.set_size_request( 44, 44 )

    self.tl.connect( "clicked", self.display_button_info )
    self.tr.connect( "clicked", self.display_button_info )
    self.bl.connect( "clicked", self.display_button_info )
    self.br.connect( "clicked", self.display_button_info )

    self.top.pack_start( self.tl,False)
    self.top.pack_start( self.tm,True)
    self.top.pack_start( self.tr,False)

    self.bottom.pack_start( self.bl,False)
    self.bottom.pack_start( self.bm,True)
    self.bottom.pack_start( self.br,False)

    self.frame.pack_start( self.top,False)
    self.frame.pack_start( self.tree,True)
    self.frame.pack_start( self.bottom,False)

    self.w.add( self.frame)

  def display_button_info( self, button ):
    message = gtk.MessageDialog(parent=self.w, 
                            flags=0, 
                            type=gtk.MESSAGE_QUESTION, 
                            buttons=gtk.BUTTONS_OK, 
                            message_format=None)
    message.set_markup( button.get_label() ) # button, button_dict[ str(button.get_label()) ] )
    message.run()

  def start( self ):
    self.w.show_all()
    gtk.main()

def main():
  bi = breadinterface()
  bi.init()
  bi.start()

if __name__ == "__main__":
  main()