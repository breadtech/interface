##
# title: Navigator.py
# by: Brian Kim
# description: the class description of an object
#   that controls the navigation of an app. It uses
#   a stack to keep track of all the controllers that
#   are in use by the app. 
#
#  there isn't much use to subclass this. the navigator
#  should be able to be used pretty transparently
# 

class Navigator( breadinterface, GtkWrapper ):
  def __init__( self, window, root_class ):
    GtkWrapper.__init__( self, window, window )
    self.ctrlrs = { root }
    
  """ the current controller on screen """
  def current( self ):
    return self.size() - 1

  def push( self, controller_class ):
    # pause the top controller
    self.current().stop()

    # add the controller to the stack
    self.ctrlrs.append( controller )

    # start the new top controller
    self.controller.start()

  def pop( self ):
    # remove the top controller from the stack
    y = self.ctrlrs.pop()

    # destory that controller
    y.cleanup()

    # start the next controller in the stack
    self.current().start()

  def root( self ):
    # simply the first controller
    return self.ctrlrs[0]

  def size( self ):
    # the size of the stack
    return len( self.ctrlrs )
                      
  def start( self ):
    # starts the navigator
    self.current().start()

