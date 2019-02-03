import os
from ftplib import FTP
import time
import datetime

# PATH's infomations
local_path = "./log"
server_path = "LOGGING/LOG01/"

# Server's infomations
server = FTP(host='172.24.7.234', user='pssp01', passwd='15507')

# 'diff local server'の結果をリスト化して格納
def diff_local_server(server, server_path, local_path):
  '''
  FTP instance, server path of the directory to save, local path
  As an argument and returns a list of non-local files.
  '''
  # 現在のローカル上の'ls'の結果をリスト化して格納
  local_files = [f.name for f in os.scandir(local_path)]
  # 現在のサーバ上の'ls'の結果をリスト化して格納
  server_dir = server.nlst(server_path)[3:]
  server_files = []
  for i in server_dir:
    # listにlistを追加させるのでapendではなくextendになる箇所が注意
    server_files.extend(server.nlst(server_path + i)[3:])
  set_local_server = set(server_files) - set(local_files)
  return print(list(set_local_server))

diff_local_server(server, server_path, local_path)