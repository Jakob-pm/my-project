# Jakob learning Python 102
author: Jakob
主要关注经典练习题，比如约瑟夫环、五大湖问题、斐波那契数列、水仙花数

## 学习素材来源：
100道python基础练习题
https://www.bilibili.com/video/BV1SG411H7e1/?spm_id_from=333.788.recommend_more_video.3&vd_source=30bab237673b3b5ce295ed306c7fe29c

时间安排：
计划3天完成，前两天每天完成40道

date = 03032023
author = Jakob
print('hello world!')
print('Goodbye')


## 目前课程内完成了：

### 102_day1
第1天完成了20题，没有统计具体时长
问题1：不够熟练
问题2：小错误引起bug
问题3：知识结构积累，数据结构和算法

### 102_day2
周日，下午1点30开始，从21题开始
'''with open('./student_like_output.txt','w') as fout:
        for data in datas:
            fout.write(' '.join(data) + '\n')'''


 '''if like not in data:
                    data = (like, sname)
                if like in data:
                    data = (data, like)'''

### 102_day3
周一，下午2点43分开始，从28题开始，目前到36题
125行： 这里不能使用表达式，以后需要研究一下，为什么print后面的表达式，if一定要有else
re需要多练习： # 需要查找和总结一些查找日期、手机号和邮箱的re写法
pandas和nupty都装上了，pandas能用但是import pandas还是红色报错
需要一个中文多余符号和无意义词的词典
需要解决一下 utf-8转码的问题



### 102_day4
周二，从下午1点开始，38题已经完成，今天计划完成到58题（按每天20题的速度，到周四可以完成100题）
很多模块比如pandas需要专门的学习，既需要case练习，也需要总结一些基本概念，比如列表与元组的属性&方法和re表达式
046 没有
输出使用format的方法：print(f'{num1}+{num2}={sum}')
解决自己以前提出的一个需求：
生成一组随记数字，一共10个，之和等于360
bin()函数可以看二进制

### 102_day5
周三，计划完成到76题
#列表里面还可以加列表：列表里面的元素是否有顺序？
'''a = []
a.append([1,2])
a.append([2,3])
print(a)

for i in a:
    print(i)'''
kmp字符串匹配算法？
什么都不做用pass

60 输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
针对这个题，为了解决特殊情况的问题，有2种思路：
第一种是罗列出所有的特殊情况，然后分别写出解决逻辑；
第二种是把2个活动解耦，单独进行，这样就不会互相干扰

for循环的次数需要再仔细理解一下
t = 0
for i in range(0,3):
    t += 1
    print('*')
这里循环了3次，为什么最后的t等于3？？
使用不同参数的写法需要总结经验，注意技巧
根据约瑟夫环解决一下提审所有犯人的问题


### 102_day6
尝试一下自己写约瑟夫环
从74题开始，今天一定要完成所有的题目
计划每道题用20分钟时间，一共需要200分钟，加上40分钟buffer应该是4个小时
看一下能超出多少

80 回答结果，结构体变量传递
关于面向对象编程，类和方法需要更多的例子来深入理解

容易把i误写成1
aa =['1','2','3','4']
ss ='' # 必须要这么写吗？
print(int(ss.join(aa)))
a.pop() #默认抛出最后一个元素
#ttributeError: module 'time' has no attribute 'clock'
print(time.perf_counter())
print(parser.parse(time.ctime())) #可以直接打印当前时间

90 从键盘输入一些字符 test_file
问题：可以二次写入，但是二次写入会覆盖掉之前的内容，
怎么样可以接着往下写，而不覆盖之前的内容？
a = a.upper() # 注意有些函数能改变原对象，有些需要接收一下，需要总结

100道题已经完成！！！

