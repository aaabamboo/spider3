# timeout 参数
'''
import urllib.request

response = urllib.request.urlopen('http://httpbin.org/get',timeout=1)  # if take timeout=0.1，则urlerror.
print(response.status)
print(response.read())
'''

import socket
import urllib.request
import urllib.error

try:
    response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1) #设置timeout参数来实现超时处理。
except urllib.error.URLError as e:
      if isinstance(e.reason,socket.timeout):
        print('TIME OUT')
