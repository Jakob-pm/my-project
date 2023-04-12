# date = 03032023
# author = Jakob
# 学习python最好的方式，是大量的做实践练习！
print('hello world!')

# 001 两数之和
'''num1 = 15
num2 = 23
sum = num1 + num2

print(f'{num1}+{num2}={sum}')'''

# 002 数字的阶乘
# 知识点：递归函数
'''def fac(i):
    if i == 1:
        return  1
    else:
        res = i*fac(i-1)
        return res

if __name__ == '__main__':
    i = int(input('请输入一个数字：'))
    print(fac(i))'''
# 错误写法：
'''if i == 1:
    jiecheng(i) =1
else:
    jiecheng(n) = i*jiecheng(i-1)'''
# 注意所谓的等式其实用return来表达了，以后注意=赋值，==逻辑结算，和return的使用区别

# 笨的方法，使用while循环做一下

'''def get_fac(num):
    result =1
    while num >0:
        result *=num
        num -= 1
    return result
print('fac 3 =',get_fac(3))'''
# print('fac 6 =',get_fac(6))
# print('fac 100 =',get_fac(100))
# 理解不一定正确：但是用for循环是从n往下递减，直到满足n-1=1的情况，最后再乘上1；
# 但是while循环是先乘上了1，最后一步是乘上n-1=2
# for循环直接从n降到了1为止，while是先把1找到，再从n降到2；
# https://www.bilibili.com/video/BV1wD4y1o7AS?p=95&vd_source=30bab237673b3b5ce295ed306c7fe29c
# P95 递归


# 补充斐波那契数列问题写法：
'''def fib(i):
    if i == 1:
        return 1
    elif i == 2:
        return 1
    # elif i == 0:
        # print('请输入正整数')
    else:
        return fib(i-1)+fib(i-2)
# 错误写法：return fib(n-1)+fib(n-2)
# 注意自己定义的参数，本来是i，写成了n

for i in range(1,7):
    print(fib(i))'''
# 注意range函数的范围是前开后闭，最后一个参数是步长


# 003 计算圆的面积

'''import math

def area_of_circle(r):
    return round(math.pi*r*r,2)
print(area_of_circle(3))'''

# 004 区间内所有素数

# 第一步：找到因数的方法
'''i = int(input('请输入一个正整数：'))
for j in range(2,i):
    if not(i%j) :
        print(j,end=' ')
        print('*')'''

'''i = int(input('请输入一个正整数：'))
for j in range(2,i):
    if not(i%j) :
        print(j,end=' ')
        print('*')
        # print('合数')
    else:
        print('$')'''
# 找到第一步和第二步逻辑的衔接点：找到真因数的个数，记为sum
# 如果sum的值为0，则该数为质数
'''i = int(input('请输入一个正整数：'))
sum = 0
for j in range(2,i):
    if not(i%j) :
        print(j,end=' ')
        sum +=1
        print()
        # print('合数')
print(sum)'''

# 第二步：判断素数的方法：输出逻辑结果，质数or合数
'''i = int(input('请输入一个正整数：'))
sum = 0
for j in range(2,i):
    if not(i%j) :
        print(j,end=' ')
        sum +=1
        print()
        # print('合数')
# print(sum)
if sum == 0:
    print('质数')
else:
    print('合数')'''

# 第三步：封装判断素数的方法为一个函数:return 0/1

'''def zhishu(num):
    sum = 0
    for j in range(2, num):
        if not (i % j):
            # print(j, end=' ')
            sum += 1
            # print()
            # print('合数')
    # print(sum)
    if sum == 0:
        return True
    else:
        return False'''
# 优化函数逻辑，简化逻辑表达
'''def is_prime(num):
    if num in (1,2):
        return True
    for j in range(2,num):
        if num%j ==0:
            return False # 如果存在因数，则返回False
    return True # 01 默认返回true'''
# 逆向思维：如果存在因数，直接输出False
# 注意参数一致性，定义名称后尽量粘贴

# num = int(input('请输入一个正整数：'))
# print(zhishu(num))


# 第四步：for循环遍历区间内的数

'''n = int(input('请输入一个正整数：'))
index = 0
for i in range(2,n+1):
    # if zhishu(i):
    if is_prime(i):
        print(i,end=' ')
        index +=1
print()
print(index)'''

# 关键在于先对因数进行计数，然后把计数等于0的情况定义为true，
# 则封装出了一个把计数变成逻辑判断的函数；

# 005 求前n个数字的平方和
# 输入数字n
# 计算1到n的平方和

# 这个应该和斐波那契是一个解法

