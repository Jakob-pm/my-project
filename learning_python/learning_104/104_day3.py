# date = 04/07/2023
# author = Jakob
print('hello world!')

import requests
from bs4 import BeautifulSoup

# url = 'http://www.xinfadi.com.cn/index.html'
url ='http://www.xinfadi.com.cn/priceDetail.html'

resp = requests.get(url)
# print(resp.text)

page = BeautifulSoup(resp.text, 'html.parser')
# <div class="tablebox">

# table = page.find('div', class_= 'tablebox')
table = page.find('div', attrs={'class':'tablebox'})
print(table)




print('done!')







# if __name__ == '__main__':
    # main()




print('Goodbye!')