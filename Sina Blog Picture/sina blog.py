import requests
import re
import time

def one_page(url):
    img_url=[]
    pattern = [r'<a href="http://blog.photo.sina.com.cn/showpic.html#url=(.*?)" target="_blank">',
        'real_src ="(.*?)&amp;690"',
        r'><a HREF="(.*?)" TARGET="_blank"><img']
    #print(requests.get(url).text)
    img_url=re.findall(re.compile(re.compile(pattern[1])),requests.get(url).text)
    return img_url

def newUrl(previous_url):
    pattern = re.compile('<div><span class="SG_txtb">.*?</span><a href="(.*?)">.*?</a></div>')
    res = requests.get(star_url).text
    try:
        return re.findall(pattern,res)[0]
    except:
        pattern = re.compile(':<a href="(.*?)" class="BNE_lkA">')
        return re.findall(pattern,res)[0]
    #print(re.findall(pattern,res)[0]
def getTitle(star_url):
    pattern=re.compile('<h1 class=".*?" id=".*?">(.*?)</h1>')
    res = requests.get(star_url)
    res.encoding='utf-8'
    res=res.text
    try:
        return re.findall(pattern,res)[0]
    except:
        pattern = re.compile('<h2 id=".*?" class="titName SG_txta">(.*?)</h2>')
        return re.findall(pattern,res)[0]
        
def txt(li):
    for i in li:
        words = str(i)
        print(words) 
        with open(r'result.txt','a',encoding='utf-8') as file_handle: 
            file_handle.write(words) 
            file_handle.write('\n') 
    
if __name__ == "__main__":
    star_url = 'http://blog.sina.com.cn/s/blog_xxxxxxxxxxxx.html'
    for i in range(107):
        print(i+1,'：',getTitle(star_url))
        pic_url = one_page(star_url)
        if pic_url == []:
            pass
        else:
            #print(pic_url)
            txt(pic_url)
        star_url = newUrl(star_url)
    pass