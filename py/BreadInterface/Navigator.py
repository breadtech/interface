##
# title: BreadInterface.Navigator
# by: Brian Kim
# description: the class that manages a stack of Controllers
#   using push and pop methods
# 

import pygtk
pygtk.require('2.0')
import gtk

from Controller import Controller
from Lifecycle import Lifecycle
from DimensionChooser import DimensionChooser

##
# navigator class
#
class Navigator( Lifecycle ):

  #
  # dimension chooser lifecycle methods
  #
  def dimension_selected( self, dim ):
    self.dim = dim
    self.finish_init()

  #
  # lifecycle methods
  # 
  def __init__( self, root, dim=None ):
    self.ready = False
    self.root = root
    if dim == None:
      dim_chooser = DimensionChooser(self)
      dim_chooser.request_dimension()
    else:
      self.dim = dim
      self.finish_init()

  def finish_init( self ):
    self.ready = True
    self.window = gtk.Window()
    self.window.set_size_request( self.dim[0], self.dim[1])
    self.window.connect("delete-event", gtk.main_quit)

    self.root.nav = self
    self.ctrlrs = [ self.root ]
            
  def start_top( self ):
    self.window.add( self.current().frame )
    self.current().start()
          
  def start( self ):
    self.start_top()
    self.window.show()
    gtk.main()

  def stop_top( self ):
    self.window.remove( self.current().frame )
    self.current().stop()

  def stop( self ):
    self.stop_top()
    self.window.hide()
    gtk.main_quit()

  #
  # navigation stack methods
  #

  def current( self ):
    """ the current controller on screen """
    return self.ctrlrs[self.size() - 1]

  def push( self, controller ):
    # stop the top controller
    self.stop_top()

    # create reference to nav
    controller.nav = self

    # add the controller to the stack
    self.ctrlrs.append( controller )

    # start the new top controller
    self.start_top()

  def pop( self ): 
    # stop the top controller
    self.stop_top()

    # remove the top controller from the stack
    y = self.ctrlrs.pop()

    # destory that controller
    y.cleanup()

    # quit the app if that was the last controller
    if self.size() == 0:
      gtk.main_quit()
      return

    # start the next controller in the stack
    self.start_top()

  def root( self ):
    # simply the first controller
    return self.ctrlrs[0]

  def size( self ):
    # the size of the stack
    return len( self.ctrlrs )

