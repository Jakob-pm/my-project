# date = 04/06/2023
# author = Jakob
print('hello world!')

import requests
import re
import xlwt

domain = 'https://www.dytt8.net/index2.htm'
resp = requests.get(domain, verify=False)
resp.encoding = 'gb2312' # 源网页里charset = gb2312
# print(resp.text)

obj1 = re.compile(r'2023新片精品.*?<ul>(?P<ul>.*?)</ul>',re.S)
obj2 = re.compile(r"</a>]<a href='(?P<href>.*?)'",re.S)
# <a href="/html/gndy/dyzz/index.html">最新电影下载</a>]<a href='/html/gndy/dyzz/20230403/63576.html'>
obj3 = re.compile(
    r'><br /><br />◎译　　名(?P<movie>.*?)<br />.*?<br />'
    r'<a target="_blank" href="(?P<download>.*?)"><strong>',
    re.S
)
# ><br /><br />◎译　　名　脐带  / 漫游在蓝色草原 / The Cord of Life<br />
# <br /><a target="_blank" href="迅雷磁力链接🔗"><strong>

result1 = obj1.finditer(resp.text)
child_href_list = []
for i in result1:
    ul = i.group('ul')
    # print(ul)

    result2 = obj2.finditer(ul)
    for k in result2:
        child_href = domain.replace('/index2.htm','') +k.group('href')
        # print(child_href)
        child_href_list.append(child_href)

# 提取子页面内容
all_data = []
for href in child_href_list:
    # print(href)
    data = []
    resp2 = requests.get(href, verify = False)
    resp2.encoding ='gb2312'
    # print(resp2.text)
    result3 = obj3.search(resp2.text)
    #print(result3.group('movie'))
    #print(result3.group('download'))
    data.append(result3.group('movie'))
    data.append(result3.group('download'))
    all_data.append(data)

print(all_data)

book = xlwt.Workbook()
sheet = book.add_sheet('2023新片精品')
col = ('片名','下载链接')
for i in range(2):
    sheet.write(0,i,col[i])
for i,k in enumerate(all_data):
    print('第%d条' %(i+1))
    print(k)
    for j in range(2):
        sheet.write(i+1,j,k[j])


book.save('/Users/jakob_pc/Desktop/test_xl_file_07.xls')



print('done!')







# if __name__ == '__main__':
    # main()




print('Goodbye!')