import socket
import sys
import time
from ftplib import FTP, error_perm
from socket import _GLOBAL_DEFAULT_TIMEOUT


# 処理時間計測のためのデコレータ
def stopwatch(func):
  def wrapper(*args, **kwargs):
    print('処理を開始します。')
    start = time.time()
    func(*args, **kwargs)
    total_time = time.time() - start
    print('処理を終了しました。トータルタイムは:{0}'.format(total_time)+"[sec]です。")
  return wrapper

@stopwatch
# ftpしてファイルを取得する関数
def ftp_get(host, filename):
  with open('./log/hpcs.csv', 'wb') as f:
    print('getting %s' % filename)
    host.retrbinary('RETR %s' % filename, f.write)
    print("hpcs.csv done")


class FTP_KIT(FTP):
  def __init__(self, switch=True, host=None, user=None, passwd=None, remote_file=None, local_file=None,  acct='',
                 timeout=_GLOBAL_DEFAULT_TIMEOUT, source_address=None):
    self.switch = switch
    self.host = host
    self.user = user
    self.passwd = passwd
    self.remote_file = remote_file
    self.local_file = local_file
    self.source_address = source_address
    self.timeout = timeout
  def login(self, user='', passwd='', acct=''):
    # '''Login, default anonymous.'''
    '''Login, default self'''
    if not user:
      user = self.user
    if not passwd:
      passwd = self.passwd
    if not acct:
      acct = ''
    resp = self.sendcmd('USER ' + user)
    if resp[0] == '3':
      resp = self.sendcmd('PASS ' + passwd)
    if resp[0] == '3':
      resp = self.sendcmd('ACCT ' + acct)
    if resp[0] != '2':
      raise error_reply(resp)
    return resp
  def ftp_get(self):
    try:
      if self.switch == 0:
        print('%s がFalseになっています。' % self.host)
      else:
        with open(self.local_file, 'wb') as f:
          self.retrbinary('RETR %s' % self.remote_file, f.write)
          print('%s done' % self.remote_file)
          print('Getting Success!!')
    except socket.gaierror:
      return print('%s に接続出来ませんでした。' % self.host)

if __name__ == "__main__":
  client = FTP_KIT(
    switch=False,
    host='172.24.7.227',
    user=' ',
    passwd=' ',
    remote_file='LOGGING/LOG01/LOG01.CSV',
    local_file='biomus.csv'
    )
  client.ftp_get()


# For Example...
# filename = '2019-02-01.csv'
# hpcs = FTP(host="172.24.7.233", user='hpcs01', passwd='15507')

# ftp_get(hpcs, filename)
