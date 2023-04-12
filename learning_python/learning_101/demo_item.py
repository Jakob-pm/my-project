# jakob
# decode = utf-8
print('hello world!')

# 元组和集合, tuple
# 元组没有增删改查，元组没有生成式，因为元组是不可变序列，内置数据结构
# 可变序列：列表、字典
# 不可变序列：str和元组
# 列表方括号，元组圆括号

# 元组 001 生成式
'''t1 = ('python','world',98)
print(t1)
print(type(t1))
print(id(t1))

t2 = 'python','world',98
print(t2)
print(type(t2))
print(id(t2))

t3 = tuple(('python','world',98))
print(t3)
print(type(t3))
print(id(t3)) # 元组id唯一

t4 = ('python',)
print(t4)
print(type(t4))
print(id(t4))'''

# 元组 002 空元组
'''lst = []
lst1 = list() #内置函数

dct = {}
dct1 = dict() #内置函数

t = ()
t1 = tuple() #内置函数

print('空列表',lst,lst1)
print('空字典',dct,dct1)
print('空元组',t,t1)'''


# 元组 003 为什么元组设计为不可变序列
# 元组存储的是对象的引用
# a)如果元组中的对象本身是不可变对象，则不能再引用其他对象
# b)如果元组中的对象是可变对象，则可变对象本身的引用不允许改变，但是数据可以改变
'''print('多任务环境下，同时操作对象时不需要加锁')
print()
t = (23,[20,30],56)
print(t)
print(type(t))
print(id(t))
print(t[0],type(t[0]),id(t[0]))
print(t[1],type(t[1]),id(t[1]))
print(t[2],type(t[2]),id(t[2]))

t[1].append(100)
print(t)
print(t[1],type(t[1]),id(t[1]))
print(id(t))'''

# 元组 004 元组的遍历
'''t = (23,[20,30],56)
for item in t:
    print(item)'''

# 集合
# 集合是python提供的内置数据结构
# 集合与列表、字典一样都属于可变类型的序列
# 集合是没有value的字典

# 集合 001 集合的创建
'''s = {2,3,3,4,5,7,9,12,15,13,11,9} # 集合的元素不允许重复，相当于字典的key不允许重复
print(s)

s1 = set(range(6))
print(s1)

s2 = set([1,2,2,2,2,4,5])
print(s2)

# s3 = set({3,4,[2,3],4}) #集合中的元素不能为列表
# print(s3)

s4 = set('Python')
print(s4)

s5 = set({123,3,4,4,5})
print(s5)

s6 = set()
print(s6)'''

# 集合 002 集合的操作
# s = set({10,20,30,40,50,60,10})
'''s = {10,20,30,40,50,60,10} # 去掉注释一定要注意不能留空格
print(10 in s)
print(10 not in s)
print(100 in s)
print(100 not in s)

s.add(80)
print(s)

s.update([100,90,70,55])
print(s)

s.update((23,67,88))
print(s)

# 移除：
s.remove(55)
print(s)
# romove和discard都是一次只删除一个元素，remove会报错keyerror，discard不会报错
s.pop()
print(s)
s.pop()
print(s)'''
# 集合 002 集合的运算
'''s1 = {10,20,30,40}
s2 = {40,10,30,20}
print(type(s1))
print(s1 == s2)
print(s1 != s2)'''

'''s3 ={10,20,30,40,50}
s4 ={10,20,30}
s5 ={10,30,90}
s6 = {80,90}
print(s4.issubset(s3))
print(s5.issubset(s3))
print()
print(s3.issuperset(s4))
print(s3.issuperset(s5))
print()
print(s3.isdisjoint(s6))
print(s4.isdisjoint(s5))'''

# 集合 003 集合的数据运算
'''s3 ={10,20,30,40,50}
s4 ={10,20,30}
s5 ={10,30,90}
s6 = {80,90}

print(s4&s5)
print(s5.intersection(s4))

print(s5|s4)
print(s5.union(s4))

print(s4-s5)
print(s4.difference(s5))

print(s4^s5)
print(s4.symmetric_difference(s5))'''

# 集合 004 集合生成式
# 将{}变成[]就是列表生成式
# 没有元组生成式
lst = [i for i in range(10)]
print(lst)

s = {i for i in range(10)}
print(s)
# 总结
# 数据结构       是否可变   是否重复  是否有序   定义符号
# 列表(list)    可变        可重复    有序       []
# 元组(tuple)   不可变     可重复     有序       ()
# 字典(dict)    可变     key不可重复  无序   {key:value}
# 集合(set)     可变      不可重复    无序       {}


'''if __name__ == '__main__':
    print('-----练习统计质数的个数 -------')
    num = int(input('请输入一个正整数：'))
    print(zhishu(num))'''


print('Goodbye!')