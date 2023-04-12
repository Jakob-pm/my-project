# 列表相当于其他语言中的数组
print('hello world!')

# 列表
# 列表的创建、排序和索引

# list 001 列表的ID、类型和内容
'''lst =['hello','world',98]
print(id(lst))
print(type(lst))
print(lst)'''
'''4374100864
<class 'list'>
['hello', 'world', 98]'''

# list 002 列表的创建
## 01 使用方括号
'''lst1 =['hello','world',98]'''
## 02 使用内置函数list
'''lst2 =list(['hello','world',98])
print(lst1 == lst2)
print(lst1 is lst2) #False,值相同，但是ID不同'''

# list 003 索引正向从0开始，反向从-1开始
'''lst1 =['hello','world',98,'hello']
print(lst1[0])  #hello
print(lst1[-1]) #98
print(lst1.index('hello'))
print(lst1.index(98))
print(lst1.index('hello',1,4))
print(lst1[0])
print(lst1[-3])
#print(lst1[-10])
## 列表切片：前开后闭，start、stop、step,默认步长为1，start如果不写，默认是0，stop默认为最后一个
print(lst1[0:3:2])
print(type(lst1[0:3:2]))
## step为负数时，反向查找
print(lst1[::-1])'''

# list 004 增删改
'''lst1 =['hello','world',98,'hello']
print(id(lst1))
lst1.append(100)
print(lst1)
print(id(lst1)) # 列表的ID不变
lst2 = ['python',100]
lst1.extend(lst2)
print(lst1)
lst1.insert(1,90)
print(lst1)
lst3=[1,2,3]
lst1[1:]=lst3
print(lst1)
lst1.remove('hello') #移除指定内容
print(lst1)
lst1.extend(lst2)
print(lst1)
lst1.pop(3) #按照index移除内容
print(lst1)
lst1[1:3]=[] #反向删除
print(lst1)
lst1.clear()
print(lst1)
del lst1
##修改
lst1 = [10,20,30,40]
lst1[3]=100
print(lst1)
lst1[1:3]=[200,300,500]
print(lst1)'''


# list 005 列表排序, sort升序，revers降序
'''lst1 = [13,56,69,32,47,53,38,69,70,2,15]
lst1.sort()
print(lst1)
lst1.sort(reverse=True)
print(lst1)
lst1.sort(reverse=False)
print(lst1)
lst1 = [13,56,69,32,47,53,38,69,70,2,15]
print(lst1)
lst2 = sorted(lst1,reverse=True)
print(lst2)'''

# list 006 列表生成式
lst1 = [i*i for i in range(0,10)]
print(lst1)
lst2 = [i*2 for i in range(1,11)]
print(lst2)
lst3 = [i for i in range(2,21,2)]
print(lst3)

'''4507466624
['hello', 'world', 98, 'hello', 100]
4507466624'''


'''if __name__ == '__main__':
    print('-----练习统计质数的个数 -------')
    num = int(input('请输入一个正整数：'))
    print(zhishu(num))'''


print('Goodbye!')