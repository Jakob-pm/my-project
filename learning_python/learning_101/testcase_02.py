# while循环的反面怎么定义
# 答案：while .. else ..循环

# i = int(input('请输入一个数字：'))
# while i <= 10:
#     print('*')
#     i-=1
#     if i == 0:
#         break
# else:
#     print('invalid')

# break到底是怎么作用的，如何忽略下面的代码，直接跳到下一个循环？
# 目前想到的方法是加一个flag，
lst = [i for i in range(1,100,1)]
print(lst)
while True:
    roottie = int(input('请输入过几？'))
    flag = True
    if roottie == 3:
        lst_new = []
        for i in lst:
            if i %3 !=0: # 整除符号是%，取余符号是//
                lst_new.append(i)
    elif roottie == 7:
        lst_new = []
        for i in lst:
            if i %7 !=0: # 整除符号是%，取余符号是//
                lst_new.append(i)
    elif roottie == 13:
        lst_new = []
        for i in lst:
            if i %13 !=0: # 整除符号是%，取余符号是//
                lst_new.append(i)
    else:
        print('请重新选择')
        flag = False
    if flag:
        print(lst_new)
        answer = input('是否继续？y/n')
        if answer == 'y':
            continue
        else:
            break
