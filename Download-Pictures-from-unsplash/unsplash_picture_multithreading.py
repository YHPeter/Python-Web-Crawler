# -*- coding: utf-8 -*-

import requests,time,re,os
from threading import Thread
import threading

def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start = time.time()
        value = func(*args, **kwargs)
        print(f"Finished {func.__name__!r} in {time.time()-start:.5f} secs")
        return value
    return wrapper_timer

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
        if r.status_code == 200:
            with open(filename,'wb') as f:
                for block in r.iter_content(chunk_size = 1024):
                    f.write(block)
            print("%s download completely!"%filename)
        else:
            print("%s can't download!"%filename)
        del r


def thread_download(save_image,url_list):# if the network speed is fast enough, can use threading
    threads = []
    for i in url_list:
        t = Thread(target = save_image, args = [i[1],i[0]])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

@timer
def urls_pool(api_url):
    url_list = []
    # proxy = {"http": "socks5://127.0.0.1:1080","https": "socks5://127.0.0.1:1080"}

    for i in range(10): #get ten page images
        url = api_url%i #can change the unsplash url for different themes
        content = requests.get(url).text.replace('?ixlib=rb-1.2.1','')# proxies=proxy optional for using proxy
        url_list = url_list + re.findall(re.compile(r'"alt_description":"(.*?)","urls":{"raw":"(.*?)","full"'),content)

    print('Total picture urls in pool:',len(url_list))
    return url_list


@timer
def download(url_pool,method):
    '''
    (url_pool [List], download_method) 1 ----> single thread; 2 ---> multithreading

    Single thread is for low connection speed to https://unsplash.com
    such as me, in China, I have to use proxy;

    Multithreading is for high connection speed to https://unsplash.com
    it will has more advantages when downloading.
    '''
    if method=='single_thread':
        for i in url_pool:
            save_image(i[1],i[0])
    elif method=='multithreading':
        thread_download(save_image,url_pool)
if __name__ == "__main__":
    pool_urls = urls_pool('https://unsplash.com/napi/landing_pages/backgrounds?page=%d&per_page=100')# Notice page=%d should add

    start = time.time()
    download(pool_urls,'single_thread') # 1 ----> single_thread; 2 ---> multithreading
    
    total_time = time.time()-start
    print(total_time)# Get total downloading time