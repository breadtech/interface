##
# title: Settings.py
# by: Brian Kim
# description: the global settings object
# 

class Settings():
  def __init__( self ):

  def get_app_name( self ):
    
  def set_app_name( self, app_name ):
    self.dict = { 'app_name' : app_name }

  def set( self, key, value, override=False ):
    try:
      x = self.dict[key]
    except KeyError:
      self.dict[key] = value

    if not x == None and override:
      self.dict[key] = value

  def get( self, key ):
    return self.dict[key]

# singleton object
settings = Settings()
