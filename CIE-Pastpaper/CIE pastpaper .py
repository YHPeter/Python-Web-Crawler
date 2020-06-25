# -*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver

web = 'https://cie.fraft.org/'

def download_pdf(lnk,name,t):
    chrome_options = webdriver.ChromeOptions()
    download_folder = "c:\\Users\\Peter\\Desktop"
    profile = {"plugins.plugins_list": [{"enabled": False,
                                         "name": "Chrome PDF Viewer"}],
               "profile.default_content_settings.popups": 0,
               "download.default_directory": download_folder,
               "download.extensions_to_open": ""}

    chrome_options.add_experimental_option("prefs", profile)

    print("Downloading file from link: {}".format(lnk))

    driver = webdriver.Chrome(r"chromedriver.exe", options=chrome_options)
    driver.get(lnk)
    sleep(t)
    driver.find_element_by_xpath('//*[@id="download"]').click()
    sleep(0.1)
    filename = name
    print("File: {}".format(filename))
    print("Status: Download Complete.")
    driver.close()
    driver.quit()
    
objec = 9707 #subject code
season = ['w']#m or s or w 
year = [18] #test year
typ = ['ms','qp']# answer paper or question paper

paper = range(1,7+1)#paper code
con = range(1,3+1)#paper conponent

for s in season:
    for y in year:
        for t in typ:
            for p in paper:
                for c in con:
                    name = str(objec)+'_'+str(s)+str(y)+'_'+str(t)+'_'+str(p)+str(c)+'.pdf'
                    url = web+str(objec)+'_'+str(s)+str(y)+'_'+str(t)+'_'+str(p)+str(c)+'.pdf'
                    download_pdf(url,name,6)
        download_pdf(web+str(objec)+'_'+str(s)+str(y)+'_'+'gt'+'.pdf',str(objec)+'_'+str(s)+str(y)+'_'+'gt'+'.pdf',8)
        download_pdf(web+str(objec)+'_'+str(s)+str(y)+'_'+'er'+'.pdf',str(objec)+'_'+str(s)+str(y)+'_'+'gt'+'.pdf',20)
