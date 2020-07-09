# Pastpapaer-Downloader-GUI

***[EN]***
This application is designed for ***A-Level and GCSE*** students to get the full subjects pastpaper resource. This software captures this website: [Pastpapers.co](https://pastpapers.co) and display on the mainwindow by **PyQt5** and requests. Functions includes downloading files or erveral folders(deeper three folders), opening files or folders in a browser or local. When clicking the download button, it creates a new thread to download all files or serveral folders(deeper three folders), so mianwindow still can do actions smoothly. Tips: Every button has its own hotkeys, it will incredibly increase efficiency.


***[CN]***
Pastpaper下载器图形版主要是为了学习Alevel和GCSE的同学开发的，通过实时爬取[Pastpapers.co](https://pastpapers.co)网页和**PyQt5** 的技术实时展示文件夹和试卷内容。支持文件夹打开、浏览器打开，可多文件夹批量下载；同时在下载单个文件时通过requests请求的长度和steam方式下载，获取文件大小和实时的下载进度！通过**多线程**技术，可在下载时完全不影响主界面的运行！每个按键设置了快捷键，大大提升效率！剩余时间模块还有待开发，有任何建议请发issue，感谢！

Actually, in the website, we change the url by deleting ```/cie/view.php?id= ```
```
Previously: https://pastpapers.co/cie/view.php?id=/cie/.../9706_s03_er.pdf --> html

Change to: https://pastpapers.co/cie/.../9706_s03_er.pdf  --> PDF file!!!!
```

Then we can download the PDF files. So during single file downloading,  by knowing the *content length* from requests with steam, the progress bar can actually show the actual percentage of this file has downloaded.