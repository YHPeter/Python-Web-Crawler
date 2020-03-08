# -*- coding: utf-8 -*-

from selenium import webdriver
import requests,time,re,os
from threading import Thread
import threading
from selenium.webdriver.chrome.options import Options


def save_image(url,filename):
    filename = r'D:/pictures/%s.jpg'%filename #pictures storing places
    # filename = filename.replace(' ','-')
    if os.path.isfile(filename):
        print(filename,'has downloaded previously!')
    else:
        print(filename,'is downloading!')
        # proxy = {"http": "socks5://127.0.0.1:1082","https": "socks5://127.0.0.1:1082"}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'}
        r = requests.get(url,headers=headers,stream=True)#stream download on # proxies=proxy optional for using proxy
        if r.status_code == 200:    # print(r.status_code)
            with open(filename,'wb') as f:
                for block in r.iter_content(chunk_size = 1024):
                    f.write(block)
            print("%s download completely!"%filename)
        else:
            print("%s can't download!"%filename)
        del r
    # print('--------------') markers


def thread_download(save_image,url_list):# if the network speed is fast enough, can use threading
    threads = []
    for i in url_list:#list = [(,)]
        #Create 
        t = Thread(target = save_image, args = [i[1],i[0]])
        # t.setDaemon(True)
        t.start()
        threads.append(t)
        # t.join()
    # print('thread_download',threading.current_thread())
    for t in threads:
        t.join()


def urls_pool():
    url_list = []
    # proxy = {"http": "socks5://127.0.0.1:1080","https": "socks5://127.0.0.1:1080"}
    for i in range(10): #get ten page images
        url = 'https://unsplash.com/napi/landing_pages/backgrounds?page=%d&per_page=20'%i #can change the unsplash url for different themes
        content = requests.get(url)# proxies=proxy optional for using proxy
        content = content.text.replace('?ixlib=rb-1.2.1','')
        url_list = url_list + re.findall(re.compile(r'"alt_description":"(.*?)","urls":{"raw":"(.*?)","full"'),content)
    return url_list

def download(list1):
    n=1 # '1' ----> single thread # '2'---> multithreading
    '''
    Single thread is for low connection speed to https://unsplash.com
    such as me, in China, I have to use proxy;

    Multithreading is for high connection speed to https://unsplash.com
    it will has more advantages when downloading.
    '''
    if n==1:
        for i in list1:
            save_image(i[1],i[0])
    else:
        thread_download(save_image,list1)
if __name__ == "__main__":
    pool_urls = urls_pool()
    print(len(pool_urls))
    start = time.time()
    download(pool_urls)
    total_time = time.time()-start
    print(total_time)#Get total downloading time
