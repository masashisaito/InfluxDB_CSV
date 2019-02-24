# InfluxDB_CSV
## Overview
### It consists of 3 PKG
* ftp_get_write.py  
  FTP necessary CSV　remote_file => local_file
  
* encode_csv.py  
  Encode CSV　ShiftJIS => UTF-8
  
* import_csv.py  
  Import CSV　.CSV => InfluxDB

### How to use
- Describe in Config.ini
- ```cron -e```  
```* * * * * python3 main.py```
## Config.ini
[SERVERNAME]  
switch = True  
host = hostname  
user = username  
passwd = password  
remote_file = Files on the FTP server  
local_file = Path of file to save  

