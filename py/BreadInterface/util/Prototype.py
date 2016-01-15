##
# title: BreadInterface.Prototype.py
# by: Brian Kim
# description: the main BreadInterface app that help end-developers design their
#   button layouts
#

import pygtk
pygtk.require('2.0')
import gtk

from App import App
from Controller import Controller
from Lifecycle import Lifecycle
from BreadInterface.views.UnicodePickerView import UnicodePickerView

# 
# a function that will generate a pygtk BI Controller 
#
def generate_code( info ):
  # gogogogo
  y = '##\n# @file %s.py\n# @author <your name here>\n# @brief <Controller description>\n#\n\n' % info['title']
  y += 'import pygtk\npygtk.require(\'2.0\')\nimport gtk\n\n'
  y += 'from BreadInterface import Controller\n\n'
  y += 'class %s( Controller ):\n' % info['title']
  y += '  #\n  # Button Labels\n  #\n'
  y += '  def tl_label( self ):\n    return \'%s\'\n' % info['tl_label']
  y += '  def tr_label( self ):\n    return \'%s\'\n' % info['tr_label']
  y += '  def bl_label( self ):\n    return \'%s\'\n' % info['bl_label']
  y += '  def bm_label( self ):\n    return \'%s\'\n' % info['bm_label']
  y += '  def br_label( self ):\n    return \'%s\'\n' % info['br_label']
  y += '\n'
  y += '  #\n  # Button Clicks\n  #\n'
  y += '  def tl_clicked( self, b ):\n    # %s\n    pass\n' % info['tl']
  y += '  def tr_clicked( self, b ):\n    # %s\n    pass\n' % info['tr']
  y += '  def bl_clicked( self, b ):\n    # %s\n    pass\n' % info['bl']
  y += '  def bm_clicked( self, b ):\n    # %s\n    pass\n' % info['bm']
  y += '  def br_clicked( self, b ):\n    # %s\n    pass\n' % info['br']
  y += '\n'
  y += '  #\n  # Button Descriptions\n  #\n'
  y += '  def tl_info( self ):\n    return \'%s\'\n' % info['tl']
  y += '  def tr_info( self ):\n    return \'%s\'\n' % info['tr']
  y += '  def bl_info( self ):\n    return \'%s\'\n' % info['bl']
  y += '  def bm_info( self ):\n    return \'%s\'\n' % info['bm']
  y += '  def br_info( self ):\n    return \'%s\'\n' % info['br']
  return y


