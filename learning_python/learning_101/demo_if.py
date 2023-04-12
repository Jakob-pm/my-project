# jakob
# decode = utf-8
print('hello world!')

# 循环
# 主要包括for循环和while循环

'''money = 1000

s = int(input('请输入取款金额'))

if money >=s:
    print('剩余金额为：',str(money-s))

else:
    print('余额不足，不能取款')
'''

'''
s = int(input('请输入一个数字'))

if s%2 == 0:
    print(s,'是偶数')
else:
    print(s,'是奇数')
'''

'''
note = int(input('请输入查询成绩：'))

if note >=90 and note <=100:
    print('您的成绩为优')
elif note < 90 and note >= 70:
    print('您的成绩为良')
elif note < 70 and note >= 60:
    print('您的成绩及格')
elif note <60 and note >= 0:
    print('成绩不及格，请继续努力')
else:
    print('请输入有效数据')
'''

'''
note = int(input('请输入查询成绩：'))

if 90 <= note <=100:
    print('您的成绩为优')
elif 70 <= note < 90:
    print('您的成绩为良')
elif 60 <= note < 70:
    print('您的成绩及格')
elif 0 <= note <60:
    print('成绩不及格，请继续努力')
else:
    print('请输入有效数据')
'''

'''
answer = input('请问您是否是会员')
money = float(input('请输入购物金额'))
# 注意⚠️： input类型统一为string类型，需要转换为int或float类型再进行计算

if answer == 'y':
    if money >= 200:
        print('打8折，请交费')
        print(money*0.8)
    else:
        print('打9折，请交费')
        print(money * 0.9)
else:
    if money >= 200:
        print('打9折，请交费')
        print(money * 0.9)
    else:
        print('无折扣，请交费')
        print(money)
'''
'''
num_a=int(input('请输入第一个整数'))
num_b=int(input('请输入第二个整数'))
'''
# 比较大小
'''if num_a >= num_b:
    print(num_a,'大于等于',num_b)
else:
    print(num_a, '小于', num_b)
    
# 使用条件表达式
'''
# print(str(num_a)+'大于等于'+str(num_b) if num_a >= num_b else str(num_a)+ '小于'+ str(num_b))

'''
age = int(input('请输入年龄：'))

if age:
    print('年龄为：',age)
else:
    print('输入错误')
'''

# r = range(9)
# print(list(r))

'''import random
r = random.random()
n = random.random()
print(r,n)
'''

# print(range(1,100,9))
# 计算1到4的和：
'''a = 0
s = 0
while a<5:
    # print(a)
    s = s + a
    a+=1
print(s)'''

#计算100以内所有的偶数的和
# 使用while循环
'''a = 1  #初始值
sum = 0
while a < 101:
    if a%2 == 0: #如果a整除2等于0，意味着a是偶数；
        sum+=a
    a+=1 #循环时加一
print(sum)'''

# 使用for循环
'''sum = 0
for i in range(1,101): #range函数前开后闭，包括开头，不包括结尾：从1到100；
    if not (i%2): # 使用了布尔运算，整除时为0，等于false，所以加上not再往下执行；
        sum+=i
print(sum)'''

#找到所有的水仙花数
'''s = 0
for i in range(100,1000):
    ge = i%10 #%是取余数，841除以10的商是84，余数是个位的1
    shi = i//10%10 #先得到商，再取余数
    bai = i//100  #直接整除100，商为百位数
    if i == ge**3+shi**3+bai**3:
        print(i)
        s+=1
print(s) #计循环次数'''

# ATM机输入密码问题，逻辑嵌套循环
'''for i in range(3):  #使用for循环不能模拟超过3次后密码锁死
    pwd=input('请输入密码：')
    if pwd == '8888':
        print('密码正确，请进入')
        break
    else:
        print('密码不正确，请重新输入' if i <2 else '错误超过3次，请明天再试') # range(3)中为0、1、2，使用条件表达式'''
#print('错误超过3次，请明天再试')

#ATM3次密码问题，穷举法
'''i = 0
pwd = int(input('请输入密码：'))
while i <=3:
    if pwd == 8888:
        print('密码正确，请进入')
        break
    i += 1'''
'''if i <3:
        print('密码不正确，请重新输入')
else:
        print('错误超过3次，请明天再试')'''

'''pwd1 = int(input('请输入密码：'))
if pwd1 == 8888:
    print('密码正确，请进入')
else:
    print('密码不正确，请重新输入')
    pwd2 = int(input('请输入密码：'))
    if pwd2 == 8888:
        print('密码正确，请进入')
        br
    else:
        print('密码不正确，请重新输入')
        pwd3 = int(input('请输入密码：'))
        if pwd3 == 8888:
            print('密码正确，请进入')
        else:
            print('错误超过3次，请明天再试')'''

# 数字菱形核心逻辑：
# i = int(input('请输入一个数字'))
# while循环写法
'''j = 1
K = i
while j < i:
    print(j, end='')
    j+=1
while k > 0:
    print(k,end='')
    k-=1
print()'''
# for循环写法
'''for j in range(1,i):
    print(j, end='')
for k in range(0,i):
    print(i-k,end='')
print()'''
# 缩减写法
'''for j in range(-i+1,i):
    print(-abs(j)+i, end='')
print()'''

#把for循环封装成函数：
'''def lingxing(length):
    for k in range(-length+1,length):
        print(-abs(k) + length, end='')
    print()
    return

print(lingxing(int(input('请输入一个数字：'))))'''


