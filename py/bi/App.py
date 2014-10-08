##
# title = App.py
# by = Brian Kim
# description = the breadinterface application class to initialize the gtk lib
#

from breadinterface import lifecycle

from Navigator import Navigator
from Settings import Settings

from Controller import Controller

class App( lifecycle ):
  def __init__( self, root=Controller('breadinterface') ):
    # init the app components
    self.settings = Settings()

    self.navigator = Navigator( root )
    Navigator.set_singleton( self.navigator )

    self.navigator.root( root_class(app_title) )

  def cleanup( self ):
    self.settings.cleanup()
    self.navigator.cleanup()

##
# app load order: 
#   state manager -> navigator -> window manager
#

  def start( self ):
    self.navigator.start()

  def resume( self ):
    self.navigator.resume()

  def pause( self ):
    self.navigator.pause()

  def stop( self ):
    self.navigator.stop()

if __name__=="__main__":
  App()
