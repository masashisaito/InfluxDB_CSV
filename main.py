from ftp_get_write import *
from ftp_get_write_hpcs import hpcs_get
import configparser
import socket
from distutils.util import strtobool

# Set TimeoutError default time
socket.setdefaulttimeout(5.0)

# [Config infomations]
config = configparser.ConfigParser()
config.read('config.ini')

# All server list
server = config.sections()

def main_ftp():
  for svs in server:
    try:
      # Configparser "TRUE" is str => bool
      switch = strtobool(config.items(svs)[0][1])
      host = config.items(svs)[1][1]
      user = config.items(svs)[2][1]
      passwd = config.items(svs)[3][1]
      remote_file = config.items(svs)[4][1]
      local_file = config.items(svs)[5][1]
      try:
        client = FTP_KIT(switch=switch, host=host, user=user, passwd=passwd, remote_file=remote_file, local_file=local_file)
        client.ftp_get()
      except socket.gaierror:
        print('%s に接続出来ませんでした。' % host)
      except socket.timeout:
        print('%s はタイムアウトでした。' % host)
    except IndexError:
      print("[%s] 内で入力情報が欠損しています。" % svs)

main_ftp()