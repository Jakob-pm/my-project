
from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import xlwt
import sqlite3
import ssl
from ssl import _create_unverified_context


findLink= re.compile(r'<a href="(.*?)">')
findImgSrc= re.compile(r'src="(.*)" width="\d*"') #可以加上re.S考虑换行的情况
# <img alt="肖申克的救赎" class="" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" width="100"/></a>
findTitle = re.compile(r'<span class="title">(.*)</span>')
# <span class="title">肖申克的救赎</span>
findRating = re.compile(r'<span class=".*" \w*=".*">(.*)</span>')
# <span class="rating_num" property="v:average">9.7</span>
findAudien = re.compile(r'<span>(\d+)人评价</span>')
# <span>2813036人评价</span>
findInq = re.compile(r'<span class="inq">(.*)</span>')
# <span class="inq">希望让人自由。</span>
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)



def getData(baseurl):
    datalist = []
    for i in range(8,10):
        url = baseurl + str(i*25)
        print(url)
        html = askURL(url)

        # print(html)

        print('*')
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div', class_='item'):
            # print(item)
            data = []
            item = str(item)
            print('*')
            # print(item)


            link = re.findall(findLink, item)[0]
            data.append(link)
            ImgSrc = re.findall(findImgSrc, item)[0]
            data.append(ImgSrc)
            Title = re.findall(findTitle, item)[0]
            data.append(Title)
            Rating = re.findall(findRating, item)[0]
            data.append(Rating)
            Audien = re.findall(findAudien, item)[0]
            data.append(Audien)
            Inq = re.findall(findInq, item)
            if Inq:
                data.append(Inq[0])
            else:
                data.append('...')
            Bd = re.findall(findBd, item)[0]
            Bd = re.findall(r' *(.*\S)\n',Bd)
            s = ' '
            Bd = s.join(Bd)
            data.append(Bd)
            datalist.append(data)
            print(datalist)



def askURL(url):
    ssl._create_default_https_context = ssl._create_unverified_context
    head = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url,headers = head)
    html = ''
    code = ''
    reason = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e,code)
        if hasattr(e,'reason'):
            print(e,reason)
    return html



baseurl = 'https://movie.douban.com/top250?start='
datalist = getData(baseurl)