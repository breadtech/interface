##
# title: breadinterface.py
# by: Brian Kim
# description: the python script that contain all the necessary components for breadinterface
#

import pygtk
pygtk.require('2.0')
import gtk

import App
import Controller

class SuitsController( Controller ):
  spade = unichr(9828)
  heart = unichr(9825)
  club = unichr(9826)
  diamond = unichr(9831)

  def __init__( self ):
    self.label = gtk.Label("NULL")
    import pango
    self.label.modify_font( pango.FontDescription("sans 72" ))
    Controller.__init__( self, view=self.label )

  def tl_label( self ):
    return self.spade

  def tl_clicked( self, widget ):
    self.label.set_text( self.spade )

  def tm_label( self ):
    return 'Suits'

  def tr_label( self ):
    return self.heart

  def tr_clicked( self, widget ):
    self.label.set_text( self.heart )

  def bl_label( self ):
    return  self.club

  def bl_clicked( self, widget ):
    self.label.set_text( self.club )

  def bm_label( self ):
    return 'click a suit'

  def bm_clicked( self, widget ):
    self.nav.pop()

  def br_label( self ):
    return self.diamond

  def br_clicked( self, widget ):
    self.label.set_text( self.diamond )

class PrototypeController( Controller ):

  #
  # breadinterface buttons definition
  #
  def tl_label( self ):
    #return self._tl_label
    return '?'	

  def tm_label( self ):
    #return self._tm_label
    return 'Sample Controller'
	
  def tr_label( self ):
    #return self._tr_label
    return unichr(0x2699)

  def bl_label( self ):
    #return self._bl_label
    return '+'

  def bm_label( self ):
    #return self._bm_label
    return 'by Fee'

  def br_label( self ):
    #return self._br_label
    return '-'

  def tl_clicked( self, widget ):
    self._tl_label = self.view.entry.get_text()
    self.update()

  def tm_clicked( self, widget ):
    Controller.tm_clicked( self, widget )
    self._tm_label = self.view.entry.get_text()
    self.update()

  def tr_clicked( self, widget ):
    self._tr_label = self.view.entry.get_text()
    self.update()

  def bl_clicked( self, widget ):
    self._bl_label = self.view.entry.get_text()
    self.update()

  def bm_clicked( self, widget ):
    self._bm_label = self.view.entry.get_text()
    self.update()

  def br_clicked( self, widget ):
    self._br_label = self.view.entry.get_text()
    self.update()
  
  def update( self ):
    Controller.update(self)
    self.view.clear()

  ##
  # custom constructor
  #
  def __init__( self ):
    self._tl_label = "tl"
    self._tm_label = "tm"
    self._tr_label = "tr"
    self._bl_label = "bl"
    self._bm_label = "bm"
    self._br_label = "br"
    Controller.__init__( self, view=PrototypeController.PrototypeView() )
    self.button_info_dict['tl'] = 'change button label to text field value'
    self.button_info_dict['tr'] = 'change button label to text field value'
    self.button_info_dict['bl'] = 'change button label to text field value'
    self.button_info_dict['bm'] = 'change button label to text field value'
    self.button_info_dict['br'] = 'change button label to text field value'

  ##
  # custom view class definition
  #
  class PrototypeView( gtk.Alignment, lifecycle ):
    def __init__( self ):
      gtk.Alignment.__init__( self, 0.4, 0.4, 0.6, 0.6 )
      self.entry = gtk.Entry()
      self.add( self.entry )

    def clear( self ):
      self.entry.set_text("")


def main():
  app = App(root=PrototypeController())
  app.start()

if __name__ == "__main__":
  main()
