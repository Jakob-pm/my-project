# date = 03072023
# author = Jakob
# 学习python最好的方式，是大量的做实践练习！
print('hello world!')

# 56 计算字符长度

'''str = input('please input your string:')

print('the length of your string is %d' % len(str))'''

# 57 打出杨辉三角

'''a = []
n = int(input('n:'))
for i in range(n):
    a.append([])  #python二维列表的属性
    for j in range(i+1):
        if j == 0 or j == i:
            a[i].append(1)
        else:
            a[i].append(a[i-1][j]+a[i-1][j-1])
for i in a:
    print(i)'''

#列表里面还可以加列表：列表里面的元素是否有顺序？
'''a = []
a.append([1,2])
a.append([2,3])
print(a)

for i in a:
    print(i)'''

# 58 查找字符串

'''sStr1 = 'abcdefg'
sStr2 = 'cde'

print(sStr1.find(sStr2))'''
# kmp字符串匹配算法？

# 59 输入3个数字，按大小顺序排列

'''if __name__ == '__main__':
    a = int(input('请输入第一个数字：'))
    b = int(input('请输入第二个数字：'))
    c = int(input('请输入第三个数字：'))

    def swap(p1,p2):
        return p2,p1

    if a >b: a,b = swap(a,b)
    if a > c: a, c = swap(a, c)
    if b > c: b, c = swap(b, c)

    print(a,b,c)'''

# 第二种方法：
'''a = int(input('请输入第一个数字：'))
b = int(input('请输入第二个数字：'))
c = int(input('请输入第三个数字：'))
lst = []
lst.append(a)
lst.append(b)
lst.append(c)
lst.sort()
print(lst)'''

# 第三种方法：
'''a = int(input('请输入第一个数字：'))
b = int(input('请输入第二个数字：'))
c = int(input('请输入第三个数字：'))

if a >b:
    if b>c:
        print(c,b,a)
    else: # a>b b<c
        if a> c:
            print(b,c,a)
        else:
            print(b, a, c)
else: # a < b
    if b< c:
        print(a,b,c)
    else: # a < b b > c
        if a> c:
            print(c,a,b)
        else:
            print(a, c, b)'''
# 换一种写法：
'''num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))
num3 = int(input('请输入第三个数字：'))

if num1 >= num2 >= num3: print(num1,num2,num3)
elif num1 >= num3 >= num2: print(num1,num3,num2)
elif num2 >= num1 >= num3: print(num2,num1,num3)
elif num2 >= num3 >= num1: print(num2,num3,num1)
elif num3 >= num1>= num2: print(num3,num1,num2)
else: print(num3,num2,num1)'''

# 60 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。

'''a = []
n = int(input('n:'))
for i in range(n):
    a.append(int(input('请输入第 %d 个数字:' %(i+1))))
max = -999999999999
max_index = 0
min = 99999999999
min_index = 0
for i in range(n):
    if a[i] < min:
        min = a[i]
        min_index = i
    if a[i] > max:
        max = a[i]
        max_index = i

print(a)
# 先处理特殊情况：
if max_index == 0:
    if min_index == n-1:
        pass # 什么都不做用pass
    else:
        a[-1], a[min_index] = a[min_index], a[-1]
elif max_index == n-1:
    if min_index == 0:
        a[0], a[-1] = a[-1], a[0]
    else:
        a[0], a[-1] = a[-1], a[0]
        a[-1], a[min_index] = a[min_index], a[-1]
elif min_index == n-1:
    a[0], a[max_index] = a[max_index], a[0]
elif min_index == 0:
    a[0], a[-1] = a[-1], a[0]
    a[0], a[max_index] = a[max_index], a[0]
else:
    a[0], a[max_index] = a[max_index], a[0]
    a[-1], a[min_index] = a[min_index], a[-1]

# 最大值与第一个元素交换
# a[0], a[max_index] =a[max_index],a[0]
# 最小值与最后一个元素交换
# a[-1], a[min_index] =a[min_index],a[-1]
# 输出结果
print(a)'''
# 第二种思路，解耦两件事情，最大值和最小值替换分别进行：
'''a = []
n = int(input('n:'))
for i in range(n):
    a.append(int(input('请输入第 %d 个数字:' %(i+1))))
max = -999999999999
max_index = 0
min = 99999999999
min_index = 0

for i in range(n):
    if a[i] < min:
        min = a[i]
        min_index = i
a[-1], a[min_index] =a[min_index],a[-1]
for i in range(n):
    if a[i] > max:
        max = a[i]
        max_index = i
a[0], a[max_index] =a[max_index],a[0]

print(a)'''

