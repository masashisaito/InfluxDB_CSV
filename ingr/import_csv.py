from influxdb import InfluxDBClient
import os
from pathlib import Path
import csv
from tqdm import tqdm

# Extended class of import_csv()
class InfluxDB_CSV(InfluxDBClient):
    # import_csv method is Convert CSV file to InfluxDB's point and write the point!
    def import_csv(self, csvfile_path, measurement):
      print('Start import: %s' % csvfile_path)
      # Open the csvfile.
      with open(csvfile_path, 'r', newline='') as csv_file:
        # Convert CSV to List type.
        reader = csv.reader(csv_file)
        reader = list(reader)
        # Set CSV's infomations. reader[0] -> CSV's header row. reader[1] -> CSV's rows other than the first row.
        fields = reader[0]
        # value = reader[1]
        row_length = len(reader)
        columun_length = len(fields)
        # Set tqdm preparation.
        rows = tqdm(range(1, row_length))

      # Encoding csvfile to InfluxDB's point, and write there points.
      for i in rows:
        value = reader[i]
        rows.set_description("Importing %s" % i)
        # Read csvfile of columun's length, and convert { fields[0]:value[0] } list.
        columun_list = {}
        for i in range(1, columun_length):
          columun_list[fields[i]] = value[i]
        # Convert CSV to InfluxDB's point
        import_array = [
          {
            "measurement": measurement,
            # UTC => T00:00Z, JST => T00:00+09:00
            "time": value[0].replace('/', '-').replace(' ', 'T').replace('.0', '+09:00'),
            "fields": columun_list
          }
        ]
        # Write there points !
        self.write_points(import_array)

# Touch import_file_list.csv in path_ingr.
def touch_import_list(path_list=os.path.dirname(__file__)):
  if "import_file_list.csv" not in os.listdir(path_list):
    Path("%s/import_file_list.csv" % path_list).touch()
    print('インポートリストの作成をします。')
  else:
    print('既存のimport_file_list.csvを使用します。')
  print('ファイルパスは: %s/import_file_list.csv です。' % path_list)

# Diff import_csvfile_list and the csvfile you are importing.
def diff_imported(path_logs):
  before_import_list = os.listdir(path_logs)
  with open("import_file_list.csv", "r") as r:
    imported_list = r.read().split()
  set_imported = set(before_import_list) - set(imported_list)
  return set_imported

# client = InfluxDB_CSV(
#   host='192.168.30.121',
#   port=8086,
#   username='root',
#   password='root',
#   database='mydb_mac'
#   )

# csv_path = 'log/20180908_235959_0000000E.CSV'
# client.import_csv(csv_path, 'hpcs')