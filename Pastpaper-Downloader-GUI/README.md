# Pastpapaer-Downloader-GUI


This application is designed for A-Level and GCSE students to get the full pastpaper resource with mutl-downloading folders and files from this website: [Pastpapers.co](https://pastpapers.co)

Actually, in the website, we change the url by deleting ```/cie/view.php?id= ```
```
Previously: https://pastpapers.co/cie/view.php?id=/cie/.../9706_s03_er.pdf 

Change to: https://pastpapers.co/cie/.../9706_s03_er.pdf 
```

Then can get the PDF files. So during single file downloading,  by knowing the content length from requests with steam, the progress bar can actually show the actual percentage of this file has downloaded.