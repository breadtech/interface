##
# title: BreadInterface.App
# by: Brian Kim
# description: the top-level class that manages the 
#     Navigator and Settings. 
#   A developer could subclass this or just use it 
#   right out of the box.
#

from Navigator import Navigator
from Settings import Settings

##
# app class 
#
class App( lifecycle ):
  def __init__( self, root, appName='breadinterface' ):
    # init the app components
    self.settings = Settings(appName)
    self.navigator = Navigator( root )
    self.navigator.set_title( appName )

  def cleanup( self ):
    self.settings.cleanup()
    self.navigator.cleanup()

  def start( self ):
    self.navigator.start()

  def resume( self ):
    self.navigator.resume()

  def pause( self ):
    self.navigator.pause()

  def stop( self ):
    self.navigator.stop()

