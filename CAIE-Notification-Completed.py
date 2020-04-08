# -*- coding: utf-8 -*-
import re,requests,time
from email.mime.text import MIMEText
from email.header import Header
import smtplib
def send_mail(info):
    message ='''CAIE Publish Least News!!!
The new website is:
'''+info
    msg = MIMEText(message,'plain','utf-8')
    msg['Subject'] = Header("CAIE NOTIFICATION",'utf-8')
    msg['From'] = Header('xxxx@xxxx.com')
    msg['To'] = Header('Who','utf-8')
    
    from_addr = 'peter@petertown.ml' #sending mail adress
    password = 'PeterTown123456'     #sending mail password
    to_addr = 'XXXXXXXXXXXX' #recesiving mail adress
    smtp_server = 'smtpdm.aliyun.com' #your smtp service provider adress
    
    
    try:
        server = smtplib.SMTP_SSL(smtp_server,465) #465 -> ssl, 25->no ssl
        server.login(from_addr,password) #log in email
        server.sendmail(from_addr,to_addr,msg.as_string())  #convert msg into string and send
        server.quit()
        print("Sent Successfully")
    except smtplib.SMTPException as e:
        print("Sent failed, resason is: ",e)
        
if __name__ == '__main__':
    headers = {"Referer": "https://www.cambridgeinternational.org/assets/css/style.css?v=2.2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}
    res = requests.get('https://www.cambridgeinternational.org/news/',headers = headers).content.decode('utf-8')
    v = set()
    all_url = re.findall('<h3><a href="(.*?)" >(.*?)</a></h3>',res)
    for i in all_url:
        url = "https://www.cambridgeinternational.org"+i[0]
        v.add(url)
    while 1:
        res = requests.get('https://www.cambridgeinternational.org/news/',headers = headers).content.decode('utf-8')
        all_url = re.findall('<h3><a href="(.*?)" >(.*?)</a></h3>',res)
        for i in all_url:
            url = "https://www.cambridgeinternational.org"+i[0]
            if url in v:
                localtime = time.asctime( time.localtime(time.time()) )
                print(localtime +i[1]+'is a old news.')
            else:                
                send_mail(url)# title url
                v.add(url)
        time.sleep(60) #every one minite run this file
