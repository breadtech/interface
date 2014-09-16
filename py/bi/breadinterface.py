##
# title: breadinterface.py
# by: Brian Kim
# description: this breadinterface class contains a set of undefined
#  methods that do absolutely nothing. As the programmer, you can 
#  define a subclass of breadinterface that gives meaning to these
#  methods. That way, you can generically control a breadinterface 
#  object's lifestyle with these methods
#

class breadinterface():
  def __init__( self ):
    pass

  def start( self ):
    pass

  def resume( self ):
    pass

  def pause( self ):
    pass
    
  def stop( self ):
    pass

  def cleanup( self ):
    pass
    

