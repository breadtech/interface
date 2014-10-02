##
# title: breadinterface.py
# by: Brian Kim
# description: this breadinterface class contains a set of undefined
#  methods that do absolutely nothing. As the programmer, you can 
#  define a subclass of breadinterface that gives meaning to these
#  methods. That way, you can generically control a breadinterface 
#  object's lifestyle with these methods
#

class lifecycle():
  def __init__( self ):
    pass

  def start( self ):
    pass

  def resume( self ):
    pass

  def pause( self ):
    pass
    
  def stop( self ):
    pass

  def update( self ):
    pass

  def cleanup( self ):
    pass

class buttons():

  # text labels
  def tl_label( self ):
    return 'tl'

  def tm_label( self ):
    return 'tm'

  def tr_label( self ):
    return 'tr'

  def ml_label( self ):
    return 'ml'

  def mm_label( self ):
    return 'mm'

  def mr_label( self ):
    return 'mr'

  def bl_label( self ):
    return 'bl'

  def bm_label( self ):
    return 'bm'

  def br_label( self ):
    return 'br'

  # clicked actions
  def tl_clicked( self, widget ):
    print 'tl clicked'

  def tm_clicked( self, widget ):
    print 'tm clicked'

  def tr_clicked( self, widget ):
    print 'tr clicked'

  def ml_clicked( self, widget ):
    print 'ml clicked'

  def mm_clicked( self, widget ):
    print 'mm clicked'

  def mr_clicked( self, widget ):
    print 'mr clicked'

  def bl_clicked( self, widget ):
    print 'bl clicked'

  def bm_clicked( self, widget ):
    print 'bm clicked'

  def br_clicked( self, widget ):
    print 'br clicked'

  # long hold actions
  def tl_long_hold( self ):
    print 'tl long hold'

  def tm_long_hold( self ):
    print 'tm long hold'

  def tr_long_hold( self ):
    print 'tr long hold'

  def ml_long_hold( self ):
    print 'ml long hold'

  def mm_long_hold( self ):
    print 'mm long hold'

  def mr_long_hold( self ):
    print 'mr long hold'

  def bl_long_hold( self ):
    print 'bl long hold'

  def bm_long_hold( self ):
    print 'bm long hold'

  def br_long_hold( self ):
    print 'br long hold'

##
# title: prototype.py
# by: Aaron Philips, Brian Kim
# description:
#  - a prototype of what we hope to accomplish 
#    with breadinterface...
# 

import pygtk
pygtk.require('2.0')
import gtk

class prototype( buttons, lifecycle ):

  #
  # breadinterface buttons definition
  #
  def tl_label( self ):
    return unichr(9776) # menu

  def tm_label( self ):
    return "breadinterface" # title

  def tr_label( self ):
    return "i"	# info

  def bl_label( self ):
    return "--"   # remove

  def bm_label( self ):
    return "these buttons don't do anything"

  def br_label( self ):
    return "+"    # add

  def tl_clicked( self, widget ):
    self.display_button_info( widget )

  def tm_clicked( self, widget ):
    self.display_button_info( widget )
    print 'tm clicked'

  def tr_clicked( self, widget ):
    self.display_button_info( widget )
    print 'tr clicked'

  def bl_clicked( self, widget ):
    self.display_button_info( widget )
    print 'bl clicked'

  def bm_clicked( self, widget ):
    self.display_button_info( widget )
    print 'bm clicked'

  def br_clicked( self, widget ):
    self.display_button_info( widget )
    print 'br clicked'

  #
  # breadinterface lifecycle methods
  #

  def __init__( self ):
    # window
    self.w = gtk.Window()

    # controller
    self.frame = gtk.VBox()
  
    # frame
    self.top = gtk.HBox()
    self.bottom = gtk.HBox()
    self.tree = gtk.TreeView()
  
    self.button_dict = {
      self.tl_label() : "clicking the menu button opens a subframe of menu items",
      self.tm_label() : "clicking the title button does not do anything",
      self.tr_label() : "clicking the info button will display more information about this (nothing)",
      self.bl_label() : "clicking the remove button will remove nothing",
      self.bm_label() : "clicking the bottom middle button will do absolutely nothing",
      self.br_label() : "clicking the add button will add nothing"
    }
  
    # bar
    self.tl = gtk.Button(self.tl_label())
    self.tm = gtk.Button(self.tm_label())
    self.tr = gtk.Button(self.tr_label())
    self.bl = gtk.Button(self.bl_label())
    self.bm = gtk.Button(self.bm_label())
    self.br = gtk.Button(self.br_label())
  
    self.w.set_size_request( 320, 480)
    self.w.connect("delete-event", gtk.main_quit)

    self.tl.set_size_request( 44, 44 )
    self.tr.set_size_request( 44, 44 )
    self.bl.set_size_request( 44, 44 )
    self.br.set_size_request( 44, 44 )

    self.tl.props.relief = gtk.RELIEF_NONE
    self.tm.props.relief = gtk.RELIEF_NONE
    self.tr.props.relief = gtk.RELIEF_NONE
    self.bl.props.relief = gtk.RELIEF_NONE
    self.bm.props.relief = gtk.RELIEF_NONE
    self.br.props.relief = gtk.RELIEF_NONE

    self.tl.connect( "clicked", self.tl_clicked )
    self.tm.connect( "clicked", self.tm_clicked )
    self.tr.connect( "clicked", self.tr_clicked )
    self.bl.connect( "clicked", self.bl_clicked )
    self.bm.connect( "clicked", self.bm_clicked )
    self.br.connect( "clicked", self.br_clicked )

    self.top.pack_start( self.tl,False)
    self.top.pack_start( self.tm,True)
    self.top.pack_start( self.tr,False)
    self.top.modify_fg(gtk.STATE_NORMAL, gtk.gdk.color_parse( "black" ) )

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
    message.set_markup( self.button_dict[button.get_label()] ) # button, button_dict[ str(button.get_label()) ] )
    message.run()

  def start( self ):
    self.w.show_all()
    gtk.main()

  def stop( self ):
    pass
  
  def resume( self ):
    pass

  def stop( self ):
    pass
  
def main():
  bi = prototype()
  bi.start()

if __name__ == "__main__":
  main()
