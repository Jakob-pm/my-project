# 如何从列表中删除一个元素

# 01循环写入新列表
# lst1 = [0,1,2,3,4,5]
# t = int(input())
# while lst1:
#     lst2 = []
#     for i in lst1:
#         if i != t:
#             lst2.append(i)
#     lst1 = lst2
#     print(lst1)
#
#
# print(lst1)

# 02 表达式形式
lst1 = [0,1,2,3,4,5]
lst2 = [i for i in lst1 if i != 3]
print(lst2)
