##
# title: BreadInterface.App
# by: Brian Kim
# description: the top-level class that manages the 
#     Navigator and Settings. 
#   A developer could subclass this or just use it 
#   right out of the box.
#

from Lifecycle import Lifecycle
from Navigator import Navigator
from Settings import Settings

##
# app class 
#
class App( Lifecycle ):
  def __init__( self, root, dim=None, appName='BreadInterface' ):
    # init the app components
    # self.settings = Settings(appName)
    self.navigator = Navigator( root, dim )
    self.appName = appName

  def cleanup( self ):
    self.settings.cleanup()
    self.navigator.cleanup()

  def start( self ):
    if not self.navigator.ready:
      print "Navigator not ready..."
      return
    self.navigator.window.set_title( self.appName )
    self.navigator.start()

  def stop( self ):
    self.navigator.stop()

