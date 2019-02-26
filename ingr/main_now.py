import import_csv
import os
from configparser import ConfigParser

# Path list
pwd = os.path.normpath('%s/../../' % __file__)
config_path = os.path.join(pwd, 'config.ini')
config = ConfigParser()
config.read(config_path)

# Server infomation
client = import_csv.InfluxDB_CSV(
  host='192.168.30.121',
  port=8086,
  username='root',
  password='root',
   # If you don't have a database yet you need to create a new database
  database='KIT_ENERGY'
)

client.import_csv(
  csvfile_path=config.items("HPCS")[5][1],
  measurement=config.items("HPCS")[6][1]
  )