'''def pfh(num):
    if num == 1:
        return 1
    else:
        res = num*num+pfh(num-1)
        return res

n = int(input('请输入一个大于2的正整数：'))
print(pfh(n))'''

# 另一种写法：
'''def sum_of_square(num):
    result = 0
    for num in range(1,num+1):
        result += num*num
    return result

n = int(input('请输入一个大于2的正整数：'))
print(sum_of_square(n))'''


# 006 计算列表数字的和

'''def sum_of_lst(l): # 定义求和函数
    res = 0
    for i in l:
        # res = res + i 优化写法
        res += i
    return res

# 然后直接调用求和函数
lst1 = [1, 2, 3, 4]
lst2 = [17, 5, 3, 5]

# print(sum_of_lst(lst1))
# print(sum_of_lst(lst2))
print(f'sum of {lst1} =', sum_of_lst(lst1))
print(f'sum of {lst2} =', sum_of_lst(lst2))
print(f'sum of {lst1} =', sum(lst1),'*')
print(f'sum of {lst2} =', sum(lst2),'**')'''

# 内置函数sum可以直接计算
# 格式化快捷键：com+alt+L

# 007 计算范围内所有的偶数
# 直接复用质数的公式，改一行条件

'''def is_even(num):
    # if num in (1,2):
        # return True
    # for j in range(2,num):
    if num%2:
        return False # 如果不能被2整除，则返回False
    return True

n = int(input('请输入一个正整数：'))
res = []
index = 0
for i in range(2,n+1):
    if is_even(i):
        # print(i,end=' ')
        res.append(i)
        index +=1
print(res)
print(index)'''

# 简化写法：1行公式
'''n = int(input('请输入一个正整数：'))
data = [i for i in range(1,n+1) if i%2 == 0]
# 条件表达式
print(data)
print(len(data))'''

# len(list)计算列表中元素的个数,不去重
'''lst1 = [1,3,5,7,3,8,9,12,6,4,38]
print(len(lst1))'''

# 008 移除列表中的多个元素
# remove函数
'''lst1 = [3,5,7,9,11,13]
lst2 = [7,11]

for i in lst2:
    lst1.remove(i)
print(lst1)'''
# new_lst = lst1[lst2]
# 问题：两个列表相减用什么公式


# 009 列表元素去重
# 笨方法，for循环
'''def get_uniq_list(l):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return res

lst1 = [10,20,30,10,20]
print(get_uniq_list(lst1))'''

# 使用set元组
'''lst1 = [10,20,30,10,20]
print(list(set(lst1)))'''

# 010 简单列表元素排序
'''lst1 = [20,40,30,50,10]
lst4 = [20,40,30,50,10]
# 第一种方法
lst1.sort()
print(lst1)
lst4.sort(reverse=True)
print(lst4)

# 注意：不能print list.sort()方法

# 第二种方法
lst2 = [20,40,30,50,10]
lst3 = sorted(lst2)
lst4 = sorted(lst2,reverse=True)
print(lst3)
print(lst4)'''


# 011 学生成绩排序

'''stu =[
    {"sno":101, "sname":'小张',"sgrade":88},
    {"sno":102, "sname":'小王',"sgrade":99},
    {"sno":103, "sname":'小李',"sgrade":77},
    {"sno":104, "sname":'小赵',"sgrade":66}
]

stu1 = sorted(stu, key = lambda x: x["sgrade"])

stu2 = sorted(stu, key = lambda x: x["sgrade"], reverse=True)

print(stu1)
print('***')
print(stu2)'''

# 012 读取成绩文件排序数据

'''def read_file():
    res = []
    with open('./student_grade_input.txt') as fin:
        for line in fin:
            line = line[:-1]
            res.append(line.split(','))
    return res

def sort_grades(datas):
    # res2 =
    return sorted(datas,
                  key=lambda x:  int(x[2]),
                  reverse=True)


def write_file(datas):
    with open('./student_grade_output.txt','w') as fout:
        for data in datas:
            fout.write(','.join(data) + '\n')

# 第一步：读取文件
datas = read_file()
print(datas)
# print(len(datas))
# 第二步：排序文件
datas = sort_grades(datas)
print(datas)


# 第三步：写出文件
write_file(datas)'''

# 013 统计学生成绩文件最高分、最低分、平均分

# 函数部分
'''def compute_score():
    scores = []
    with open('./student_grade_input.txt') as fin:
        for line in fin:
            line = line[:-1]
            fields = line.split(',')
            scores.append(int(fields[2]))
    max_score = max(scores)
    min_score = min(scores)
    avg_score = round(sum(scores)/len(scores),2)
    return max_score,min_score,avg_score


# 运行部分
max_score,min_score,avg_score = compute_score()
print(f'max_score={max_score},min_score={min_score},avg_score={avg_score}')
'''

