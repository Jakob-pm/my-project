# jakob
# decode = utf-8
print('hello world!')

# 函数
# 执行特定任何以完成特定功能的一段代码
# 复用代码、隐藏实现细节、提高可维护性、提高可读性便于调试

# 函数 001 函数的创建
'''def calc(a,b): # 形式参数，形参的位置在函数的定义处
    c = a + b
    return c
print(calc(10,20))''' # 实参，实际输入的参数，函数的调用处

# 函数 002 函数调用的参数传递
# 位置传递和关键字传递
# 在函数调用过程中，如果实参是不可变对象，在函数体内的修改不会影响实参的值，
# 如果实参是可变对象，在函数体内的调用会影响实参的值

# 函数 003 函数的返回值

'''def fun(num):
    odd = []
    even = []
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even  #注意return的位置，在def的次一级
print(fun([10,29,34,23,44,53,55]))'''

# 函数的返回值：
# 如果没有返回值，return可以不写
# 如果返回值为1个，直接返回类型
# 如果返回值为多个，返回的结果为元组


# 函数 003 函数的参数
# 个数可变的位置形参
# 个数可变的关键字形参，*，只能采用关键字传递


'''def fun(a,b,c):
    print('a=', a)
    print('b=', b)
    print('c=', c)

fun(10,20,30)

lst=[11,22,33]
fun(*lst)'''

# 函数 003 函数的参数
# 局部变量和全局变量

'''def fun(a,b):
    c = a + b
    return
fun(1,2)'''
# print(c)局部变量，报错
# print(a) 局部变量，报错

'''def fun3():
    global age #生成为全局变量
    age = 20
fun3()
print(age)'''

# 函数 004 递归
# 调用自身的函数叫递归函数
# 组成部分包括递归调用和递归终止条件
# 调用过程，每递归调用一次，都会在栈内存分配一个栈帧，
# 每执行完一次，都会释放相应的空间
# 优点：思路和代码简单
# 缺点：占用内存多，效率比较低（空间换时间？）

'''def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)
print(fac(6))'''

'''def fib(n):
    if n == 1:
        return  1
    elif n == 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(1,7):
    print(fib(i))'''
# 函数 005 两大思想"面向过程、面向对象
# 解决复杂问题，通过面向对象方式便于我们从宏观上把握事物之间复杂的关系、方便我们分析整个系统；
# 具体到围观操作，仍然要使用面向过程方式来处理
# 类=数据类型，对象=实例
# 类的组成：类属性、实例方法、静态方法、类方法
# 在类之内定义的叫方法，在类之外的叫做函数
# 封装、继承、多态



'''if __name__ == '__main__':
    print('-----练习统计质数的个数 -------')
    num = int(input('请输入一个正整数：'))
    print(zhishu(num))'''


print('Goodbye!')