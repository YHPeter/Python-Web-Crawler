# -*- coding: utf-8 -*-
# # novel_download with asynchronous library

'''
Summary for some novel book station re pattern:

Chnage the regular expression pattern for different novel besite:
In "http://www.ibqg5200.com"
url list and title pattern = '<li><a href="(.*?)">(.*?)</a></li>'
content pattern = '&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'


In "http://www.xbiquge.la"
&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br /><br />
"<dd><a href='(.*?)' >(.*?)</a></dd>"

In "https://www.126shu.co/79497/",
'<dd><a href="(.*?)">(.*?)</a></dd>'
&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />

In 'https://www.abcxs.com/book/28191/'

'''
import aiohttp,asyncio
import re,os,time,requests,shutil
from fake_useragent import UserAgent
ua = UserAgent()
headers = ua.random


async def get(session,url):
    async with session.get(url) as response:
        return await response.text()
        asyncio.sleep()


async def write_file(novel_content,title,filename):
    content = re.findall(re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />'),novel_content)# change the re pattern for each chapter
    with open(filename,'w',encoding='utf-8') as f:
        f.writelines(title+'\n')
        for k in content:
            f.writelines(k+'\n')
        f.writelines('\n')
        f.close()
    print(title,'download completely!')
        

async def main_process(url,title,index,semaphore,file_adress):
    #print(url,title,index)
    filename = file_adress + str(str(index).zfill(5)) + '.txt' # make sure combine in order
    if os.path.isfile(filename):
        print(title,'has downloaded previously!')
    else:
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                novel_content = await get(session, 'http://www.biquge.tv/'+url)# change to the main website url
                # print(novel_content)
            await write_file(novel_content,title,filename)

def merge_txt(floder):
    new_file = re.findall('(.*?)//$',floder)[0]
    k = open(new_file+'.txt', 'w',encoding = 'utf-8')
    for parent, dirnames, filenames in os.walk(floder):
        for floder in filenames:
            txtPath = os.path.join(parent, floder)
            f = open(txtPath,encoding = 'utf-8').read()
            k.write(f+"\n")
        k.close()

def urlPool(book_index,pattern):
    urls_list=requests.get(book_index,ua.random).content
    urls_list=str(urls_list,'gbk',errors = 'ignore')#sometimes will change to 'utf-8'
    urls = re.findall(re.compile(pattern),urls_list)
    return urls #[(url,chapter_title)]


if __name__ == '__main__':
    start1 = time.time() #count seconds
    urls = urlPool(r"http://www.biquge.tv/0_3/",'<dd><a href="(.*?)">(.*?)</a></dd>') # get url pools(url,re.pattern)
                                                                                               # change the re pattern for content list
    print(urls)
    folder_adress = "//雪域兵王//"
    try:
        if os.path.exists(folder_adress):
            pass
        else:
            os.mkdir(folder_adress)
    except:
        pass
    semaphore = asyncio.Semaphore(500) # Limit concurrency to 500 in windows; if content get nothing, derease the number, thw website can't bear....
    tasks = [asyncio.ensure_future(main_process(url[0],url[1],index,semaphore,folder_adress)) for index,url in enumerate(urls)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    print("Starting combine!")
    merge_txt(folder_adress)
    shutil.rmtree(folder_adress)
    print('Total time:',(time.time()-start1),'s','Time for each chapter:',(time.time()-start1)/len(urls),'s')

    