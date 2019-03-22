from ftp_get_write import *
import configparser
from datetime import datetime
import time
import socket

# Set TimeoutError default time
socket.setdefaulttimeout(5.0)

# [Config infomations]
config = configparser.ConfigParser()
config.read('config.ini')

# Function of FTP to HPCS
def hpcs_get(config):
  try:
    # HPCS's FTP infomation
    HPCS_host = config.items("HPCS")[1][1]
    HPCS_user = config.items("HPCS")[2][1]
    HPCS_passwd = config.items("HPCS")[3][1]
    HPCS_remote_file = datetime.now().strftime("%Y/%m/%d").replace("/", "-") + ".csv"
    HPCS_local_file = config.items("HPCS")[5][1]
  except:
    pass
  try:
    print('\n[HPCS]')
    HPCS_client = FTP_KIT(host=HPCS_host, user=HPCS_user, passwd=HPCS_passwd, remote_file=HPCS_remote_file, local_file=HPCS_local_file)
    HPCS_client.ftp_get()
  except error_perm:
    print('%s: %s 保存する対象のパスを確認してください。' % (HPCS_host, HPCS_remote_file))
  except FileNotFoundError:
    print('%s: %s 保存するパスが間違っています。' % (HPCS_host, HPCS_local_file))
  except socket.gaierror:
    print('%s: 接続出来ませんでした。' % HPCS_host)
  except socket.timeout:
    print('%s: タイムアウトでした。' % HPCS_host)
  except socket.gaierror:
    print('%s に接続出来ませんでした。' % HPCS_host)
  except UnboundLocalError:
    print('HPCSキーがないため、HPCS機能をオフにします。')

if __name__ == "__main__":
    hpcs_get(config)