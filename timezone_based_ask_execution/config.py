from configparser import ConfigParser 
import os
config = ConfigParser()
config.read(os.environ['CONFIG_PATH'] + '/config.ini')
  