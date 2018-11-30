import requests
import os
from bs4 import BeautifulSoup
url = 'https://www.baidu.com'
fp = open('host.txt','r')
ips = fp.readlines()
proxys = list()
for p in ips:
    ip =p.strip('\n').split('\t')
    proxy = 'http:\\' +  ip[0] + ':' + ip[1]
    proxies = {'proxy':proxy}
    proxys.append(proxies)
for pro in proxys:
    try :
        s = requests.get(url,proxies = pro)
        print (s)
    except Exception as e:
        print (e)