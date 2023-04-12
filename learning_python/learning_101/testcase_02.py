# while循环的反面怎么定义
# 答案：while .. else ..循环

i = int(input('请输入一个数字：'))
while i <= 10:
    print('*')
    i-=1
    if i == 0:
        break
else:
    print('invalid')