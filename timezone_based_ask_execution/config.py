from configparser import ConfigParser 
import os
config = ConfigParser()
config.read(os.environ['CONIFG_PATH'] + '/config.ini')
  