# 61 n个整数，使其前面个数顺序向后移动m个位置，最后m个数变成最前面的

'''a = [2,8,6,1,28,45,34,2]
b = [0,0,0,0,0,0,0,0]
# print(len(a))
#print(len(b))
m = int(input('m:'))
if m in range(2,len(a)-1):
    pass
else:
    print('invalid')
t = 0
for i in range((len(a)-m),len(b)):
    b[i] = a[t]
    t += 1
    print('*')
# for循环的次数需要再仔细理解一下
print((len(a)-m))
print(t)
for i in range(0,(len(a)-m)):
    b[i] = a[m+i] # 这里也可以写为 b[i] = a[t] t += 1
print(a)
print(b)'''

# 62 n个人围成一圈，顺序排号，从第一个人开始报数，凡是报到3的人退出圈子，问最后留下来的是第几号那位
# 约瑟夫环

'''if __name__ == '__main__':
    n = int(input('请输入参加游戏的人数：'))
    num= []
    for i in range(n):
        num.append(i+1)

    i = 0 # 当前位置
    k = 0 # 报数
    m = 0 # 删掉的个数

    while m<n-1: # 为什么是到n-2? while循环到什么时候退出？
        if num[i] != 0:
            k += 1
        if k == 3:
            num[i] = 0
            print(num)
            k = 0
            m += 1 # 最后一轮循环，这里m又加一，加到了n-1
        i += 1
        if i == n: # 首尾相连
            i = 0
            # print('*')
    print(m)
    print(i) # 这是最后一个被删除的数字下标，倒数第二个幸存者
    i = 0
    while num[i] ==0:
        i += 1
    print(num[i])'''


# 63 求一个字符串的长度

'''def my_len(s):
    i = 0
    for each in s:
        i += 1
    return i

s = input('plese input the string here:')
print(my_len(s))
# 可以直接使用内置函数 len()
print('the length of your string is %d' % len(s))'''

# 64 编写input和output函数输入，输出5个学生的数据记录。

# 第一种写法
'''N = 3
# stu
# num : string
# name : string
# score []: list
student = []
for i in range(5):
    student.append(['','',[]])

def input_stu(stu):
    for i in range(N):
        stu[i][0]=input('input student num:\n')
        stu[i][1] = input('input student name:\n')
        for j in range(3):
            stu[i][2].append(int(input('score:\n')))

def output_stu(stu):
    for i in range(N):
        print('%-6s%-10s' % (stu[i][0],stu[i][1]))
        for j in range(3):
            print('%8d' % stu[i][2][j])

if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)'''

# 第二种写法

'''n = int(input('n:'))
student = []

def input_stu(stu):
    for i in range(n):
        student.append([])
        print('-----第%d位学生的信息开始录入-----' % (i+1))
        name = input('请输入学生姓名：')
        serial = int(input('请输入学号：'))
        chinese = int(input('请输入%s的语文成绩：' % name))
        math = int(input('请输入%s的数学成绩：' % name))
        english = int(input('请输入%s的英语成绩：' % name))
        student[i].append(name)
        student[i].append(serial)
        student[i].append(chinese)
        student[i].append(math)
        student[i].append(english)

def output_stu(stu):
    print('-----学生信息如下-----')
    for i in range(n):
        print('学号%d：'%stu[i][1], end='')
        print(stu[i][0])
        print('语文 %d'%stu[i][2])
        print('数学 %d' % stu[i][3])
        print('英语 %d' % stu[i][4])
        print('***************************')

if __name__ == '__main__':
    input_stu(student)
    print(student)
    output_stu(student)'''

