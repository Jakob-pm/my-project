# date = 03052023
# author = Jakob
# 学习python最好的方式，是大量的做实践练习！
print('hello world!')

with open('/Users/jakob_pc/Desktop/鹿鼎记001.txt') as fin:
    content8 = fin.read()
print(content8)


## 在终端输入'file --mime-encoding <filename>' 可以查到文档的编码格式
# encoding='ISO-8859-1'
# https://stackoverflow.com/questions/19699367/for-line-in-results-in-unicodedecodeerror-utf-8-codec-cant-decode-byte


print('Goodbye')