# 014 统计英文文章中每个单词出现的次数

'''word_count = {}

with open('./count_word_nums.txt') as fin:
    for line in fin:
        line = line[:-1]
        words = line.split() # 为什么用line函数的split方法能直接切分出单词？不理解
        for word in words:
            if word not in word_count:
                word_count[word] = 0 # 字典后面加方括号什么意思？
            word_count[word] +=1 # 怎么通过循环把单词和单词的个数加到字典里的？不理解

# print(word_count)

print(sorted(
    word_count.items(),
    key=lambda x: x[1],
    reverse=True
)[:8])'''

# 015 统计目录下所有文件的大小

'''import os
print(os.path.getsize('count_word_nums.txt'))

sum_size = 0
for file in os.listdir('.'):
    if os.path.isfile(file):
        # print(file)
        sum_size += os.path.getsize(file)

print('all size of dir:', sum_size/1000,'M')
'''


# 016 按文件后缀名整理文件夹

# 怎样获取文件后缀名：
# os.path.splitext('/path/to/aaa/mp3')
# -->输出：('/path/to/aaa','.mp3')

# 怎样移动文件
# import shutil
# shutil.move('aaa.txt','dir/bbb/foo')

'''import os
import shutil

dir ='./arrange_dir'

for file in os.listdir(dir):
    ext = os.path.splitext(file)[1] # 使用这个函数获得后缀名
    ext = ext[1:]  #切片，index以0开始，所以去掉了第一个元素
    # print(file)
    if not os.path.isdir(f'{dir}/{ext}'):
        os.mkdir(f'{dir}/{ext}') # 这个方法可以创建目录
    # print(file,ext)
    source_path = f'{dir}/{file}'
    target_path = f'{dir}/{ext}/{file}'
    shutil.move(source_path, target_path)'''

# 017 递归搜索目录找出最大文件
# 路径位置：/Users/jakob_pc/Desktop/Python实践

# 方法：
# for root,dirs,files in os.walk('python/Lib/email'):
# root  代表当前目录
# dirs  代表当前目录下的子目录
# files 代表当前目录下普通文件

'''import os
search_dir = '/Users/jakob_pc/Desktop/Python实践'

result_files = []
for root,dirs,files in os.walk(search_dir):
    for file in files:
        file_path = f'{root}/{file}'
        result_files.append(
            (file_path,
            os.path.getsize(file_path) / 1000))
    #print(root,dirs,files)

print(sorted(result_files,
       key=lambda x: x[1],
       reverse=True)[:3])'''


# 018 计算班级的高分低分和平均分

'''course_grades = {}
# key: course, value: grade list

with open('course_stu_grade_input.txt') as fin:
    for line in fin:
        line = line[:-1]
        course,sno,sname,grade = line.split('，')
        if course not in course_grades:
            course_grades[course] = []
        course_grades[course].append(int(grade))

# print(course_grades)

for course,grades in course_grades.items():
    print(
        course,
        max(grades),
        min(grades),
        round(sum(grades)/len(grades),2)
    )'''

# 019 实现不同文件的数据关联

'''course_teacher_map = {}
someting = []
course_list = []

with open('course_teacher.txt') as fin:
    for line in fin:
        line = line[:-1]
        course,teacher = line.split('，')
        course_teacher_map[course] = teacher

print(course_teacher_map)

# line_num=1
with open('course_stu_grade_input.txt') as fin:
    for line in fin:
        line = line[:-1]
        course, sno, sname, sgrade = line.split('，')
        teacher = course_teacher_map.get(course)
        something = course, teacher, sno, sname, sgrade
        if something not in course_list:
            course_list.append(something)

# print(type(something))

# datas = course, teacher, sno, sname, sgrade

# print(datas)
with open('course_stu_grade_onput.txt', 'w') as fout:
    for data in course_list:
        fout.write(','.join(data) + '\n')'''

# 020 批量合并多个txt文件
# Python读取文件的2个方法：
# for line in fin 是逐行读取
# content = fin.read() 可以一次性读取文档所有的内容

'''import os

data_dir = './arrange_dir/txt'

contents = []
for file in os.listdir(data_dir):
    file_path = f'{data_dir}/{file}'
    if os.path.isfile(file_path) and file.endswith('.txt'):
        with open(file_path) as fin:
            contents.append(fin.read())
final_content = '\n'.join(contents)

with open('./arrange_dir/final_txt','w') as fout:
    fout.write(final_content)'''
# 以后需要解决一下顺序的问题


print('Goodbye')
