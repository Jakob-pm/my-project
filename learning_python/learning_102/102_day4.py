# date = 03072023
# author = Jakob
# 学习python最好的方式，是大量的做实践练习！
print('hello world!')

# 039 有一个已经排好序的数组，需要插入一个数字，要求符合原来数组排序的规律

'''a = [1,4,6,9,13,16,19,28,40,100,0]
print('before:')
for i in range(0,len(a)-1): #这里理解一下，len(a)是数组的长度，0到len(a)因为是前开后闭，长度刚好等于数组长度
    print(a[i],end =' ')
print()
number = int((input('please input the number you want to insert:')))

# 先找到i的位置，输出i的值
# for i in range(len(a)-1,0,-1):
    # while a[i] > number:
        # i -= 1
# print(a[i+2])

local = 0
for i in range(len(a)-2,-1,-1):
    if number > a[i]:
        local = i + 1
        break
print(local)


for k in range(len(a)-2,local-1,-1):
    a[k+1] = a[k]

a[local] = number

print(a)'''
# 把i后面的值都替换，最后替换a[i]

# 040 将一个数组逆序输出

# 奇数
'''a = [1,2,3,4,5]

# print(len(a))
for i in range(0,(len(a)-1)//2):
    temp = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a) - i - 1] = temp
print(a)
# 偶数
b = [1,2,3,4]
# print(len(b))
for k in range(0,len(b)//2):
    temp = b[k]
    b[k] = b[len(b)-k-1]
    b[len(b) - k - 1] = temp
print(b)'''

# 041 模仿静态变量的用法
# 面向对象的逻辑
'''def test():
    var = 0
    print(var)
    var += 1

test()
test()
test()'''

'''class Test:
    var = 0
    def test(self):
        self.var +=1
        print(self.var)

a = Test()
print(Test.var)
print(a.var)
a.test()
a.test()
a.test()
print(a.var)
print(Test.var)'''

# 042 学习使用auto定义变量的方法

'''num = 2
def test():
    num = 1
    print('test num:%d' % num)
    num += 1
for i in range(3):
    print('num:%d' % num)
    num += 1
    test()'''

# 043 模拟静态变量
# 同样是面向对象的思想
'''class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print('nNum = %d' % self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print('The num = %d' % nNum)
        inst.inc()'''

'''class Test:
    num = 1
    def test(self):
        self.num += 1
        print(self.num)


num = 1
a = Test()
print(Test.num)
num += 1
print(num)
print(a.num)
a.test()
print(a.num)
print(num)
print(Test.num)'''

# 044 两个矩阵相加

'''x = [[12,7,3],
     [4,5,6],
     [7,8,9]]

y = [[5,8,1],
     [6,7,3],
     [4,5,9]]

z = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(3):
    for j in range(3):
        z[i][j] = x[i][j] + y[i][j]

for i in z:
    print(i)
print('*')
print(z)'''

# 045 统计1到100的和

'''temp = 0
for i in range(1,101):
    temp += i
print('the sum is %d' % temp)'''


# 046 没有

# 47 两个变量值互换

'''a = 11
b = 32'''

# 第一种方法：使用第三方变量
'''c = a
a = b
b = c
print(a,b)'''
# 第二种方法：加减法
'''a = a+b
b = a - b
a = a-b
print(a,b)'''
# 第三种方法：语言特性，使用元组的特点
'''a,b = b,a
print(a,b)'''

# 48 比较2个数字大小
'''i = int(input('请输入第一个数字：'))
j = int(input('请输入第二个数字：'))
if i >j:
    print(f'{i} > {j}')
elif i ==j:
    print(f'{i} = {j}')
elif i <j:
    print(f'{i} < {j}')
else:
    print('未知')'''

# 49 使用lambda来创建匿名函数

'''POWER = lambda x,y : x ** y # **代表幂运算
a = 10
b = 20

print(POWER(a,b))'''



# 50 输出一个随机数

'''import random

print(random.randint(10,20))
print(random.random())
print(random.uniform(10,20))'''

# 生成一组随记数字，一共10个，之和等于360


# 51 学会使用按位与&
# 只有2个都是1，结果才是1

'''if __name__ == '__main__':
    a = 0x77
    b = a & 3
    print('a & b = %d' % b)
    b &= 7
    print('a & b = %d' % b)'''
# bin()函数可以看二进制

# 52 学会使用按位或|
# 只要一个是1，结果就是1

'''if __name__ == '__main__':
    a = 0x77
    b = a | 3
    print('a | b = %d' % b)
    b &= 7
    print('a | b = %d' % b)'''

# 53 学会使用按位异^
# 0^0 =0 1^1=0 0^1=1 1^0=1

'''if __name__ == '__main__':
    a = 0x77
    b = a ^ 3
    print('a ^ b = %d' % b)
    b ^= 7
    print('a ^ b = %d' % b)'''

# 交换数据的第4种方法：
# 一个数 对 另一个数 进行 2次 异或运算 得到的结果还是自身
'''a = 10
b = 20
print(a^b^b) #a
print(b^a^b) #a
print(b^a^a) #b
print(a^b^a) #b

a = a^b
b = a^b # = a^b^b 等于a
a = a^b # = (a^b)^a 等于b

print(a,b)'''

# 54 取一个整数a从右端开始的4-7位
# 先使a右移4位，
# 设置一个低4位全为1、其余全为0的数，可用~(~0 << 4)
# 将上面的数进行&运算。

'''if __name__ == '__main__':
    a = int(input('请输入一个整数：'))
    b = a >> 4
    c = ~(~0 << 4)
    d = b & c
    print('%o\t%o' %(a,d))'''

# 55 学会使用按位反~
# 说明：
# 二进制数在内存中以补码的形式存储。
# 按位取反： 二进制每一位取反，0变成1， 1变成0.
# 最高位为符号位，正数的符号位为0，负数为1.
# 对正数而言，最高位是0，其余各位代表数值本身（以二进制表示），
# 如+42 的补码为00101010。
# 对负数而言，把该数绝对值的补码按位取反，然后整个数加1，即得该数的补码，
# 如-42的补码为11010110(00101010)按位取反11010101+1即11010110。
'''print(~9)
print(~(-9 ))'''





print('Goodbye')