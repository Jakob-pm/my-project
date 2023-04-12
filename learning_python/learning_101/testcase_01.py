# 测试一下load函数

import os

filename = 'student.txt'

student_lst = []
def load(lst):
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            student_old = file.readlines()
            # student = {}
            for i in student_old:
                student = dict(eval(i))
                lst.append(student)


load(student_lst)
for i in student_lst:
    print(i)
    print(type(i))

# print(student_lst)
