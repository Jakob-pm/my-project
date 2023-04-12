# date = 03072023
# author = Jakob
# 学习python最好的方式，是大量的做实践练习！
import time

print('hello world!')

# 74 809*?? = 800_??+9*?? 其中？？代表的两位数，809*？？为四位数，8*？？的结果为两位数，
# 9*？？的结果为3位数。求？？代表的两位数，以及809*？？后的结果。

'''for i in range(10,100):
    a = 809*i
    b = 8*i
    c = 9*i
    if 1000 <= a <= 9999:
        if 10 <= b <= 99:
            if 100 <= c <= 999:
                print(i)
print(809*i)'''

# 75 第82例

'''a = 0o12345
print(int(str(a),10)) # 10可以省略
b = 5*1+4*8+3*8*8+2*8*8*8+1*8*8*8*8
print(b)'''

'''a = '12345'
sum = 0
for i in range(len(a)-1,-1,-1):
    # print(ord(a[i])-ord('0')) ASCII码，高精度算法
    sum += 8**(len(a)-i-1)*(ord(a[i])-ord('0'))
print(sum)'''


# 76 求0-7所能组成的奇数个数
# 组成1位数是4个；
# 组成2位数是7*4个；
# 组成3位数是7*8*4个；
# 组成4位数是7*8*8*4个。

'''j = 1
sum = 0
for i in range(1,11):
    if i ==1:
        j = 7
    elif i ==2:
        j *= 4
    else:
        j *=8
    sum += j
    print('{0}位数有{1}个'.format(i,j))
print('总共有{0}个'.format(sum))'''

# 77 连接字符串
# join函数可以处理list和string
'''delimiter = '>>'
mylist= ['Brazil','Russia','India','China']
print(delimiter.join(mylist))'''

'''mystr = 'ABCDEFG'
fenge = '--'
mystr=fenge.join(mystr)
print(mystr)'''

'''str1 = input('please input your first string:')
str2 = input('please input your second string:')
print(str1+'--'+str2)'''

# 78 输入一个奇数，然后判断至少多少个9除以该数的结果是整数。
# 例：999999/13 =76923
'''ori_num = int(input())
n1 = 1
c9 =1
m9 =9
sum =9
while n1 != 0:
    if sum%ori_num ==0:
        n1 =0
    else:
        m9*=10
        sum += m9
        c9 += 1
print('%d'%c9)'''

'''a = int(input())
b = 9
while b%a!=0:
    b = b*10+9
print(len(str(b)))'''

# 79 两个字符串连接程序

'''a = 'abcde'
b = 'fghij'
c = a+b
print(c)'''

# 80 回答结果，结构体变量传递

'''if __name__ == '__main__':
    class student:
        x = 0
        c = 0
    def f(stu):
        stu.x =20
        stu.c = 'c'
    a = student()
    a.x =3
    a.c ='a'
    f(a)
    print(a.x,a.c)'''

# 81 读取7个数(1-50)的整数值，每读取一个值，程序打印出该值个数的*。

'''if __name__ == '__main__':
    n = 1
    while n <= 7:
        a = int(input('input a number:'))
        while a < 1 or a >50:
            a = int(input('input a number:'))
        print(a*'*')
        n+=1'''

'''for i in range(7):
    num= int(input('num:'))
    while not(1<=num<=50):
        num = int(input('num:'))
    print(num*'*')'''


# 82 某个公司用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，
# 加密规则如下：每位数字都加上5，然后用和除以10的余数代替该数字，
# 再将第一位和第四位交换，第二位和第三位交换。
'''a = int(input("****"))
while not(999<a<10000):
    a = int(input("****"))
aa = []
aa.append(a%10)
aa.append((a//10)%10)
aa.append((a//100)%10)
aa.append(a//1000)
# print(aa)
# sss='-'
# print(sss.join(aa)) join函数只能处理string类型
temp = 0
for i in range(4):
    temp = (aa[i]+5)%10 # 容易把i误写成1
    aa[i] = str(temp)
ss ='' # 必须要这么写吗？
print(int(ss.join(aa)))'''
# 另一种写法：
'''num = int(input("****"))
while not(999<num<10000):
    num = int(input("****"))
a = num%10 #个位
b = (num//10)%10 #十位
c = (num//100)%10 #百位
d = num//1000 #千位
print(a,b,c,d)
res = 0
res += (a+5)%10
res *=10
res += (b+5)%10
res *=10
res += (c+5)%10
res *=10
res += (d+5)%10
print(res)'''

