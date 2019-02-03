from ftplib import FTP
import time

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

filename = '2019-02-01.csv'
hpcs = FTP(host="172.24.7.233", user='hpcs01', passwd='15507')
ftp_get(hpcs, filename)