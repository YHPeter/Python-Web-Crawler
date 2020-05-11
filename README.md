# Python-Spider

## Project List:
1. The spider programme is designed for catching one complete novel with searching function by name of novel or writer.
2. CIE past paper catching online through website: https://cie.fraft.org/ with **selenium** Library.
3. It is made for collecting the **picture's address** on the [Sina Blog](http://blog.sina.com.cn/), due to cancel the one-click export function.
4. Use the online [Baidu Translate](https://fanyi.baidu.com) to get EN->CN or CN->EN passage with **js/javascript reverse parsing**. The details of js reverse process are in the folder.
5. Use online translation [Youdao Translate](http://fanyi.youdao.com) access **automatic language choice translation**, also support input of terminal or **local txt file** and output in terminal or the previous **txt file without replacement**.
6. The usage of **stream** (break large file into small pieces to avoid take up too musch memory) with **multi-threading** and **http/socks5 proxy** to download large size files such as 8k wallpaper in [Unsplash.com](https://www.unsplash.com).
7. Downloading Chinese novel online with **asynchronous method** shortens the total time. Compared to the single thread and asynchronous method, the second one (approximately 0.05s per chapter) is **faster 10 time than single thread** (approximately 0.5s per chapter). 
~~At the same time, user needs to click the bat file to combine all the single txt files in each independent folders in a different situation.~~ The least version have mixed the combing function without clicking the bat file.
8. As the influence of COVID-19, the updated announcement is related to every candidate who signed for the summer exam. This programme aims to get the updated news from https://www.cambridgeinternational.org/news/ every minute and send the new URL to our emails via **SMTP email**. I have **deployed to the server**, the more details in the folder. [CAIE-Notification](https://github.com/YHPeter/Python-Web-Crawler/tree/master/CAIE-Notification-via-SMTP-Email)

### Basic tools:
The basic and essential function is in the get https website.py file, which can get the https website normally.

## Python爬虫入门小项目
1.  入门级小说爬虫，具有按小说或作者的名字搜索的功能。
2.  爬取CAIE Patpaper从 https://CIE.fraft.org/ 这个网站，通过**selenium库模拟浏览器右键另存为下载PDF文件**。
3.  新浪博客由于取消了一键导出照片功能，这个项目是为在[新浪博客](http://blog.sina.com.cn/)上收集图片地址而制作的。
4.  通过**js逆向**分析**百度翻译**的requests，成功使用[百度翻译](https://fanyi.baidu.com)，可以中译英或英译中。具体js逆向过程可在打开文件夹仔细阅读 README.md！
5.  通过**js逆向**分析**有道翻译**的requests请求，使用在线翻译[有道翻译](http://fanyi.youdao.com) 访问自动语言选择翻译，还支持终端或本地txt文件的输入，并在终端或原来的txt文件中输出，无需替换。
6.  在[Unsplash.com](https://www.unsplash.com) 中使用带有**多线程，http代理和分块(stream)** 来下载8k墙纸等大文件，减少整个文件占用内存的情况。
7.  采用**异步下载**网络小说，缩短总时间。与单线程和异步方法相比，第二种方法（大约每章0.05s）比单线程（大约每章0.5s）**快10倍**。~~同时，用户需要点击bat文件，在不同的情况下将每个独立文件夹中的所有单个txt文件合并。~~最新的版本已经集成合并功能，无需bat文件。具体看代码！
8.  由于COVID-19的影响，CAIE官方的更新公告与每个参加2020夏季考生息息相关。该项目：每分钟从 https://www.cambridgeinternational.org/news/ 获取最新消息，并通过**SMTP电子邮件**地址将新的URL发送到我们的电子邮件。我已**部署服务器**，文件夹中有更多详细信息。[CAIE-Notification](https://github.com/YHPeter/Python-Web-Crawler/tree/master/CAIE-Notification-via-SMTP-Email)

## 希望大家可以Star！Star！Star！I will keep on working!
