##
# title: BreadInterface.Settings
# by: Brian Kim
# description: the class that can store and recall key/value pairs
#   to persist user preferences.
# ZZ: incomplete implementation
#

##
# the Settings class will be defined as a 
# singleton oject
# code from http://code.activestate.com/recipes/52558/
class Settings():
  # storage for the instance reference
  __instance = None

  def __init__(self, app_name="app"):
    """ Create singleton instance """
    # Check whether we already have an instance
    if Settings.__instance is None:
      # we need an app_name

      # create and remember instance
      Settings.__instance = Settings.SettingsClass(app_name)
    self.__dict__['_Settings__instance'] = Settings.__instance

  def __getattr__(self, attr):
    """ Delegate access to implementation """
    return getattr(self.__instance, attr)

  def __setattr__(self, attr, value):
    """ Delegate access to implementation """
    return setattr(self.__instance, attr, value)

  ##
  # setttings class
  #  ivars: dict
  #
  class SettingsClass():
    def __init__( self, app_name ):
      # parse the file and set the dict to the ivar _dict
      self._dict = Settings.SettingsClass.get_settings( app_name )

    ##
    # creates the settings file path
    @staticmethod
    def settings_file_path( app_name ):
      # get the home path
      from os.path import expanduser
      home_dir = expanduser("~")
      
      # create the settings file name
      fname = "." + app_name + "_settings"

      # return the home_dir + file name
      return home_dir + "/" + fname

    ##
    # @param app_name this variable will determine the name of the settings file
    #
    @staticmethod
    def get_settings( app_name ):
      """ returns a dictionary of the key/value pairs in the file """
      # get the settings path
      settings_path = Settings.SettingsClass.settings_file_path(app_name.replace(' ', '_'))
  
      try:
        # open the settings file 
        settings_fp = open( settings_path, "r" )
      except:
        settings_fp = open( settings_path, "w+" )
        settings_fp.write( 'app_name='+app_name+'\n' )
        settings_fp.close()
        settings_fp = open( settings_path, "r" )

  
      # y = return variable
      y = {}
  
      # get the key value  
      for line in settings_fp:
        # convert it to an array
        pair = line.split('=')
        # get the key and the value
        key = pair[0]
        value = pair[1]
        # store the key value pair in the return variable
        y[key] = value
  
      # close the file pointer
      settings_fp.close()
  
      return y
  
    def save( self ):
      """ method to save the settings dictionary """
      # get the home path
      from os.path import expanduser
      home_dir = expanduser("~")
      
      # create the settings file name
      fname = "." + app_name + "_settings"
      settings_path = home_dir + "/" + fname
  
      # open the settings file 
      settings_fp = open( settings_path, "w+" )

      # print the key/value pair into the settings file
      for key in self._dict:
        print_line = key + '=' + self._dict[key] +'\n'
        settings_fp.write(print_line)

      # close the settings file
      settings_fp.close()
  
    def set( self, key, value, override=False ):
      """ sets a setting """
      try:
        x = self._dict[key]
      except KeyError:
        self._dict[key] = str(value)
  
      if not x == None and override:
        self._dict[key] = value
  
    def get( self, key, default="1312340" ):
      """ gets a setting """
      try: 
        return self._dict[key]
      except:
        return default

