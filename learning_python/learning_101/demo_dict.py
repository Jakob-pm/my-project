# jakob
# decode = utf-8
#   字典{}，键值对形式，无序的序列，形式为key:value
# 字典里的位置根据hash函数算出来的，key是一个不可变的序列；
# key是str，不可以进行增删改；
print('hello world!')

# 字典 001 字典创建
'''dct1 ={'张三':100,'李四':98,'王武':45}
print(dct1)
dct2 = dict(name='Jakob',age=30)
print(dct2)
dct3 = {}
print(dct3)

print(dct1['张三'])
print(dct2['age'])

print(dct2.get('age'))
print(dct2.get('height',606))

print('张三' in dct1)
print('张三' not in dct1)

del dct1['张三']
print(dct1)

dct1['陈六']=67
print(dct1)

dct1['陈六']=100
print(dct1)'''

# 字典 002 获取字典视图
'''dct1 = {'李四':98,'王武':45,'陈六':100} #注意前面不要有空格
keys = dct1.keys()
print(keys)
print(type(keys))
print(list(keys))

values = dct1.values()
print(values)
print(type(values))
print(list(values))

items = dct1.items()
print(items)
print(type(items))
print(list(items))'''

# 字典 003  字典元素遍历
'''dct1 = {'李四':98,'王武':45,'陈六':100}

for item in dct1:
 print(item,dct1[item],dct1.get(item))'''

# 字典 004 字典的特点
print('5个特点：')
print('字典中所有元素都是一个键值对，key不允许重复，value可以重复')
print('字典中的元素是无序的')
print('字典中的key必须是不可变对象')
print('字典也可以根据需要动态伸缩')
print('字典会浪费较大的内存，是一种使用空间换时间的数据结构')

# 字典 005 字典生成式
items=['fruits','books','others']
prices=[98,78,85]
lst=zip(items,prices)
dct1 = {item.upper():price for item,price in zip(items,prices)}
print(list(lst))
print(dct1)

'''if __name__ == '__main__':
    print('-----练习统计质数的个数 -------')
    num = int(input('请输入一个正整数：'))
    print(zhishu(num))'''


print('Goodbye!')