# 83 列表使用实例

'''a =[1,2,3,4]
print(len(a),'*')
print(a[2:],'**')
a.append(5)
print(len(a),'***')
print(a[-1],'****')
a.pop() #默认抛出最后一个元素
print(a)
a.pop()
print(a)
a.pop()
print(a)'''

'''matrix = [[1,2,3],[4,5,6],[7,8,9]]
col2 = [row[1] for row in matrix] # 可以或者列表中的某一列
print(col2)'''

# 84 时间函数举例

'''import time
print(time.time()) #浮点数时间
print(time.ctime(time.time()))
print(time.ctime())
print(time.asctime())
print(time.asctime(time.localtime()))
print(time.asctime(time.gmtime())) #格林尼治时间'''

# 85 时间函数举例2 统计程序运行时间

'''import time
start = time.time()
for i in range(10000):
    print(i)
end = time.time()
print(end-start)'''

# 86 时间函数举例3
'''import time
start = time.clock() #ttributeError: module 'time' has no attribute 'clock'
for i in range(10000):
    print(i)
end = time.clock()
print(end-start)'''
# print(time.perf_counter())
'''import time
start = time.perf_counter() #ttributeError: module 'time' has no attribute 'clock'
for i in range(10000):
    print(i)
end = time.perf_counter()
print(end-start)'''

# 87 时间函数举例4

'''import time
import random
ans = random.randint(1,100)
# print(ans)
start = time.perf_counter()
guess = int(input('please guess the number:'))
game_times = 0
while 1:
    if guess == ans:
        print('Bingo!')
        game_times += 1
        break
    elif guess < ans:
        print('guess bigger please!')
        guess = int(input('please guess the number:'))
        game_times +=1
    else:
        print('guess less please!')
        guess = int(input('please guess the number:'))
        game_times += 1
end = time.perf_counter()
diff = int(end - start)
print('%d s' % diff)
print('%d 次' % game_times)
if diff <= 5:
    print('you are very clever!!!')
else:
    print('come on, you can do it better!')'''


# 88 字符串日期转换为易读的日期格式

'''print(time.ctime())
# Thu Mar  9 18:27:05 2023
from dateutil import parser
dt = parser.parse('Thu Mar  9 18:27:05 2023')
print(dt)

print(parser.parse(time.ctime())) #可以直接打印当前时间'''

# 89 计算字符串子串出现的次数

'''str1 = input('please input the string:')
str2 = input('please input the sub_string:')

print(str1.count(str2))

lst1 = [1,2,3,3,3,4,4]
print(lst1.count(3))
print(lst1.count(4))

tuple1 = (1,2,3,3,3,4,4)
print(tuple1.count(3))'''

# 90 从键盘输入一些字符

'''file_name = input('请输入文件名：')
fp = open(file_name,'w')
s = input('请输入字符串：')
while s!= '#':
    fp.write(s+'\n')
    s = input('请输入字符串：')
print('End')'''


# 91 从键盘输入一些字符
'''file_name = input('请输入文件名：')
a = input('请输入字符串：')
a = a.upper() # 注意有些函数能改变原对象，有些需要接收一下，需要总结
# print(a)
fp = open(file_name,'w')
fp.write(a)
print('End')
fp = open(file_name,'r')
print(fp.read())'''
# 92 有2个磁盘文件A和B，各存放一行字母，要求把这2个文件中的信息合并，
# (按字母顺序排列)，输出到一个新文件C中。

'''fp1 = open('test_file','r')
a = fp1.read()
print(a)
fp1.close()

fp2 = open('test_file_0','r')
b = fp2.read()
print(b)
fp2.close()

c = list(a+b)
# print(c)

for i in c:
    if i == ' ':
        c.remove(i)
# print(c)
fp3 = open('test_file_1','w')
c.sort()
# print(c)
#for i in c:
    #fp3.write(i)
# fp3.close()
# 另一种选择，用join函数
s = ' '
c= s.join(c)
fp3.write(c)
print('End')'''



# 93 列表转换为字典

keys = ['a','b']
values = [1,2]

print(dict(zip(keys,values)))
# print(dict([keys,values])) 这样不行





print('Goodbye')