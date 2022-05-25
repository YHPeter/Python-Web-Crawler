# Python-Spider (Web Scraping)

## Project List

1. Download Chinese internet novel with searching functions via author and title
2. Download CIE Pastpaper online through website: <https://cie.fraft.org/> with **selenium**
3. Collect the **picture's urls** of the [Sina Blog](http://blog.sina.com.cn/) for downloading to save memory of childhood
4. Use **javascript reverse parsing** to stimulate webpage of [Baidu Translate](https://fanyi.baidu.com) to request translation
5. Use **javascript reverse parsing** to stimulate webpage of [Youdao Translate](http://fanyi.youdao.com) to request translation via terminal or **local txt file**
6. Set **multi-threading** and **http/socks5** proxy to download 8k wallpapers in [Unsplash.com](https://www.unsplash.com) with phrasing its **API** response
7. Download Chinese novel with **asynchronous** method shortens the total time, compared to the first project, **faster *10* times** than single thread (approximately 0.5s per chapter)
8. Get the updated news from <https://www.cambridgeinternational.org/news/> (refreshing every minute) and send an email containing news URL via **SMTP email**
9. Design a GUI window for downloading Pastpaper in [Pastpapers.co](https://pastpapers.co) by **PyQt5** with multithreading downloading module
10. Use the **selenium** to simulate the user login in, then used *get()* method to get HTML version JSON data of a company background system

## Python爬虫入门级项目

1. 入门级单线程网络小说爬虫，具有按小说或作者的名字搜索的功能。
2. 爬取CAIE Patpaper从 <https://CIE.fraft.org/> 这个网站，通过**selenium库模拟浏览器右键另存为下载PDF文件**。
3. 新浪博客由于取消了一键导出照片功能，这个项目是为在[新浪博客](http://blog.sina.com.cn/)上收集图片地址而制作的。
4. 通过**js逆向**分析**百度翻译**的requests，成功使用[百度翻译](https://fanyi.baidu.com) ，可以中译英或英译中。具体js逆向过程可在打开文件夹仔细阅读 README.md！
5. 通过**js逆向**分析**有道翻译**的requests请求，使用在线翻译[有道翻译](http://fanyi.youdao.com) 访问自动语言选择翻译，还支持终端或本地txt文件的输入，并在终端或原来的txt文件中输出，无需替换。
6. 在[Unsplash.com](https://www.unsplash.com) 中使用带有**多线程，http代理和分块(stream)** 来下载8k墙纸等大文件，减少整个文件占用内存的情况。
7. 采用**异步下载**网络小说，缩短总时间。与单线程和异步方法相比，第二种方法（大约每章0.05s）比单线程（大约每章0.5s）**快10倍**。
8. 由于COVID-19的影响，CAIE官方的更新公告与每个参加2020夏季考生息息相关。该项目：每分钟从 <https://www.cambridgeinternational.org/news/> 获取最新消息，并通过***SMTP电子邮件***地址将新的URL发送到我们的电子邮件。已**部署服务器**，文件夹中有更多详细信息。[CAIE-Notification](https://github.com/YHPeter/Python-Web-Crawler/tree/master/CAIE-Notification-via-SMTP-Email)
9. Pastpaper 下载器图形版主要是为了学习Alevel和GCSE的同学开发的，通过实时爬取[Pastpapers.co](https://pastpapers.co)网页和**PyQt5** 的技术实时展示文件夹和试卷内容。支持文件夹打开、浏览器打开，可多文件夹批量下载；同时在下载单个文件时通过requests请求的长度和steam方式下载，获取文件大小和实时的下载进度！通过**多线程**技术，可在下载时完全不影响主界面的运行！每个按键设置了快捷键，大大提升效率！剩余时间模块还有待开发，有任何建议请发issue，感谢！
10. 这个项目是一个公司后台系统的网络爬虫。敏感信息已被隐藏。在这个网站上保存cookie并与请求保持会话是很困难的。因此，我使用**selenium**来模拟用户登录，然后使用get()方法获取HTML版本的JSON数据并清理数据。

## 希望大家可以 Star
