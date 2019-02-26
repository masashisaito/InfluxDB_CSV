import encode_csv
import import_csv
import os
from tqdm import tqdm
from configparser import ConfigParser

# Server infomation
client = import_csv.InfluxDB_CSV(
  host='192.168.30.121',
  port=8086,
  username='root',
  password='root',
  # If you don't have a database yet you need to create a new database
  database='mydb_mac'
  )

# Infomation of CSV_file.
logs = '/Users/Daiki/Desktop/research/log'
encoded_logs = '/Users/Daiki/Desktop/research/log_encoded'
hpcs_measurement = 'hpcs'

# Run the Encoding program.
encode_csv.encode_csv(logs, encoded_logs)

# Touch the import_list in current directory.
import_csv.touch_import_list(path_list=None, measurement=hpcs_measurement)

csv_dir = import_csv.diff_imported(encoded_logs, hpcs_measurement)
path_list = os.path.dirname(__file__)

for file in csv_dir:
  print('starting', file)
  file_path = os.path.join(encoded_logs, file)
  client.import_csv(file_path, hpcs_measurement)
  print(file, 'done')
  with open("%s/import_file_list_%s.csv" % (path_list, hpcs_measurement), "a") as w:
    w.write(file + "\n")
