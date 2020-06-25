# -*- coding: utf-8 -*-
import requests
import re,time
from fake_useragent import UserAgent
ua = UserAgent()
headers = ua.random
urls = ["http://www.xbiquge.la/10/10512/{}.html".format(i) for i in range(4541621,4541741)]
start = time.time()
for url in urls:
    headers = ua.random
    content = requests.get(url,headers).content.decode('utf-8')
    title =  re.findall(re.compile('<h1> (.*?)</h1>'),content)
    cont = re.findall(re.compile('<br />&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'),content)
    #print(content)
    try:
        print(title[0],':',cont[0])
    except:
        pass
print(time.time()-start)
