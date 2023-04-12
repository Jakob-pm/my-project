# jakob
# decode = utf-8
print('hello world!')

# 正则
# 数据解析的基本工具

import re

# re 正则 001 Python函数写法
'''content = """苹果，是绿色的
橙子，是橙色的
香蕉，是黄色的
乌鸦，是黑色的
猴子，
"""


p = re.compile(r'，.+') # r防止转义

for i in p.findall(content):
    print(i)
# print(p)
# print(content)
# print(type(content))'''

# re 正则 002 元字符
# . 表示任意一个字符，除了\n
# \d 表示0-9之间任意一数字
# \D 表示非数字
# \s表示空白字符
# \S 表示非空白字符
# \w 表示大小写字母、数字、下划线
# \W 表示除大小写字母、数字、下划线之外的其他

# re 正则 003 字符集
# [], [abcd],[a-d],[0-9]
# 取反，^
# 多字符匹配
'''print(re.match('[0-9][0-9]','55'))
print(re.match('[0-9][A-Z]','5F'))

print(re.match('\w\w','55'))
print(re.match('[\w\W][\w\W][\w\W][\w\W][\w\W]','我rG2#'))'''

# re 正则 004 转义符
'''str = 'c:\\python\ne\test.py'
str1 = 'c:\\\python\\ne\\test.py'
str2 = r'c:\\python\ne\test.py'

print(str1)
print(str2)'''

'''print(re.match('\d','\d'))  #  前面的\d代表数字，不能匹配/d,后面的\d在Python中等于\\d
print(re.match('\\d','\d')) # \d \\d
print(re.match('\\\d','\d')) # \\d \\d
print(re.match('\\\\d','\d')) # \\d \\d

# 优先使用python，再使用正则表达式处理字符
print(re.match('\n','\n'))
print(re.match('\\n','\n'))
print(re.match('\\\n','\n'))'''

# re 正则 005 数量规则

'''print(re.match('\d*','15201368901')) #贪婪模式
print(re.match('\d+','15201368901'))''' # *是0到多次，+是至少一次

'''print(re.match('\d','1520136a8901'))
print(re.match('\d？','1520136a8901'),'*')
print(re.match('\d？','a'),'**')
print(re.match('\d？',''),'***')
print(re.match('\d？','1'),'****')'''

# 不理解
'''print(re.match('\d{5}','15201368901'))
print(re.match('\d{5,}','15201368901'))
print(re.match('\d{5,}','152a01368901'))
print(re.match('\d{1,3}','152a01368901'))
print(re.match('\d{1,4}','152a01368901'))'''

# 边界

'''tel='13955007891aa123'
# print(re.match('\d*',tel))
# [1] [358] [56789] {8}
print(re.match('^1[358][5-9]\d{8}$',tel))'''

# 单词边界
'''str1 = 'i put a lighted match to the letter and watched it burn.'
print(re.findall(r'ed\b',str1)) # \b  边界
print(re.findall(r'\Bed',str1)) # \B  非边界'''

# re 正则 006 分组匹配

'''t = '2021-09-14'
print(re.match('2021-09-14',t))
print(re.match('\d{4}-\d{2}-\d{2}',t))
print(re.match('\d{4}-(0[1-9]|1[0-2])-\d{2}',t))
print(re.match('\d{4}-(0[1-9]|1[0-2])-\d{2}',t).group())
print(re.match('\d{4}-(0[1-9]|1[0-2])-\d{2}',t).group(0))
print(re.match('\d{4}-(0[1-9]|1[0-2])-\d{2}',t).group(1))'''

# con = '''<title>this is python3</title>'''

'''print(re.match(r'<title>([\w\W]*)</title>',con).group(1))

print(re.match(r'<(\w+)>([\w\W]*)</\1>',con).group(1))


# 给分组起别名（？P<name>），引用分组别名（？P=name）
print(re.match(r'<(?P<tag>\w+)>([\w\W]*)</(?P=tag)>',con).group(1))'''






print('Goodbye!')