'''def diamond(leng):
    for j in range(1,leng+1):
        print(' '*(leng-j),end='')
        # print('*', end='')
        for k in range(-j+1,j):
            print(-abs(k)+j, end='')
            # print('*', end='')
        print()
    for m in range(1,leng):
        print(' ' * m, end='')
        for n in range(-leng+m+1,leng-m): #注意等值性和反向关系，这里的leng-m对应上一种情况里的j，同时range的范围跟m的大小是反向的；
            print(-abs(n)+leng-m, end='')
        print()
    return "Done"
# print(lingxing(int(input('请输入一个数字：'))))
if __name__ == '__main__':
    print('-----练习输出菱形数字图形 -------')
    leng = int(input('请输入一个数字：'))
    print(diamond(leng))'''

# 打印数字菱形
# i = int(input('请输入一个数字'))
'''l = 1
while l <= i:
    j = 1
    k = l -1
    print(' '*(i-l),end='')
    while j <=l:
        print(j, end='')
        j+=1
    l += 1
    while k > 0:
        print(k, end='')
        k-=1
    print('')
m = i-1
while m >0:
    j = 1
    k = m-1
    print(' ' * (i-m), end='')
    while j <=m:
        print(j,end='')
        j+=1
    while k>0:
        print(k, end='')
        k-=1
    print('')
    m-=1'''

'''for l in range(1, i+1):
    print(' '*(i-l),end='')
    for j in range(1,l+1):
        print(j,end='')
    for k in range(l-1,0,-1):
        print(k,end='')
    print()
for l in range(i-1,0,-1):
    print(' ' * (i-l), end='')
    for j in range(1,l):
        print(j, end='')
    for k in range(l, 0, -1):
        print(k, end='')
    print()
    # print('*')
'''

'''for l in range(1,i+1):
    print(' '*(i-l),end='')
    for j in range(1,l):
        print(j,end='')
    for k in range(l,0,-1):
        print(k,end='')
    print()
for l in range(1,i):
    print(' '*l,end='')
    for j in range(1,i-l):
        print(j,end='')
    for k in range(i-l,0,-1):
        print(k,end='')
    print()'''

#菱形
'''i = int(input('请输入一个数字'))
for j in range(-i+1,i):
    print(' '*abs(j)+'*'*((i*2-1)-abs(j)*2))
'''

#九九乘法表
'''
for i in range(1,10):
    for k in range(1,i+1): # 双层嵌套，小数在前
        print(k,'*',i,'=',k*i,' ',end='') #注意不换行，使用end函数
    print() #  注意换行
'''
# 逻辑循环练习
'''for t in ['a','b','c','d']:
    if (t != 'a')+(t == 'c')+(t == 'd')+(t != 'd') == 3:
        print(t)'''

#求正整数的因子
# 使用while循环
# i = int(input('请输入一个正整数：'))
'''j = 1
k = 0
while j <= i:
    if i%j ==0:
        print(j)
        k+=1
    j+=1'''
# 使用for循环
'''k = 0
for j in range(1,i+1):
    if i%j ==0:
        print(j)
        k+=1'''
# print('数字',i,'的因子一共有',k,'个')
# 定义函数
'''def yinzi(num):
    k = 0
    for j in range(1,num):
        if num%j ==0:
            print(j)
            k+=1
    print('数字',num,'的因子一共有',k,'个。')
    return 'Done'

if __name__ == '__main__':
    print('-----练习计算因子 -------')
    num = int(input('请输入一个正整数：'))
    print(yinzi(num))'''

'''for i in range(1,101):
    for j in range(1,i):
        if'''

# 计算100以内的质数：
# 确定质数的条件：
'''i = int(input('请输入一个正整数：'))
k = 0
for j in range(1,i):
    if i%j ==0:
        # print(j,'*')
        k+=1
# print(k)
if k == 0 or k == 1:
    print('质数')
    # print(i, end=' ')
    # sum+=1
else:
    print('合数')'''
#计算100以内的质数，包括1
'''sum = 0
for i in range(1,1000):
    k = 0
    for j in range(1,i):
        if i%j ==0:
            # print(j,'*')
            k+=1
    # print(k)
    if k == 1 or k == 0:
        # print('奇数')
        # print(i, end=' ')
        sum+=1
    # else:
        # print('偶数')
# print()
print(sum)'''
#  写成函数形式，计算到某个数一共有多少个质数：
'''def zhishu(num):
    sum = 0
    for i in range(2,num+1):
        k = 0
        for j in range(1,i):
            if i%j ==0:
                # print(j,'*')
                k+=1
        # print(k)
        if k == 1:
            # print('奇数')
            print(i, end=' ')
            sum+=1
        # else:
            # print('偶数')
    print()
    print('质数一共有',sum,'个。')
    return 'Done'


if __name__ == '__main__':
    print('-----练习统计质数的个数 -------')
    num = int(input('请输入一个正整数：'))
    print(zhishu(num))'''

# 逻辑推理：四大湖问题

for dth in [1,2,3,4]:
    for hzh in [1,2,3,4]:
        for pyh in [1, 2, 3, 4]:
            for th in [1, 2, 3, 4]:
                if (dth == 1) + (hzh == 4) + (pyh == 3) == 1:
                    if (hzh == 1) + (dth == 4) + (pyh == 2) + (th == 3)== 1:
                        if (hzh == 4) + (dth == 3)== 1:
                            if (pyh == 1) + (th == 4) + (hzh == 2) + (dth == 3)== 1:
                                if dth !=hzh and dth !=pyh and dth !=th and hzh !=pyh and hzh !=th and pyh !=th:
                                    print('dth=', dth)
                                    print('pyh=', pyh)
                                    print('hzh=', hzh)
                                    print('th=', th)


# continue 和 break的区别是，continue是跳过本次循环中接下来的代码，break是直接跳过后续的循环次数
'''for i in range(1,26):
    if i%3 ==0:
        continue
    print(i)'''



print('Goodbye!')