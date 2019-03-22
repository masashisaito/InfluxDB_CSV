from ftp_get_write import *
from ftp_get_write_hpcs import hpcs_get
from configparser import ConfigParser
import os
import socket
from distutils.util import strtobool


# Set TimeoutError default time
socket.setdefaulttimeout(5.0)

# [Config infomations]
pwd = os.path.normpath('%s/../' % __file__)
config_path = os.path.join(pwd, 'config.ini')
config = ConfigParser()
config.read(config_path)

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
        print('\n[%s]' % svs)
        client = FTP_KIT(switch=switch, host=host, user=user, passwd=passwd, remote_file=remote_file, local_file=local_file)
        client.ftp_get()
      except error_perm:
        print('%s: %s 保存する対象のパスを確認してください。' % (host,remote_file))
      except FileNotFoundError:
        print('%s: %s 保存するパスが間違っています。' % (host,local_file))
      except socket.gaierror:
        print('%s: 接続出来ませんでした。' % host)
      except socket.timeout:
        print('%s: タイムアウトでした。' % host)
    except IndexError:
      print("[%s] 内で入力情報が欠損しています。" % svs)

main_ftp()
hpcs_get(config)