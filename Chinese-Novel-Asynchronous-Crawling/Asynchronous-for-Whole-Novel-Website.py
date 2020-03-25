# -*-utf-8-*-
#novel_download with asynchronous library
'''
Chnage the regular expression pattern for different novel besite:
In "http://www.ibqg5200.com"
url list and title pattern = '<li><a href="(.*?)">(.*?)</a></li>'
content pattern = '&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'


In "http://www.xbiquge.la"
&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /><br />
url list and title pattern = "<dd><a href='(.*?)' >(.*?)</a></dd>"

In "https://www.126shu.co/79497/",
'<dd><a href="(.*?)">(.*?)</a></dd>'
&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />

In "https://www.52bqg.com/"
"<dd><a href='(.*?)' >(.*?)</a></dd>"
'&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'
'''

import aiohttp,asyncio
import re,os,time,requests,shutil
import random
from fake_useragent import UserAgent
ua = UserAgent()
headers = ua.random


async def get(session,url):
    async with session.get(url) as response:
        return await response.text()
        #asyncio.sleep()


async def write_file(novel_content,title,filename):
    content = re.findall(re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'),novel_content)
    with open(filename,'w',encoding='utf-8') as f:
        f.writelines(title+'\n')
        for k in content:
            f.writelines(k+'\n')
        f.writelines('\n')
        f.close()
    print(title,'download completely!')
        

async def main_process(url,title,index,semaphore,file_adress):
    print(url,title,index)
    filename = file_adress + str(str(index).zfill(5)) + '.txt'
    # if os.path.isfile(filename):
    #     print(title,'has downloaded previously!')
    # else:
    if os.path.isfile(filename):
        print(title,'has downloaded previously!')
    else:
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                novel_content = await get(session, url)# change to the main website url
                # print(novel_content)
            await write_file(novel_content,title,filename)


def urlPool(book_index,pattern):
    urls_list=requests.get(book_index).content
    urls_list=str(urls_list,'gbk',errors = 'ignore').replace("'",'"')#or 'utf-8'
    urls = re.findall(re.compile(pattern),urls_list)
    book_name = re.findall(re.compile('<h1>(.*?)</h1>'),urls_list)
    urls.extend(book_name)
    return urls #[(url,chapter_title),book-name][-1]


def merge_txt(floder):
    new_file = re.findall('(.*?)//$',floder)[0]
    k = open(new_file+'.txt', 'w',encoding = 'utf-8')
    for parent, dirnames, filenames in os.walk(floder):
        for floder in filenames:
            txtPath = os.path.join(parent, floder)
            f = open(txtPath,encoding = 'utf-8').read()
            k.write(f+"\n")
        k.close()


def main():
    book_urls = [("https://www.52bqg.com/book_"+str(i)+'/') for i in range(1,10)]
    print(book_urls)
    for info in book_urls:
        start1 = time.time() #count seconds
        urls = urlPool(info,'<dd><a href="(.*?)">(.*?)</a></dd>')#"<dd><a href='(.*?)' >(.*?)</a></dd>"
        file_adress = 'your file adress'+urls[-1]+'//'
        file_name_txt = 'your file adress'+urls[-1]+'.txt'
        print(file_adress)
        if os.path.exists(file_name_txt):
            pass
        else:
            try:
                if os.path.exists(file_adress):
                    pass
                else:
                    os.mkdir(file_adress)
            except:
                pass
            semaphore = asyncio.Semaphore(500) # Limit concurrency to 500 in windows; if content get nothing, derease the number, thw website can't bear....
            tasks = [asyncio.ensure_future(main_process(info+url[0],url[1],index,semaphore,file_adress)) for index,url in enumerate(urls[0:-1])]
            loop = asyncio.get_event_loop()
            loop.run_until_complete(asyncio.wait(tasks))

            print("Starting combine!")
            merge_txt(file_adress)
            shutil.rmtree(file_adress)

            print('Total time for this book:',(time.time()-start1),'s')#,'Time for each chapter:',(time.time()-start1)/len(urls),'s')

if __name__ == '__main__':
    main()