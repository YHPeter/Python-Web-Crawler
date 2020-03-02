
import gzip,re,time,hashlib
import requests, random, json
from fake_useragent import UserAgent

def main(func,adr):
    if func == 1:
        query = str(input("Please enter words:\n"))
        translate_m(query,1)
    elif func == 2:
        for line in open(adr,'r',encoding='utf-8').readlines():
            tran_str = translate_m(line,2)
            print(tran_str)
            try:
                with open(adr,'a',encoding='utf-8') as f:
                    f.writelines(tran_str)
                    f.write("\n")
                f.close()
            except:
                pass


def translate_m(query,mode):
    if query == '\n' or None:
        return None
    ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"

    ua_md5 = ua.replace('Mozilla/','')

    bv = hashlib.md5(ua.encode("utf-8")).hexdigest()

    ts = int(time.time()*1000)

    salt = int((ts+random.random())*10)

    sign = hashlib.md5(("fanyideskweb" + query + str(salt) + "Nw(nmmbP%A-r6U3EUn]Aj").encode("utf-8")).hexdigest()
    headers={
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":'_ntes_nnid=7b34edbd2a4d37836b3a07492e9974cd,1580549696317; OUTFOX_SEARCH_USER_ID_NCOO=15956253.730198728; OUTFOX_SEARCH_USER_ID="1669298088@10.108.160.18"; JSESSIONID=aaaxa3eC1ctHM_uPC9ucx; SESSION_FROM_COOKIE=unknown',
    "Host":"fanyi.youdao.com",
    "Origin":"http://fanyi.youdao.com",
    "Referer":"http://fanyi.youdao.com/",
    "User-Agent":ua,
    "X-Requested-With":"XMLHttpRequest",
    "smartresult":"dict",
    "smartresult":"rule",
    }

    param={
    "i":query,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":salt,
    "sign":sign,
    "ts":ts,
    "bv":bv,
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_CLICKBUTTION",
    }

    res = requests.post("http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule",data = param,headers = headers)
    content = json.loads(res.text)
    origin, translated = '',''
    for f in content['translateResult'][0]:
        origin = (origin + f['src'])
        translated = (translated + f['tgt'])
    if mode == 1:    
        print('Origin:',origin,'\n'+'Translated:',translated)
    else:
        print('Origin:',origin,'\n'+'Translated:',translated)
        return translated

if __name__ == "__main__":
    main(2,r'text.txt')
    #Terminal Output ->1 
    #File Output -> 2 with file adress
    pass
