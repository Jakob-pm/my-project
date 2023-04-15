# Jakob learning Python 101
author: Jakob
主要关注基础概念，比如列表、字典、循环，以及循环、函数，面向对象编程的思想

## 学习素材来源：
马士兵教育，杨淑娟，图解python入门课程
https://www.bilibili.com/video/BV1wD4y1o7AS/?spm_id_from=333.999.0.0&vd_source=30bab237673b3b5ce295ed306c7fe29c

银角大王，web开发全家桶
https://www.bilibili.com/video/BV1rT4y1v7uQ/?p=2&spm_id_from=pageDriver&vd_source=30bab237673b3b5ce295ed306c7fe29c

date = 03032023
author = Jakob
print('hello world!')
print('Goodbye')

## 目前课程内完成了：
### 101_day1 数据类型，包括int、float、元祖、列表、字典等； 
目前没有学str的部分，后期补上
包括：
demo_dict, demo_item, demo_dict

### 101_day2 循环，包括for-in循环和while循环
具体的练习在demo_if中

### 101_day3 函数的基本知识，包括类、对象、方法等，目前理解对类和方法的理解较差，后期需要实战中加深理解
没有练习

### 101_day4 re正则表达式模块，有了最基础的了解，但需要很多的熟练度
具体的练习在demo_re中

### 101_day5 今天做学生信息管理系统
date: 04/11/2023
开始时间：下午2：35
今天要把这个项目完成，先打开课程把代码抄了，然后再总结一下基本的信息
学生信息管理系统已经完成！！！

### 101_day6 学生信息管理系统整理和调试
date: 04/12/2023
开始时间：下午2：35
今天要把这些代码进行优化，同时把readme文件和.py文件推送到github上
一共有11个函数，尝试规整和优化
整理一下打开文件的几种方法，with open+ pyautogui？
面向对象编程问题，如何让load函数吐出来一个lst参数，其他的函数可以直接用？
else: pass和return是否都可以不写？
目前完成新增+查询+删除

### 101_day7 学生信息管理系统继续整理
date: 04/13/2023
开始时间：下午1：27
已经推送到github上，今天把代码中剩余的函数搞一下，同时做一个系统流程图
修改和排序部分
要注意文件中和缓存列表中每个字段的数据类型
如何处理总分总，并且分的时候会出现重新返回循环的情况，用flag，具体在testcase_02里

### 101_day8 开启Django前后端学习
date: 04/14/2023
开始时间：下午1：59
P2，前端引入和html标签
一句里面引号如果有包含关系，需要用双引号和单引号区分
今天学了flask功能，html标签包括meta charset为解码类型、<!--标题-->、div标签、span标签、a标签、
嵌套标签、列表标签和表格标签
明天继续input标签

### 101_day8 开启Django前后端学习
date: 04/15/2023
开始时间：下午1：00
P6 表单标签
tab键自动补全
input标签(7种)、下拉框、多行文本
input标签包括：text, password, file, radio, checkbox,button & submit
案例，用户注册界面
标签包括：
h/div/span/a/img/ul/ol/table/textarea/select
案例：用户注册
GET请求【URL方法、表单提交】
POST请求【表单提交】
表单提交包括：form标签包裹提交的数据标签，提交方式，提交地址，form标签里要有submit标签
ImmutableMultiDict([('user', 'admin'), ('pwd', '123123'), ('gender', '1'), ('hobby', '0'), ('hobby', '1'), ('hobby', '2'), ('hobby', '3'), ('city', '1'), ('strength', '31'), ('remarks', 'vdfgdgndvdfv\r\nsdfgsdfgdsfb\r\ngdfdfbdf')])
'爱好': ['唱']
'备注': None
request.form.get只能获得一个-->
request.values.getlist可以获取列表
明天是CSS，然后是BootSrap，之后前端总结，接下来学习MySQL数据库