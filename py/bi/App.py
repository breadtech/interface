##
# title = BI.App.py
# by = Brian Kim
# description = the breadinterface application class to initialize the gtk lib
#

import pygtk
pygtk.require('2.0')
import gtk
from bi.Controller import BIController, BIDefaultController

class BIApp( ):
  def __init__( self ):
    self.window = gtk.Window( )
    self.window.resize( 480, 640 )
    self.window.add( self.main().view )

  def main( self, x=None ):
    if x==None:
      if self._main==None:
        self._main = BIDefaultController()
      return self._main
    else:
      self._main = x

  def start( self ):
    self.window.show()

def main():
  app = BIApp()
  app.start()
  gtk.main()

if __name__=="__main__":
  main()
