import requests
import re
import time
def one_page(url):#获取本页图片链接
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
        print(words)       # data是前面运行出的数据，先将其转为字符串才能写入
        with open(r'C:\Users\peter\Desktop\结果存放.txt','a',encoding='utf-8') as file_handle:   # .txt可以不自己新建,代码会自动新建
            file_handle.write(words)     # 写入
            file_handle.write('\n')         # 有时放在循环里面需要自动转行，不然会覆盖上一条数据    
    
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