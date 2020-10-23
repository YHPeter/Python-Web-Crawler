# -*- coding: utf-8 -*-
from selenium import webdriver
import time, xlsxwriter,json
from selenium.webdriver.common.keys import Keys

class Web():
    def __init__(self):
        self.number_perpage = 100
        self.number_page = 2
        with open('user.txt') as f:
            username,password = f.readlines()
            self.username = username.replace('username: ','')
            self.password = password.replace('password: ','')

    def Crawl(self):
        driver = webdriver.Chrome('chromedriver.exe')
        driver.get("https://xxxxxxxxx.xxxxxxxxx.xxxxxxxxx/login")
        time.sleep(1)
        driver.find_element_by_id("account").send_keys(self.username)
        driver.find_element_by_id("password").send_keys(self.password)
        driver.find_element_by_id("password").send_keys(Keys.ENTER)
        time.sleep(0.5)

        result = []
        for i in range(self.number_page):
            url = 'https://xxxxxxxxx.xxxxxxxxx.xxxxxxxxx/xxxxxxxxx?xxxxxxxxx=&xxxxxxxxx=&xxxxxxxxx=&xxxxxxxxx=&xxxxxxxxx=&xxxxxxxxx=&offset=%d&limit=%d'
            driver.get(url%(i*self.number_perpage,self.number_perpage))
            time.sleep(0.5)
            js = str(driver.page_source).replace('<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','').replace('</pre></body></html>','')
            print(json.loads(js))
            data = json.loads(js)
            uid = [data['data'][i]['uid'] for i in range(self.number_perpage)]
            for i in range(self.number_perpage):
                driver.get('https://xxxx.xxxxxx.xxxxxx/xxxxxxxx/%s'%uid[i])
                js = str(driver.page_source).replace('<html><head></head><body><pre style="word-wrap: break-word; white-space: pre-wrap;">','').replace('</pre></body></html>','')
                data = json.loads(js)
                xxxxxxxxx = data['xxxxxxxxx']
                xxxxxxxxx = data['xxxxxxxxx']
                xxxxxxxxx = data['xxxxxxxxx']
                xxxxxxxxx = data['xxxxxxxxx']
                xxxxxxxxx = data['xxxxxxxxx']
                numapi = len(xxxxxxxxx)
                curapi = [[xxxxxxxxx[i]['xxxxxxxxx'],xxxxxxxxx[i]['xxxxxxxxx'],xxxxxxxxx[i]['xxxxxxxxx'],xxxxxxxxx[i]['xxxxxxxxx'],xxxxxxxxx[i]['xxxxxxxxx']] for i in range(numapi)]
                xxxxxxxxx = sum([xxxxxxxxx[i][3] for i in range(numapi)])
                result.append([uid[i], xxxxxxxxx,xxxxxxxxx,xxxxxxxxx,xxxxxxxxx,xxxxxxxxx,xxxxxxxxx,sorted(xxxxxxxxx,key=lambda x: x[2])])
        self.result = result
        for x in result:
            print(x)
    
    def saveResult(self):
        result = self.result
        result.sort(key=lambda x: x[6],reverse=True)
        titile = ['ID','xxxxxxxxx','xxxxxxxxx','xxxxxxxxx','xxxxxxxxx','xxxxxxxxx','xxxxxxxxx']+['xxxxxxxxx ID','xxxxxxxxx','xxxxxxxxx','xxxxxxxxx','xxxxxxxxx']*10
        workbook = xlsxwriter.Workbook('Result.xlsx')
        worksheet = workbook.add_worksheet()
        for i in range(len(titile)):
            worksheet.write(0,i,titile[i])
            
        for row in range(len(result)):
            for k in range(7):
                worksheet.write(row+1,k,result[row][k])
            col = 7
            for j in range(int(result[row][5])):
                for k in range(5):
                    worksheet.write(row+1,col,result[row][-1][j][k])
                    col+=1
        workbook.close()

if __name__ == "__main__":
    background = Web()
    background.Crawl()
    background.saveResult()
    
 