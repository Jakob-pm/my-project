# 关于流程控制
# 01 while循环的反面怎么定义
# 答案：while .. else ..循环

# i = int(input('请输入一个数字：'))
# while i <= 10:
#     print('*')
#     i-=1
#     if i == 0:
#         break
# else:
#     print('invalid')

# 02 break到底是怎么作用的，如何忽略下面的代码，直接跳到下一个循环？
# 目前想到的方法是加一个flag，
# lst = [i for i in range(1,100,1)]
# print(lst)
# while True:
#     roottie = int(input('请输入过几？'))
#     flag = True
#     if roottie == 3:
#         lst_new = []
#         for i in lst:
#             if i %3 !=0: # 整除符号是%，取余符号是//
#                 lst_new.append(i)
#     elif roottie == 7:
#         lst_new = []
#         for i in lst:
#             if i %7 !=0: # 整除符号是%，取余符号是//
#                 lst_new.append(i)
#     elif roottie == 13:
#         lst_new = []
#         for i in lst:
#             if i %13 !=0: # 整除符号是%，取余符号是//
#                 lst_new.append(i)
#     else:
#         print('请重新选择')
#         flag = False
#     if flag:
#         print(lst_new)
#         answer = input('是否继续？y/n')
#         if answer == 'y':
#             continue
#         else:
#             break


# 03 总分总，如果几种情况都需要执行后续的代码块，保留else开口就行了
# if只是一个判断，并不是选择，不需要保持封闭，所以如果总分总，一直使用elif不要使用else就行了
# for i in [2,3,4,5]:
#     if i ==2:
#         index = 1
#     elif i == 3:
#         index = 1
#     elif i == 4:
#         index = 1
#     elif i == 5:
#         index = 2
#     else:
#         print('不可能') # 这句代码永远不会用到，也不需要一个else
#     print(index)
# 这个也能写成表达式
# for i in [2,3,4,5]:
#     index = 2 if i ==5 else 1
#     print(index)

# 04 成绩问题
# 第一种方法，字典，使用整除//把成绩变成十位数字，使用字典的get方法获得对应成绩等级，设定一个不及格对应的默认值；
# while True:
#     score = int(input('请输入学生成绩：'))
#     grade_dict = {10:'A',9:'A',8:'B',7:'C',6:'D'}
#     grade = grade_dict.get(score//10,'F')
#     print(grade)
#     answer = input('是否继续进行：(y/n)')
#     if answer == 'n' or answer == 'N':
#         break
# 字典的另外一种写法
# scr = int(input('请输入学生成绩：'))
# grades = {"A": 90, "B": 80, "C": 70, "D": 60}
#
# def convert_grade(scr):
#     for ltrgrd, numgrd in grades.items():
#         if scr >= numgrd:
#             return ltrgrd
#     return "F"
# print(convert_grade(scr))

# 第二种方法，定义一个函数
# scr = int(input('请输入学生成绩：'))
# def convertgrade(scr):
#     if scr >= 90:
#         print('A')
#         return
#     elif scr >= 80:
#         print('B')
#         return
#     elif scr >= 70:
#         print('C')
#         return
#     elif scr >= 60:
#         print('D')
#         return
#     elif scr < 60:
#         print('F')
#         return
# convertgrade(scr)

# 转成这样看不懂了
# def convertgrade(scr, numgrd, ltrgrd):
#     if scr >= numgrd:
#         return ltrgrd
#     if scr < numgrd:
#         return ltrgrd
# convertgrade(scr, 0.9, 'A')
# convertgrade(scr, 0.8, 'B')
# convertgrade(scr, 0.7, 'C')
# convertgrade(scr, 0.6, 'D')
# convertgrade(scr, 0.6, 'F')

# 第三种方法，bisect
# from bisect import bisect
# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#      i = bisect(breakpoints, score)
#      return grades[i]
# print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

# 第四种方法，使用next和zip实现
# scr = int(input('请输入学生成绩：'))
# def grade(scr):
#     grades = zip('ABCD', (90, 80, 70, 60))
#     return next((grade for grade, limit in grades if scr >= limit), 'F')
# print(grade(scr))

# 第五种方法，使用numpy
# 以后学了numpy再看
# import numpy as np
# x = np.array([0.9,0.8,0.7,0.6,0.5])
#
# conditions  = [ x >= 0.9,  x >= 0.8, x >= 0.7, x >= 0.6]
# choices     = ['A','B','C','D']
#
# np.select(conditions, choices, default='F')
# array(['A', 'B', 'C', 'D', 'F'], dtype='<U1')



