import re,requests,os
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
ua = UserAgent()


class Pastpaper(object):
    def __init__(self):
        """Initial Pastaper Project"""
        super(Pastpaper).__init__()
        self.domain_url = "https://pastpapers.co"
        self.store_palce = "C:/Users/peter/Desktop/pastpaper"
        self.files_pools = []
        self.current_display = [["cie",],"aqa","cces", "ocr"]
        self.office,self.grade,self.year,self.month,self.component = '','','','',''
        self.exam_office = {"cie":["A-Level","IGCSE","O-Level","Pre-U"], "aqa":["A-Level",'GCSE'], "cces":["GCE-A-Level","GCSE"], "ocr":["A-Level",'GCSE']}
        self.home_choose = [['CIE: A-Level','/cie/?dir=A-Level'],['CIE: IGCSE','/cie/?dir=IGCSE'],['CIE: O-Level','/cie/?dir=O-Level'],['CIE: Pre-U','/cie/?dir=Pre-U'],
                    ['AQA: A-Level','/aqa/?dir=A-Level'],['AQA: IGCSE','/aqa/?dir=GCSE'],
                    ['CCES: A-Level','/cces/?dir=A-Level'],['CCES: GCE-A-Level','/cces/?dir=GCE-A-Level'],
                    ['OCR: A-Level','/ocr/?dir=A-Level'],['OCR: IGCSE','/ocr/?dir=GCSE']]
        self.current_display = self.home_choose
        # print("cie","aqa","cces", "ocr")
        # self.office = input('Please input exam office name:')
        # print(self.exam_office.get(self.office,'Error!'))
        # # self.grade = self.exam_office.get(self.office,'Error!')[int(input('Please iuput the courses:'))-1]
        # self.start_dir = '/%s/?dir=%s'%(self.office,self.grade)

        '''
        super(Pastpaper).__init__()
        self.domain_url = "https://pastpapers.co"
        self.store_palce = "C:/Users/peter/Desktop/pastpaper"
        self.exam_office = {"cie":["A-Level","IGCSE","O-Level","Pre-U"], "aqa":["A-Level",'GCSE'], "cces":["GCE-A-Level","GCSE"], "ocr":["A-Level",'GCSE']}
        print("cie","aqa","cces", "ocr")
        self.office = input('Please input exam office name:')
        print(self.exam_office.get(self.office,'Error!'))
        self.grade = self.exam_office.get(self.office,'Error!')[int(input('Please iuput the courses:'))-1]
        self.start_dir = '/%s/?dir=%s'%(self.office,self.grade)
        self.files_pools = []
        self.current_display = self.exam_office
        # for i in ['/cie/?dir=A-Level/Economics-9708/2018-Oct-Nov','/cie/?dir=A-Level/Economics-9708/2019-Oct-Nov','/cie/?dir=A-Level/Economics-9708/2019-May-June','/cie/?dir=A-Level/Economics-9708/2019-March']:
        #     self.dir_content(i)
        '''

    def dir_content(self,dir):
        """ Get content of dir; --> List[contents]"""
        dir = '/cie/?dir=A-Level%2FEconomics-9708'
        current_url = self.domain_url+dir
        headers = {'User-Agent': ua.random}
        proxy = {"http": "127.0.0.1:7890","https": "127.0.0.1:7890"}     
        r = requests.get(current_url,headers)# ,proxies = proxy

        soup = BeautifulSoup(r.text.replace('%2F','/').replace('%26','&').replace('%20',' '),'lxml')
        sel = soup.find_all('a',class_ = "item dir")
        if sel==[]:
            sel = soup.find_all('a',class_ = "item _blank pdf")
            self.current_display = sel
            for i in sel:
                self.files_pools.append([i.get_text().strip(),i['href'][12:]])
            self.single_file_urls()
        else:
            options = []
            for i in sel:
                options.append([i.get_text().strip(),i['href']])
            self.current_display = options
        del r


    def download_file(self,file_name,file_path,file_url):
        headers = {'User-Agent': ua.random}
        proxy = {"http": "127.0.0.1:7890","https": "127.0.0.1:7890"}     
        
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        else:
            if os.path.isfile(file_path+file_name):
                print(file_name,'has downloaded previously!')
                return None
        r = requests.get(file_url,headers,stream = True)# ,proxies = proxy
        if r.status_code == 200:
            with open(file_path+file_name,'wb') as f:
                for block in r.iter_content(chunk_size = 2048):
                    f.write(block)
            print("%s download completely!"%file_path)
        else:
            print("%s can't download!"%file_path)
        del r


    def single_file_urls(self):
        """--> List[files ]; The final files contetns page url; --> List[]"""
        for i in self.files_pools:
            self.download_file(i[0],self.store_palce+i[1].replace('/'+self.office+'/'+self.grade,'').replace(i[0],''),self.domain_url+i[1])
            print('Finsh Downoloaded',i[0])
        self.files_pools.clear
# pa = Pastpaper()
# print(pa.current_display)
# pa.dir_content(1)
# print(pa.current_display)