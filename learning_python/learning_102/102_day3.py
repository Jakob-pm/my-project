# date = 03062023
# author = Jakob
# 学习python最好的方式，是大量的做实践练习！
print('hello world!')

# 028 验证一个字符串是否是日期

# import re

'''def date_ist_right(date):
    return re.match('\d{4}-\d{2}-\d{2}',date) is not None



date1 = '2023-03-06'
date2 = '202-03-06'
date3 = '2023/03-06'
date4 = '20230306'

print(date1,date_ist_right(date1))
print(date2,date_ist_right(date2))
print(date3,date_ist_right(date3))
print(date4,date_ist_right(date4))
# print(date1,date_ist_right(date1))'''

# 029 提起手机号码

content = '''白日依19989881888山尽，黄河入45645546468798978海流。
欲穷12345千里目，更上15619292345一层楼。'''

'''import re

pattern = r'1[3-9]\d{9}'

results = re.findall(pattern, content)
# print(results)

for res in results:
    print(res)'''

# 030 批量提起网页上的手机号码

'''import re

pattern = r'1[3-9]\d{9}'

file_content = ''

with open ('phone_number.txt') as fin:
    file_content = fin.read()

datas = re.findall(pattern, file_content)

print(len(datas))
with open('./phone_number_output.txt','w') as fout:
    for data in datas:
        # print(data)
        fout.write(data + '\n')'''

# 031 自动提起邮箱地址

content1 = '''
寻隐者12345@qq.com不遇
朝代：asdf12dsa#abc.com唐
作python66@163.com者：贾岛
松下问童子，言师采python-abc@163com药去。
只在python_ant-66@sina.net此山中，云深不知处。
'''

'''import re

pattern = re.compile(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,4}')
# 需要查找和总结一些查找日期、手机号和邮箱的re写法

datas = re.findall(pattern, content1)

for data in datas:
    print(data)'''

# 032 验证密码是否符合格式

# 要求：
# 1. 长度必须在6-20位之间
# 2. 必须包含小写字母
# 3. 必须包含大写字母
# 4. 必须包含数字
# 5. 必须包含特殊字符

'''import re

def check_pass_valid(password):
    if not 6 <= len(password) <= 20:
        return False, '密码长度必须在6~20之间'
    if not re.findall(r'[a-z]',password):
        return False, '必须包含小写字母'
    if not re.findall(r'[A-Z]',password):
        return False, '必须包含大写字母'
    if not re.findall(r'[0-9]',password):
        return False, '必须包含数字'
    if not re.findall(r'[^0-9a-zA-Z]',password):
        return False, '必须包含特殊字符'
    return True

password = input('请设置您的登陆密码：')
print(check_pass_valid(password))'''

# 033 提取商品价格

content2 = '''
小明上街买菜
买了1斤黄瓜花了8元；
买了2斤葡萄花了13.5元；
买了3斤白菜花了5.4元；'''

# 要求提取（1 黄瓜 8） （2 葡萄 13.5） （3 白菜 5.4）

'''import re

for line in content2.split('\n'):
    pattern = r'(\d)斤(.*)花了(\d+\.{0,1}\d*)元'
    res = re.findall(pattern,line)
    if res:   #如果直接print结果，会出现空的list[],这里用一个if判断，排除了空的list
        print(res)
    # print(re.findall(pattern,line) if re.findall(pattern,line)  else 'end=')
    # 这里不能使用表达式，以后需要研究一下，为什么print后面的表达式，if一定要有else

    # print(line)'''


# 034 给文章中的手机号打马赛克

'''import re

pattern = r'(1[3-9])\d{9}'

content3 = re.sub(pattern, r'\1*-****-****',content)

print(content3)
print(content)'''

# 035 多种日期格式的标准化

content4 ='''
白日依2021/05/26山尽，黄河入2021.05.27海流。
欲穷05-28-2020千里目，更上5/29/2020一层楼。
'''

'''import re

content4_1 = re.sub(r'(\d{4})/(\d{2})/(\d{2})',r'\1-\2-\3',content4)

content4_2 = re.sub(r'(\d{4})\.(\d{2})\.(\d{2})',r'\1-\2-\3',content4) #这里的点前面需要加上\进行转义，否则点识别的是任意字符

content4_3 = re.sub(r'(\d{2})-(\d{2})-(\d{4})',r'\3-\2-\1',content4)

content4_4 = re.sub(r'(\d{1,2})/(\d{2})/(\d{4})',r'\3-\1-\2',content4)

print(content4_4)
print(content4)'''

# 036 统计英文单词出现频率

'''import re

with open('count_word_nums.txt') as fin:
    content5 = fin.read()

# print(content5.split())
# datas = re.split(r'[\s.()-?:\d]+',content5)
datas = re.split(r'[^a-zA-Z]+',content5)
# print(datas)

import pandas as pd

print(pd.Series(datas).value_counts()[:10])'''


# 037 中文文章分词

content5 = '''
新进展是，3月5日这一周，美国财政部削减了3个月期限的国库券招标规模，计划几天后发行570亿美元的3个月国库券，比上一次发行同期限债券的规模减少了30亿美元，此后还有可能进一步削减。
这表明，美国债务上限看不到任何突破迹象，美国财政部采取发行短期债券来还旧债的应急之策正在进入被动期，美国发债的底气已经明显不足。
与此同时，3月5日当周有着全球资产定价之锚之称的10年期美债收益率一度突破4%关口,重新回到去年四季度触及的十余年高位。
美债收益率与价格和持有情况成反比，收益率越高，说明全球买家抛售美债的幅度越大。
'''

'''import re
import jieba
import pandas as pd

content6 = re.sub(r'[\s\\n，,%。+\d]','',content5)
# print(content6)
word_list = jieba.cut(content6)
cut_list = ['了','个','后','的','这','与','月','日','与此同时','来','还','任何']
# 需要一个中文多余符号和无意义词的词典
final_list =[]

for word in word_list:
    if word not in cut_list:
        final_list.append(word)

# print(list(final_list))

print(pd.Series(final_list).value_counts()[:10])'''

# 038 提取一篇文章中所有人名

# /Users/jakob_pc/Desktop/鹿鼎记.txt

content7 = '李雷喜欢韩梅梅，他俩早恋了'

with open('/Users/jakob_pc/Desktop/鹿鼎记.txt') as fin:
    content8 = fin.read()
# print(content8)
import jieba.posseg as posseg
import pandas as pd

names = []
for word, flag in posseg.cut(content8):
    if flag =='nr':
        names.append(word)
        #print(word, flag)

print(pd.Series(names).value_counts()[:5])








print('Goodbye')