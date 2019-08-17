import requests
def getHTMLText(url):
    try:
        x=requests.get(url,timeout=30)
        r.raise_for_status() #，引发HTTPExror异常
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
if __name__=="__main__":
    url ="http://www.baidu.com"
    print(getHTMLText(url))
