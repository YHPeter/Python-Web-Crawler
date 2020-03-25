import requests
import re
import time
import random


def download(book_name):
    # 下载小说
    search_real_url = 'https://www.biquge5200.com/modules/article/search.php?searchkey=' + book_name
    
    try:
        novel_source = requests.get(search_real_url).text
        reg1 = r'<td class="odd"><a href="(.*?)">(.*?)</a></td>.*?<td class="odd">(.*?)</td>'
        # 所有搜索到的结果（包括小说网址、名称、作者姓名）
        novel_list = re.findall(reg1, novel_source, re.S)
        # 判断是否有结果返回
        if len(novel_list) == 0:
            print('你要找的小说不存在，请检查后重新输入')
    except Exception as e:
        print(e)
    for novel_url, novel_name, novel_author in novel_list:
        if novel_name == book_name:
            print('你即将下载的小说：%s 作者：%s' % (novel_name, novel_author))
            return novel_url, novel_name


def get_chapter(url):
    # 获取章节页面
    try:
        # 章节页面源代码
        chapter_page_source = requests.get(url).text
        reg2 = r'<dd><a href="(.*?)">(.*?)</a></dd>'
        chapter_list = re.findall(reg2, chapter_page_source)
    except Exception as e:
        print(e)
    return chapter_list


def get_content(chapter_list, novel_name):
    count = 0
    length = len(chapter_list)
    for chapter_url, chapter_name in chapter_list:
        try:
            time.sleep(1+random.random())
            content_source = requests.get(chapter_url).text
            reg = r'<div id="content">(.*?)</div>'
            content = re.findall(reg, content_source, re.S)[0]
            content = content.replace('<br/>', '').replace(' ', '').replace('<p>', '').replace('</p>', '\n')
            count += 1
            with open(novel_name + '.txt', 'a', encoding='utf-8') as f:
                f.write(chapter_name + '\n' * 2 + content + '\n' * 2)
                print('正在写入: ' + chapter_name)
                print('进度：%0.2f' % (count / length*100)+'%')
        except Exception as e:
            print(e)


if __name__ == '__main__':
    book_name = input('请输入你要下载的小说名字(确保输入的小说名字正确)：')#search novel book by novel name without fuzzy query
    novel_url, novel_name = download(book_name)
    chapter_list = get_chapter(novel_url)
    get_content(chapter_list, novel_name)
