from ftp_get_write import *
import configparser
from datetime import datetime
import time
from distutils.util import strtobool

# [Config infomations]
config = configparser.ConfigParser()
config.read('config.ini')
# All server list
server = config.sections()

# HPCS's FTP infomation
HPCS_host = config.items("HPCS")[1][1]
HPCS_user = config.items("HPCS")[2][1]
HPCS_passwd = config.items("HPCS")[3][1]
HPCS_remote_file = datetime.now().strftime("%Y/%m/%d").replace("/", "-") + ".csv"
HPCS_local_file = config.items("HPCS")[5][1]
HPCS_client = FTP_KIT(host=HPCS_host, user=HPCS_user, passwd=HPCS_passwd, remote_file=HPCS_remote_file, local_file=HPCS_local_file)
HPCS_client.ftp_get()

for svs in server:
  try:
    # Configparser "TRUE" is str => bool
    switch = strtobool(config.items(svs)[0][1])
    host = config.items(svs)[1][1]
    user = config.items(svs)[2][1]
    passwd = config.items(svs)[3][1]
    remote_file = config.items(svs)[4][1]
    local_file = config.items(svs)[5][1]
    client = FTP_KIT(switch=switch, host=host, user=user, passwd=passwd, remote_file=remote_file, local_file=local_file)
    client.ftp_get()
  except IndexError:
    print("[%s] 内で入力情報が欠損しています。" % svs)