import encode_csv
from import_csv import InfluxDB_CSV


client = InfluxDB_CSV_IMP(
  host='192.168.30.121',
  port=8086,
  username='root',
  password='root',
  database='mydb_mac'
  )

save_file_path = InfluxDB_CSV_ENC(
  b_enc='/Users/Daiki/Desktop/research/log'
  a_enc='/Users/Daiki/Desktop/research/log_encoded'
)

csv_path = 'log/20180908_235959_0000000E.CSV'
client.import_csv(csv_path, 'hpcs')