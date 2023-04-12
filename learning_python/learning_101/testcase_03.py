# 列表的直接替换
# lst1 = [0,1,2]
# lst2 = [2,3,4,5]
# lst1 = lst2
# print(lst1)

'''lst1 = [0,1,2,3,4,5]
t = int(input())
while lst1:
    lst2 = []
    for i in lst1:
        if i != t:
            lst2.append(i)
    lst1 = lst2
    print(lst1)
    answer = input('是否继续删除？y/n')
    if answer == 'y':
        continue
    else:
        break

print(lst1)'''

# 把del函数单独拿出来试一下

import time
import os

def delet():
    student_lst = []
    load(student_lst)
    print(len(student_lst))
    while student_lst:
        student_lst_new = []
        flag = False
        student_id = input('请输入要删除的学生ID：')
        for student in student_lst:
            if student['id'] != student_id:
                student_lst_new.append(student)

            else:
                flag = True
        print(len(student_lst_new))
        student_lst= student_lst_new
        print(len(student_lst))
        if flag:
            print(f'id为{student_id}的学生信息已被删除！')
        else:
            print(f'未找到id{student_id}为的学生信息！')
        save(student_lst)
        print('$')
        answer = input('是否继续删除？y/n')
        if answer == 'y':
            continue
        else:
            print('*')
            break


def save(lst):
    # 把原始存储数据读取到缓存
    student_lst = []
    load(student_lst)
    # 把新增的学生信息加到缓存列表中
    for i in lst: # 这里i指的是每一个学生的信息，即列表里的字典
        student_lst.append(i)
    # 按学号排序(包括原始+新增部分)
    student_lst.sort(key=lambda x: int(x['id']), reverse=False)
    # 写入文件，真正的save部分，覆盖模式
    with open(filename, 'w', encoding='utf-8') as file:
        for i in student_lst:
            file.write(str(i)+'\n')


def load(lst):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
            for i in student_old:
                student = dict(eval(i))
                lst.append(student)


filename = 'student.txt'

delet()
student_lst = []
load(student_lst)
print(len(student_lst))

# 先把代码改对，然后清洗数据
# 注意，所有增删改给到save函数的都是完成信息，save只负责按学号排序并保存到文件，增删改要检查自己输出的列表是否完整和重复

