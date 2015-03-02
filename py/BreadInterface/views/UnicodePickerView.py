##
# @file UnicodePickerView
# @author Brian Kim
# @brief a view that allows a user to pick a unicode value
#

import pygtk
pygtk.require('2.0')
import gtk

from BreadInterface import *

class UnicodePickerView(gtk.VBox):
  class Delegate():
    def did_select_unicode( self, val ):
      print 'unicode selected: ' + val 

  def hexgrp2str( self, grp ):
    # get the range
    low = grp*256
    high = grp*256+255
    return str('0x%04x - 0x%04x' % (low,high))
    
  def __init__( self, delegate=Delegate() ):
    self.delegate = delegate

    #
    # model
    #
    
    # range = curr*256 <> curr*256+255
    # the current low end of the unicode table
    self.curr = 0
    self.unicodes = [unichr(x) for x in range(255)]
    self.unicodes[0] = None   
    self.groups = [(0, 'ASCII'), (35, 'Symbols I'), (38, 'Symbols II'), (39, 'Symbols III')]
    self.combobox_model = gtk.ListStore(str)
    for x in self.groups:
      s = str(x[1] + ': ' + self.hexgrp2str(x[0]))
      self.combobox_model.append([s])

    #
    # ui
    #

    # 
    # layout: combobox, table of unicode, control
    gtk.VBox.__init__( self )
   
    # top: selects a popular unicode range
    self.combobox = gtk.ComboBox()
    cell = gtk.CellRendererText()
    self.combobox.pack_start(cell)
    self.combobox.add_attribute(cell, 'text', 0)
    self.combobox.set_model( self.combobox_model )
    self.combobox.connect( 'changed', self.cb_changed )

    # middle: a table
    self.table = gtk.Table(17, 17)
    # labels
    self.col_headers = [gtk.Label(str('0x_%x'%x)) for x in range(16)]
    self.row_headers = [gtk.Label(str('0x%x_'%x)) for x in range(16)]
    self.buttons    = [gtk.Button(self.unicodes[x]) for x in range(255)]
    for i in range(255):
      button = self.buttons[i]
      button.props.relief = gtk.RELIEF_NONE
      button.set_size_request( 22, 22 )
      button.connect( 'clicked', self.unicode_clicked )
      

    # add column headers to table
    for i in range(16):
      # determine placement of header
      left   = i+1
      right  = left+1
      top    = 0
      bottom = 1
      # addit
      self.table.attach( self.col_headers[i], left, right, top, bottom )
      
    # add row headers to table
    for i in range(16):
      left   = 0
      right  = 1
      top    = i+1
      bottom = top+1
      # add it
      self.table.attach( self.row_headers[i], left, right, top, bottom )

    # add unicode labels to table
    row = 0
    col = 0
    for i in range(255):
      left   = i % 16 + 1
      right  = left+1
      top    = i / 16 + 1
      bottom = top+1 
      # add it
      self.table.attach( self.buttons[i], left, right, top, bottom )
 
    # bottom: left arrow, current range, right arrow
    self.bottom = gtk.HBox()
    
    self.leftleft = gtk.Button('<<')
    self.left = gtk.Button('<')
    self.range = gtk.Label('0x0000 - 0x00ff')
    self.right = gtk.Button('>')
    self.rightright = gtk.Button('>>')
    # hook up the buttons
    self.left.connect( 'clicked', self.dec )
    self.leftleft.connect( 'clicked', self.decdec )
    self.right.connect( 'clicked', self.inc )
    self.rightright.connect( 'clicked', self.incinc )

    # add components to bottom hbox
    self.bottom.pack_start( self.leftleft, False )
    self.bottom.pack_start( self.left, False )
    self.bottom.pack_start( self.range, True )
    self.bottom.pack_start( self.right, False )
    self.bottom.pack_start( self.rightright, False )

    # add components to vbox
    self.pack_start( self.combobox, False)
    self.pack_start( self.table, True )
    self.pack_start( self.bottom, False )
  
  def unicode_clicked( self, button ):
    self.delegate.did_select_unicode( button.get_label() )

  def cb_changed( self, cb ):
    # get index
    i = cb.get_active()
    # get the curr
    self.curr = self.groups[i][0] if i > -1 else self.curr
    # update
    self.update()

  def dec( self, button ):
    self.curr = self.curr - 1 if self.curr > 0 else 0
    self.update()

  def decdec( self, button ):
    self.curr = self.curr - 16 
    if self.curr < 0:
      self.curr = 0
    self.update()

  def inc( self, button ):
    self.curr = self.curr + 1
    self.update()

  def incinc( self, button ):
    self.curr = self.curr + 16 
    self.update()

  def start( self ):
    self.show_all()

  def update( self ):
    
    #
    # set the button labels
    low = self.curr*256

    # update model
    for i in range(255):
      self.unicodes[i] = unichr(i+low)
    # check for that null byte str
    self.unicodes[0] = "" if self.curr == 0 else unichr(low)
  
    # update ui
    self.range.set_text( self.hexgrp2str(self.curr) )
    for i in range(255):
      self.buttons[i].set_label( self.unicodes[i] )

    # reset combobox
    self.combobox.set_active(-1)
  
if __name__ == "__main__":
  a = App( appName="Unicode Picker", root=Controller( UnicodePickerView(), "Unicode Picker" ))
  a.start()
