# https://www.biquyun.com
# author: Yu Hao
# code: utf-8

import re
import ssl
import urllib.request
import time
import os
import random
from bs4 import BeautifulSoup


def get_web_page(url):
    ssl._create_default_https_context = ssl._create_stdlib_context
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ''Chrome/51.0.2704.63 Safari/537.36'}
    req = urllib.request.Request(url, headers=headers)
    web_page = urllib.request.urlopen(req)
    return web_page.read().decode('gbk')


def reindent(s):
    leading_space = 2 * '　'
    lines = [leading_space + line.strip()
             for line in s.splitlines()]
    return '\n'.join(lines)


def search_book(name):
    name = str(name.encode("gbk"))
    name = name.replace(r'\x', '%')
    name = name.replace("b'", "")
    name = name.replace("'", "")
    novel_source = get_web_page("https://www.biquyun.com/modules/article/soshu.php?searchkey=+%s" % (name))
    soup = BeautifulSoup(novel_source, "lxml")
    tr = soup.find_all("tr", id="nr")
    print("搜素结果")
    if not tr:
        print("没有找到相关的书籍")
        main()
    else:
        print("{:　^10}\t{:　^5}\t{:　^8}\t{:　^1}\t{:　^2}".format("文章名称", "作者", "字数", "更新", "状态"))
        novel_url = re.findall(r'<td class="odd"><a href="(.*?)">.*?', novel_source, re.S)
        novel_name_author = re.findall(r'<td class="odd"><a href=".*?">(.*?)</a></td>.*?<td class="odd">(.*?)</td>',
                                       novel_source, re.S)
        novel_number = re.findall('\d+K', novel_source, re.S)
        novel_refresh = re.findall(r'<td class="odd" align="center">(.*?)</td>', novel_source, re.S)
        novel_value = re.findall(r'<td class="even" align="center">(.*?)</td>', novel_source, re.S)
        for i in range(len(novel_number)):
            print(i + 1,
                  "{:　^10}\t{:　^5}\t{:　^8}\t{:　^1}\t{:　^2}".format(novel_name_author[i][0], novel_name_author[i][1],novel_number[i], novel_refresh[i], novel_value[i]))
        index = int(input("输入你想要的书籍编号进行下载：")) - 1
        return novel_url[index], novel_name_author[index][0]


def chapter_url_require(url):
    novel_source = get_web_page(url)
    chapter_url = re.findall(r'<dd><a href="(.*?)">', novel_source, re.S)
    n = int(input("从第几章开始下载：")) - 1
    return chapter_url[n::]


def download_chapter(url_list, book_name):
    n = 1
    print("开始时间：",time.asctime( time.localtime(time.time())))
    start = time.perf_counter()
    for url in url_list:
        time.sleep(round(0.5+random.random()))
        novel_source = get_web_page('https://www.biquyun.com' + url)
        soup = BeautifulSoup(novel_source, "html.parser")
        r = soup.find_all(id="content")
        context = r[0].text
        title = soup.find('h1')
        print('{:　<10}\t{:　>3}{}'.format(title.text, round(n / len(url_list) * 100, 2), '%'))
        n = n + 1
        with open(book_name + '.txt', 'a', encoding="utf-8") as f:
            f.write(str(title.text).lstrip() + '\n' + reindent(str(context).lstrip()) + '\n' * 2)
            f.close
    print("结束时间：",time.asctime( time.localtime(time.time())))
    time_used = (time.perf_counter() - start)
    print("总耗时：",round(time_used,2))


def main():
    name = input("请输入小说名称或关键词：")
    ulist = search_book(name)
    chapter_list = chapter_url_require(ulist[0])
    download_chapter(chapter_list, ulist[1])
    print("爬取成功！！！")


if __name__ == "__main__":
    main()
