# -*- coding: utf-8 -*-
import requests
import urllib

def getHTMLText(url):
    try:
        ssl._create_default_https_context = ssl._create_stdlib_context #the most important step
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
        req = urllib.request.Request(url, headers=headers)
        web_page = urllib.request.urlopen(req)
        return web_page.read().decode('utf-8')
    except Exception as e:
        return e

if __name__=="__main__":
    url ="www.google.com"
    print(getHTMLText(url))
