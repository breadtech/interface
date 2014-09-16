##
# title = App.py
# by = Brian Kim
# description = the breadinterface application class to initialize the gtk lib
#

from breadinterface import breadinterface

from Navigator import Navigator
from Settings import Settings
from WindowManager import WindowManager
from StateManager import StateManager

from Controller import Controller

class App( breadinterface ):
  def __init__( self, app_title, root_class=Controller.DefaultController ):
    # init the app components
    self.settings = Settings()
    self.wm = WindowManager()
    self.navigator = Navigator( wm.window )
    self.navigator.root( root_class )
    self.sm = StateManager()

  def cleanup( self ):
    self.settings.cleanup()
    self.wm.cleanup()
    self.navigator.cleanup()
    self.sm.cleanup()

##
# app load order: 
#   state manager -> navigator -> window manager
#

  def start( self ):
    self.sm.start()
    self.navigator.start()
    self.wm.start()

  def resume( self ):
    self.sm.resume()
    self.navigator.resume()
    self.wm.resume()

  def pause( self ):
    self.wm.pause()
    self.navigator.pause()
    self.sm.pause()

  def stop( self ):
    self.wm.stop()
    self.navigator.stop()
    self.sm.stop()

if __name__=="__main__":
  App()
