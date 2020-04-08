# Python-Spider

## Project List:
1. The spider programme is designed for catching one complete novel with searching function by name of novel or writer.
2. The same function as the first one, however, change another website.
3. CIE past paper catching online through website https://cie.fraft.org/ with selenium.
4. It is made for collecting the picture's address on the Sina blog, due to cancel the one-click export function.
5. Use the online Baidu Translate(https://fanyi.baidu.com) to get EN->CN or CN->EN passage with js reverse parsing.
6. Use online translation Youdao Translate(http://fanyi.youdao.com) access automatic language choice translation, also support input of terminal or local txt file and output in terminal or the previous txt file without replacement.
7. The usage of proxy and stream with multi-threading to download large size files such as 8k wallpaper in https://www.unsplash.com.
8. Downloading Chinese novel online with asynchronous method shortens the total time. Compared to the single thread and asynchronous method, the second one (approximately 0.05s per chapter) is faster 10 time than single thread (approximately 0.5s per chapter). 
At the same time, user needs to click the bat file to combine all the single txt files in each independent folders in a different situation.
9. As the influence of COVID-19, the updated announcement is related to every candidate who signed for the jun/July exam series. The programme aims to get the updated news from https://www.cambridgeinternational.org/news/ every minute and send the new URL to our emails via SMTP email address. I have deployed to the server, the more details in folder. [CAIE-Notification-via-SMTP-Email](https://github.com/YHPeter/Python-Web-Crawler/tree/master/CAIE-Notification-via-SMTP-Email)

### Basic tools:
The basic and essential function is in the get https website.py file, which can get the https website normally.
