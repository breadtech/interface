##
# title = Controller.py
# by = Brian Kim
# description = the breadinterface controller
#  manages a frame (view) and the actions that should
#  trigger changes in some model
#

from breadinterface import *
from GtkWrapper import GtkWrapper

from Navigator import Navigator

from Frame import Frame
from Bar import Bar
# from Button import Button

class Controller( lifecycle, buttons, GtkWrapper ):

  ##
  # constructor
  #
  def __init__( self, title, main_view=None,  ):
    # set the title
    self.title = title 

    # create the frame
    tl = Button( self.tl_label(), self.tl_clicked )
    tm = Button( self.title, self.tm_clicked )
    tr = Button( self.tr_label(), self.tr_clicked )
    ml = Button( self.ml_label(), self.ml_clicked )
    mm = Button( self.mm_label(), self.mm_clicked )
    mr = Button( self.mr_label(), self.mr_clicked )
    bl = Button( self.bl_label(), self.bl_clicked )
    bm = Button( self.bm_label(), self.bm_clicked )
    br = Button( self.br_label(), self.br_clicked )

    top_bar = Bar( tl, tm, tr )
    middle_bar = Bar( ml, mm, mr )
    bottom_bar = Bar( bl, bm, br )

    self.frame = Frame( top_bar, middle_bar, bottom_bar )

    # forward the frame's gtk obj to be the controller's gtk obj
    self.obj = self.frame.obj

    # set up the gtk stuff
    self.gtk()

  def gtk( self ):
    self.frame.gtk()

  def segue( self, mode, target ):
    pass

  # breadinterace methods
  def start( self ):
    self.frame.start()

  def stop( self ):
    self.frame.stop()

  def update( self ):
    self.frame.update()

  def cleanup( self ):
    self.frame.cleanup()
    self.frame = None
