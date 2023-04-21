# 01 替换字符串中的不良内容
# import re
#
#
# def main():
#     sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
#     purified = re.sub('[操肏艹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
#                       '*', sentence, flags=re.IGNORECASE)
#     print(purified)  # 你丫是*吗? 我*你大爷的. * you.
#
#
# if __name__ == '__main__':
#     main()
#
# 02 提取出国内手机号码
# import re
#
#
# def main():
#     # 创建正则表达式对象 使用了前瞻和回顾来保证手机号前后不应该出现数字
#     pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
#     sentence = '''
#     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
#     不是15600998765，也是110或119，王大锤的手机号才是15600998765。
#     '''
#     # 查找所有匹配并保存到一个列表中
#     mylist = re.findall(pattern, sentence)
#     print(mylist)
#     print('--------华丽的分隔线--------')
#     # 通过迭代器取出匹配对象并获得匹配的内容
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     print('--------华丽的分隔线--------')
#     # 通过search函数指定搜索位置找出所有匹配
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())
#
#
# if __name__ == '__main__':
#     main()

# 03 爬取笔趣阁电子书
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os

"""
从www.biqubao.com笔趣阁爬取小说，楼主教程中的网址我当时没打开，
就参照楼主教程，爬取了笔趣阁小说网的内容。
    2018-07-31
"""

if __name__=='__main__':
    #所要爬取的小说主页，每次使用时，修改该网址即可，同时保证本地保存根路径存在即可
    target="http://www.soduzw.com/mulu_191340.html"
    # 本地保存爬取的文本根路径
    save_path = '/Users/jakob_pc/Desktop'
    #笔趣阁网站根路径
    index_path='http://www.soduzw.com/'

    req=requests.get(url=target)
    #查看request默认的编码，发现与网站response不符，改为网站使用的gdk
    print(req.encoding)
    req.encoding = 'gbk'
    #解析html
    soup=BeautifulSoup(req.text,"html.parser")
    list_tag=soup.div(id="list")
    print('list_tag:',list_tag)
    #获取小说名称
    story_title=list_tag[0].dl.dt.string
    # 根据小说名称创建一个文件夹,如果不存在就新建
    dir_path=save_path+'/'+story_title
    if not os.path.exists(dir_path):
        os.path.join(save_path,story_title)
        os.mkdir(dir_path)
    #开始循环每一个章节，获取章节名称，与章节对应的网址
    for dd_tag in list_tag[0].dl.find_all('dd'):
        #章节名称
        chapter_name=dd_tag.string
        #章节网址
        chapter_url=index_path+dd_tag.a.get('href')
        #访问该章节详情网址，爬取该章节正文
        chapter_req = requests.get(url=chapter_url)
        chapter_req.encoding = 'gbk'
        chapter_soup = BeautifulSoup(chapter_req.text, "html.parser")
        #解析出来正文所在的标签
        content_tag = chapter_soup.div.find(id="content")
        #获取正文文本，并将空格替换为换行符
        content_text = str(content_tag.text.replace('\xa0','\n'))
        #将当前章节，写入以章节名字命名的txt文件
        with open(dir_path+'/'+chapter_name+'.txt', 'w') as f:
            f.write('本文网址:'+chapter_url)
            f.write(content_text)
