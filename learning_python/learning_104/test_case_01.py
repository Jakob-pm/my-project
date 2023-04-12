# 测试函数askURL
# 'https://movie.douban.com/top250?start=0&filter='

import urllib.request
import urllib.error
import ssl
from ssl import _create_unverified_context

def askURL(url):
    global html
    global code
    global reason
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
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e,code)
        if hasattr(e,'reason'):
            print(e,reason)
    # return html

askURL('https://movie.douban.com/top250?start=0&filter=')

# 成功！！！