# 65 创建一个链表

'''if __name__ == '__main__':
    ptr = []
    n = int(input('请确定链表的长度：'))
    for i in range(n):
        num = int(input('请输入第%d个数字：'%(i+1)))
        ptr.append(num)
    print(ptr)'''

# 另一种写法：
'''ptr = [int(input('请输入数字：')) for x in range(5)]
print(ptr)'''


# 66 反向输入一个链表

'''ptr = [int(input('请输入数字：')) for x in range(5)]
print(ptr)

# 第一种方法：
# ptr.reverse()
# print(ptr)

# 第二种方法：
# for i in range(5,0,-1):
    # print(ptr[i-1], end=' ')

# 第三种方法：
for i in range(5):
    print(ptr[-(i+1)], end=' ')
print()'''

# 67 列表排序与连接

# sorted函数是生成新的列表
'''a = [3,4,5,1,2]
b = sorted(a)
c = sorted(a,reverse=True)
print(b)
print(c)'''

# sort方法是将原来的列表进行排序
'''a = [3,4,5,1,2]
a.sort(reverse=True)
print(a)'''

# 68 简单题目

'''if __name__ == '__main__':
    for i in range(5):
        n = 0
        if i != 1:n +=1
        if i == 3:n +=1
        if i == 4: n += 1
        if i != 4: n += 1
        print(n)
        # if n == 3: print(64+i)'''

# 69 输入n为偶数，调用函数求1/2+1/4+...+1/n

'''def even_add(n):
    t = int(n/2)
    # print(t, end = '*')
    # print()
    if t == 1:
        return 0.5
    else:
        return (even_add(n-2)+1/n)
        print('##')

# print(even_add(2))
# print(even_add(4),end = '**')
# print(even_add(10),end = '***')
# print()
# print(1/2+1/4+1/6+1/8+1/10)

# a = 8
# print(int(a/2))
def odd_add(n):
    t = int((n+1)/2)
    # print(t, end = '*')
    # print()
    if t == 1:
        return 1
    else:
        return (odd_add(n-2)+1/n)
        print('##')


n = int(input('请输入一个数字：'))
if n%2:
    print(odd_add(n))
else:
    print(even_add(n))'''

# 优化写法
'''def a(n):
    if n%2:
        print(c(n))
    else:
        print(b(n))

def b(n):
    sum = 0
    for i in range(2,n+1,2):
        sum += 1/i
    return sum
def c(n):
    sum = 0
    for i in range(1, n + 1, 2):
        sum += 1 / i
    return sum

if __name__ == '__main__':
    n = int(input('请输入一个数字：'))
    a(n)'''


# 70 循环输入列表

'''a = [s for s in 'Fuck you!']
for i in range(len(a)):
    print(a[i],end='')
print()'''

# 71 找到年龄最大的人

'''person = {'li':18,'wang':50,'zhang':20,'sun':22}
m = 'li'
for i in person.keys():
    if person[m] < person[i]:
        m = i
print('%s %d' %(m, person[m]))'''

# 72 字符串排序

'''str1 = input('string1:')
str2 = input('string2:')
str3 = input('string3:')

print(str1,str2,str3)
if str1 > str2: str1,str2 =str2,str1
if str1 > str3: str1,str3 =str3,str1
if str2 > str3: str2,str3 =str3,str2
print(str1,str2,str3)'''


# 73 猴子分桃

'''i=0
while i >= 0:
    if i%5 ==1:
        if (i-1)%4 ==1:
            if (i - 2) % 3 == 1:
                if (i - 3) % 2 == 1:
                    print(i)
                    break
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1
    else:
       i += 1'''

# 答案写法：
i =1
while 1:
    # 0-4
    temp = i
    for j in range(5):  # 0-4
        if temp%5 != 1:
            break
        else:
            temp = (temp-1)/5*4
            if j == 4:
                print(i)
                exit()
    i += 1



# 74 809_?? = 800_??
# 75 第82例
# 76 求0-7所能组成的奇数个数




print('Goodbye')