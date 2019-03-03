from configparser import ConfigParser
from distutils.util import strtobool
from ftp_get_write_proto import *
import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Set TimeoutError default time
socket.setdefaulttimeout(5.0)

config = ConfigParser()
config.read('config.ini')
servers = config.sections()

def ftp_svs():
  svs_lis = []
  for svs in servers:
    switch = strtobool(config.items(svs)[0][1])
    host = config.items(svs)[1][1]
    user = config.items(svs)[2][1]
    passwd = config.items(svs)[3][1]
    remote_file = config.items(svs)[4][1]
    local_file = config.items(svs)[5][1]
    svs_lis.append(FTP_KIT(switch=switch, host=host, user=user, passwd=passwd, remote_file=remote_file, local_file=local_file))
  return svs_lis


def ftp_conlog(ftpob):
  try:
    ftpob.connect()
    print('%s: コネクト成功: ログインします' % ftpob.host)
    try:
      ftpob.login()
      print('%s: ログイン成功' % ftpob.host)
    except error_perm:
      print('%s: ログイン失敗、ユーザ、パスワード情報を確認してください。' % ftpob.host)

  except socket.gaierror:
    print('%s: コネクト失敗、ホスト情報を確認してください。' % ftpob.host)
  except socket.timeout:
    print('%s: コネクト失敗、タイムアウトでした。ホスト情報を確認してください。' % ftpob.host)


def ftp_exec(sections=None):
  lis = []
  sec_num = len(sections)
  executor = ThreadPoolExecutor(max_workers=sec_num)
  for svs in range(sec_num):
    lis.append('executor.submit(ftp_conlog(ftp_svs()[%s]))' % svs)
  lis = ';'.join(lis)
  return exec(lis)


if __name__ == "__main__":
  ftp_exec(servers)
