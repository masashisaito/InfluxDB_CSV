from import_csv import *
from configparser import ConfigParser
from concurrent.futures import ThreadPoolExecutor

# Path list
pwd = os.path.normpath('%s/../../' % __file__)
config_path = os.path.join(pwd, 'config.ini')
config = ConfigParser()
config.read(config_path)
servers = config.sections()


# Server infomation
influx = InfluxDB_CSV(
  host='192.168.30.121',
  port=8086,
  username='root',
  password='root',
   # If you don't have a database yet you need to create a new database
  database='KIT_ENERGY'
)

influx.import_csv(
  csvfile_path=config.items("HPCS")[5][1],
  measurement=config.items("HPCS")[6][1]
)

def import_exec(influx=influx, sections=None):
  lis = []
  sec_num = len(sections)
  executor = ThreadPoolExecutor(max_workers=sec_num)
  for svs in range(sec_num):
    lis.append('executor.submit(influx.import_csv(csvfile_path=config.items(sections[i])[5][1], measurement=config.items(sections[i])[6][1]))')
  lis = ';'.join(lis)
  return print(lis)

if __name__ == "__main__":
  import_exec(influx, servers)