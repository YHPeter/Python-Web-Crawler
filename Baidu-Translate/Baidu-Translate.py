# -- coding: utf-8 --

from urllib import parse,request
import re
import urllib
import execjs
import gzip

class Baidu_Translate():

    def __init__(self):
        fun_cho = input("CN -> EN Press 1 \nEN -> CN Press 2 \n")
        n=0
        if  fun_cho == str(1):
            from_param = "zh"
            to_param = "en"
            current_url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"
        elif fun_cho == str(2):
            from_param = "en"
            to_param = "zh"
            current_url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
        elif fun_cho == str(0): #exit()
            return exit()
        else:
            print("Default mode: EN -> CN")
            sumary = [fun_cho,"en","zh","https://fanyi.baidu.com/v2transapi?from=en&to=zh"]
            self.Translate(sumary)
            n = 1
            pass
        if n ==0:
            query = str(input("Enter translation: \n"))
            sumary = [query,from_param,to_param,current_url]
            self.Translate(sumary)
        else:
            pass
    def getToken(self):
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"
        }
        con = requests.get("https://fanyi.baidu.com", headers)
        token = re.findall(re.compile("token: '(.*?)',"),con.text)[0]
        return str(token)

    def Translate(self,info_list):
        sign = execjs.compile(open(r"sign.js",'r',encoding='utf-8').read()).call('e',info_list[0])
        headers={
            "Host": "fanyi.baidu.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36",
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding":"gzip, deflate, br",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "https://fanyi.baidu.com",
            "Connection": "keep-alive",
            "Referer": "https://fanyi.baidu.com/",
            "cookie":"PSTM=1578927563; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; BAIDUID=B4D8C06CE2611BC3E9398E26FF4E4256:SL=0:NR=10:FG=1; BIDUPSID=B864A9681F197C9FBC78AEF4A6F24E35; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1582264272,1582334062,1582442179,1582461350; __cfduid=dbc056a2a7ace759e8034bdc68280a10f1582560673; H_PS_PSSID=1456_21121_30824_22159; DOUBLE_LANG_SWITCH=0; to_lang_often=%5B%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; delPer=0; PSINO=7; from_lang_often=%5B%7B%22value%22%3A%22dan%22%2C%22text%22%3A%22%u4E39%u9EA6%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1582976644; __yjsv5_shitong=1.0_7_b9373ab1f52901827727b195984f68ec9674_300_1582976642658_112.0.150.0_bb4e5405; yjs_js_security_passport=7f0cbf275c192d91a1e8c4a23654bd1c4b50b01b_1582976644_js",
        }
        post_param = {  
            "from": info_list[1],
            "to": info_list[2],
            "query": info_list[0],
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": sign,
            "token": "3c7770359299deb6d5def1c1e45140d7",#self.getToken(),
            "domain": "common",
        }
        #print(post_param)
        con = request.Request(info_list[3],bytes(urllib.parse.urlencode(post_param), encoding='utf-8'), headers)
        content = gzip.decompress(request.urlopen(con).read()).decode("utf-8")
        #print(content)
        res = re.findall(re.compile('"dst":"(.*?)","prefixWrap":0,"result',re.S),content)[0] #正则提取trans_result.data[""0""].dst
        print(eval('u"%s"' % res))
while 1:
    fanyi = Baidu_Translate()