class PrototypeController( Controller ):

  #
  # breadinterface buttons definition
  #
  def tl_label( self ):
    return self._tl_label

  def tm_label( self ):
    return self._tm_label
	
  def tr_label( self ):
    return self._tr_label

  def bl_label( self ):
    return self._bl_label

  def bm_label( self ):
    return self._bm_label

  def br_label( self ):
    return self._br_label

  #
  # button clicks
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

  #
  # button information
  def tl_info( self ):
    return 'change button label to text field value'
  def tr_info( self ):
    return 'change button label to text field value'
  def bl_info( self ):
    return 'change button label to text field value'
  def bm_info( self ):
    return 'change button label to text field value'
  def br_info( self ):
    return 'change button label to text field value'
  
  def update( self ):
    Controller.update(self)
    self.view.clear()

  # 
  # generate code (prototype view delegate)
  def generate_code( self, info ):
    if len(info['title']) == 0:
      info['title'] = "MyController"
    info['tl_label'] = self._tl_label
    info['tr_label'] = self._tr_label
    info['bl_label'] = self._bl_label
    info['bm_label'] = self._bm_label
    info['br_label'] = self._br_label
    y = generate_code( info )
    with open('%s.py'%info['title'],'w') as fp:
      fp.write(y)
      fp.close()
      msg = gtk.MessageDialog(type=gtk.MESSAGE_INFO,flags=gtk.DIALOG_MODAL,buttons=gtk.BUTTONS_OK)
      msg.set_markup('The file \'%s.py\' has been successfully created'%info['title'])
      msg.run()
    self.nav.stop() 

  ##
  # custom constructor
  #
  def __init__( self ):
    # ui
    self._tl_label = "tl"
    self._tm_label = "tm"
    self._tr_label = "tr"
    self._bl_label = "bl"
    self._bm_label = "bm"
    self._br_label = "br"
    Controller.__init__( self, view=PrototypeController.PrototypeView(self) )

  ##
  # custom view class definition
  #
  class PrototypeView( gtk.VBox, Lifecycle, UnicodePickerView.Delegate ):
    class Delegate():
      def generate_code( self, info ):
        pass
    
    def gen1_clicked( self, view ):
      self.remove(self.vbox1)
      self.add(self.vbox2)
      # such a hack...
      self.title_entry.set_text( self.delegate._tm_label )
  
    def go2gen1( self, view ):
      self.remove(self.vbox2)
      self.add(self.vbox1)
    
    def gen2_clicked( self, view ):
      x = {}
      x['title'] = self.title_entry.get_text()
      x['tl'] = self.tl_entry.get_text()
      x['tr'] = self.tr_entry.get_text()
      x['bl'] = self.bl_entry.get_text()
      x['bm'] = self.bm_entry.get_text()
      x['br'] = self.br_entry.get_text()
      self.delegate.generate_code( x )
   
    def uni_clicked( self, view ):
      # swap the views
      self.remove( self.vbox1 )
      self.add( self.unicode_view )
 
    # 
    # unicode picker delegate
    def did_select_unicode( self, val ):
      old = self.entry.get_text()
      old += val
      self.entry.set_text(old)
      # swap the views
      self.remove(self.unicode_view)
      self.add(self.vbox1)

    def __init__( self, delegate=Delegate() ):
      gtk.VBox.__init__( self, 25 )
      self.set_border_width( 25 )

      #
      # model
      self.delegate = delegate
      self.instr_s = PrototypeController.PrototypeView.instructions()
      self.instr_buf = gtk.TextBuffer()
      self.instr_buf.set_text(self.instr_s)
   
      #
      # ui
      self.vbox1 = gtk.VBox()
      
      #
      # vbox1
      # top: instructions
      # middle: entry
      # bottom: generate code+unicode picker
      #

      #
      # top
      self.instr = gtk.TextView( self.instr_buf )
      self.instr.set_editable( False )
      self.instr.set_wrap_mode( gtk.WRAP_WORD )

      #
      # middle
      hbox = gtk.HBox()
      label = gtk.Label("Desired Button Label: ")
      self.entry = gtk.Entry()
      hbox.pack_start( label, False )
      hbox.pack_start( self.entry )

      #
      # bottom
      self.gen1button = gtk.Button( "Generate Code" )
      self.unibutton = gtk.Button( "Unicode Picker" )
      # hook up button clicks
      self.gen1button.connect( "clicked", self.gen1_clicked )
      self.unibutton.connect( "clicked", self.uni_clicked )
  
      # add components to vbox
      self.vbox1.pack_start( self.instr, False )
      self.vbox1.pack_start( hbox )
      self.vbox1.pack_start( self.unibutton, False )
      self.vbox1.pack_start( self.gen1button, False )
      self.vbox1.show()
      self.add( self.vbox1 )
  
      #
      # vbox2
      # name field
      # button layout info field
      #

      self.vbox2 = gtk.VBox()
      hbox1 = gtk.HBox()
      # title
      title_label = gtk.Label( 'Controller Title: ' )
      self.title_entry = gtk.Entry()
      hbox1.pack_start(title_label,False)
      hbox1.pack_start(self.title_entry)
      # tl
      hbox2 = gtk.HBox()
      tl_label = gtk.Label( 'Top-Left Description: ' )
      self.tl_entry = gtk.Entry()
      hbox2.pack_start(tl_label,False)
      hbox2.pack_start(self.tl_entry)
      # tr
      hbox3 = gtk.HBox()
      tr_label = gtk.Label( 'Top-Right Description: ' )
      self.tr_entry = gtk.Entry()
      hbox3.pack_start(tr_label,False)
      hbox3.pack_start(self.tr_entry)
      # bl
      hbox4 = gtk.HBox()
      bl_label = gtk.Label( 'Bottom-Left Description: ' )
      self.bl_entry = gtk.Entry()
      hbox4.pack_start(bl_label,False)
      hbox4.pack_start(self.bl_entry)
      # bm
      hbox5 = gtk.HBox()
      bm_label = gtk.Label( 'Bottom-Middle Description: ' )
      self.bm_entry = gtk.Entry()
      hbox5.pack_start(bm_label,False)
      hbox5.pack_start(self.bm_entry)
      # br
      hbox6 = gtk.HBox()
      br_label = gtk.Label( 'Bottom-Right Description: ' )
      self.br_entry = gtk.Entry()
      hbox6.pack_start(br_label,False)
      hbox6.pack_start(self.br_entry)

      # buttons
      self.back = gtk.Button('Go Back')
      self.gen2button = gtk.Button('Generate Code')
      # hook em up
      self.back.connect( 'clicked', self.go2gen1 )
      self.gen2button.connect( 'clicked', self.gen2_clicked )

      self.vbox2.pack_start( hbox1 )
      self.vbox2.pack_start( hbox2 )
      self.vbox2.pack_start( hbox3 )
      self.vbox2.pack_start( hbox4 )
      self.vbox2.pack_start( hbox5 )
      self.vbox2.pack_start( hbox6 )
      self.vbox2.pack_start( self.back, False )
      self.vbox2.pack_start( self.gen2button, False )

      self.vbox2.show_all()

      #
      # embed the unicode picker in the view
      self.unicode_view = UnicodePickerView(self)
      self.unicode_view.show_all()
   
    def update( self ):
      pass

    def clear( self ):
      self.entry.set_text("")
    
    @staticmethod
    def instructions(): 
      y = 'Instructions:\n'
      y += '- insert text in the \'Desired Button Label\' field below and click a corner button to fill with that text.\n'
      y += '- clicking the \'Unicode Picker\' button will display a table of clickable Unicode characters\n' 
      y += '- clicking the \'Generate Code\'  button will display an interface to create a template Controller class '
      y += 'with the specified button labels'
      return y


def main():
  app = App(root=PrototypeController(),dim=(800,600))
  app.start()

if __name__ == "__main__":
  main()
