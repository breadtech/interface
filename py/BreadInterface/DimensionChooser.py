##
# @file DimensionChooser.py
# @author Brian Kim
# @brief a method that displays an interface
#        for the user to choose a window dimension
# 

import pygtk
pygtk.require('2.0')
import gtk

class DimensionChooser():
  # delegate class definition
  class Delegate():
    def dimension_selected( self, dim ):
      pass

  @staticmethod
  def dim2str( dim ):
    """
     converts a dimension tuple into a string
    """
    return str(dim[0])+"x"+str(dim[1])
  
  def request_dimension(self):
    """
     the method that displays the gui to pick a dimension
      returns the selected dimension
    """
    self.w.show_all()
    gtk.main()
  
  def dim_selected( self, button, data ):
    self.delegate.dimension_selected( data )
    self.w.hide_all()
    gtk.main_quit()
  
  def __init__( self, delegate=Delegate() ):
    """
     constructor: initializes variables 
    """
    self.delegate = delegate 
   
    # model
    msg = "Pick a Screen Size"
    self.dims = [(1280,640),(1024,640),(800,640),(320,568),(320,480)]
  
    # view
    self.w = gtk.Window()
    self.w.set_title("Screen Size")
    frame = gtk.VBox()
    self.w.add(frame)
    msg_label = gtk.Label(msg)
    self.buttons = [gtk.Button(DimensionChooser.dim2str(x)) for x in self.dims]
    frame.pack_start(msg_label)
    for i in range(len(self.dims)):
      button = self.buttons[i]
      dim = self.dims[i]
      button.connect( 'clicked', self.dim_selected, dim )
      frame.pack_start(button)
  
if __name__ == "__main__":
  class X(DimensionChooser.Delegate):
    def dimension_selected( self, dim ): 
      print "selected dimension: "+DimensionChooser.dim2str(dim)
  x = X()
  dim = DimensionChooser(x) 
  dim.request_dimension()
