# Jakob learning Python 103
author: Jakob
主要关注pyautogui库

## 学习素材：
40个Python自动化项目
https://www.bilibili.com/video/BV17a411o7Hh/?spm_id_from=333.999.0.0&vd_source=30bab237673b3b5ce295ed306c7fe29c

时间安排：
计划2天完成，今天和下周一

date = 03102023
author = Jakob
print('hello world!')
print('Goodbye')

## 目前课程内完成了：

### 103_day1
03.10,下午1点17分开始

终端输入pip3 list，可以查看目前安装的Python库的模块

print(wb.nsheets)# 属性
print(wb.sheet_names()) #方法
属性和方法的区别是？？
xlrd库的官方文档：https://xlrd.readthedocs.io/en/latest/index.html
https://zhuanlan.zhihu.com/p/390813018
https://blog.csdn.net/memory_qianxiao/article/details/80953186
https://www.programcreek.com/python/example/6932/xlwt.Workbook
xlwt官方文档：https://pypi.org/project/xlwt/1.0.0/
https://blog.csdn.net/weixin_50648794/article/details/109716526
!!! 读写格式的文件属性和方法很不一样，需要注意！

04 xlwt 设置样式
这个案例中还是覆盖了之前的文件
https://vimsky.com/examples/detail/python-ex-xlwt-Font-colour_index-method.html

font color index

04 xlwt 设置样式
color_index没有生效--->
ft.colour_index = 4 写成colour
case, 把index代表的颜色用for循环打出来，但是后一个write的动作会覆盖前一个文件，这个问题需要想办法解决一下



### 103_day2
从# 05 数据的汇总案例开始
今天只搞这一个-->完成

### 103_day3

从# 06开始，计划完成到#11
#06
原始数据：/Users/jakob_pc/Desktop/Python实践/表格拆分.xls
表头定义：'type' 'item' 'amount' 'sum'
all_data 层级结构是：
{
'A':[{},{},{}],
'B':[{},{},{}],
'C':[{},{},{}]
}
{'A': [{'type': '水果', 'item': '杨桃', 'amount': 3.0, 'sum': 20.0}, {'type': '水果', 'item': '樱桃', 'amount': 5.0, 'sum': 50.0}, {'type': '水果', 'item': '草莓', 'amount': 8.0, 'sum': 30.0}, {'type': '水果', 'item': '石榴', 'amount': 7.0, 'sum': 6.0}, {'type': '水果', 'item': '香蕉', 'amount': 9.0, 'sum': 10.0}], 'B': [{'type': '生活用品', 'item': '纸巾', 'amount': 20.0, 'sum': 3.0}, {'type': '生活用品', 'item': '洗衣液', 'amount': 1.0, 'sum': 30.0}, {'type': '生活用品', 'item': '床单', 'amount': 3.0, 'sum': 60.0}, {'type': '生活用品', 'item': '口罩', 'amount': 50.0, 'sum': 1.5}, {'type': '生活用品', 'item': '充电器', 'amount': 1.0, 'sum': 30.0}], 'C': [{'type': '零食', 'item': '薯条', 'amount': 5.0, 'sum': 6.0}, {'type': '零食', 'item': '花生', 'amount': 3.0, 'sum': 20.0}, {'type': '零食', 'item': '沙琪玛', 'amount': 6.0, 'sum': 4.0}, {'type': '零食', 'item': '辣条', 'amount': 3.0, 'sum': 5.0}]}
每一行数据是一个最内层的字典：
{'type': '水果', 'item': '杨桃', 'amount': 3.0, 'sum': 20.0}

#07
Requirement already satisfied: et-xmlfile in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from openpyxl) (1.1.0)
原始文档用：
/Users/jakob_pc/Desktop/Python实践/表格拆分02.xls
到7点完成2个，明天从#8继续(openpyxl创建Excel)


### 103_day4
20230326
计划从#08开始，完成到10；

### 103_day5
20230327
#8 继续，不知道今天能完成几个；
从set values输入多个值开始；

## 103_day6
20230328
#8 继续，还剩最后15分钟；
set_chart应该没有什么问题了。
下午13：46，#8终于搞完了

### 103_day7
20230329
#11 生成excel工资条
下午2：21开始，到3点计划完成11题，注意提高效率！！
检查光标位置，检查输入法，打开B站，开始干活！
原始文档：/Users/jakob_pc/Desktop/Python_datas/103_day7/data11/salary_list.xlsx
把发送邮件一块整了
https://blog.51cto.com/u_15326986/3328762
收获：获得表头的公式
title = [cell.value for cell in list(list(sh1.rows)[0])]
#12 隔行变色
/Users/jakob_pc/Desktop/Python_datas/103_day7/data12.xlsx
for i in range(2, sh1.max_row+1,2):
用range设定for循环触发条件，减少循环次数

### 103_day8
2023/03/30
#13 快速统计加班时间


### 103_day9
2023/03/31
开始时间，下午13：31
视频倍速1.25
#14 快速查excel重复数据
/Users/jakob_pc/Desktop/Python_datas/103_day9/data14.xlsx


#15 身份证号提前信息
data_only = True
sh3 = wb.create_sheet('数据')
for i, d in enumerate(data):
   sh1.cell(i + 1, 1).value = d
[
[],[],[],[]
]
join函数：
a =1
b= 3

s =''
s = s.join(str(a)+'年'+str(b))
print(s)
不要回写到原始数据。
 t_data[0] = t_data[0].date() #日期格式的处理
表达式的写法：
row[0] = (row[0].date() if type(row[0]) != str else row[0])

word、pdf和ppt先跳过，先发邮箱搞定

#35 批量发送邮件
/Users/jakob_pc/Desktop/Python_datas/103_day9/data35.xlsx

<table>
    <tr>    table_head
        <td>工号</td>
        <td>姓名</td>
        <td>基本工资</td>
        <td>保险</td>
        <td>总金额</td>
    </tr>
    <tr>    table_info
        <td>工号</td>
        <td>姓名</td>
        <td>基本工资</td>
        <td>保险</td>
        <td>总金额</td>
    </tr>
</table>

工号	姓名	职务	基本工资	提成	加班工资	社保扣除	考勤扣除	应发工资	邮箱
10000	刘备	首领	8,000.00 	5,000.00 	3,000.00 	680.00 	0.00 	15,320.00 	405fjl@163.com

#32 发送普通邮件
msg_body = MIMEText(mail_text,'plain','utf-8')
smtp_obj.sendmail('1551786081@qq.com','405fjl@163.com',msg_body.as_string())
done!

#33 发送html邮件
<h1></h1>
<p></p>
<p><a href = ''></a></p>

msg_body = MIMEText(mail_text,'html','utf-8')
msg_body['From'] = Header('测试邮箱','utf-8')
msg_body['To'] = Header('employee')
msg_body['Subject'] = Header('测试测试！！！','utf-8')


#34 发送附件邮件
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

multi_part = MIMEMultipart()
multi_part.attach(msg_body)

multi_part.attach(file)

smtp_obj.sendmail('1551786081@qq.com','405fjl@163.com',multi_part.as_string())


进阶一下：
发送多个附件
/Users/jakob_pc/Desktop/Python_datas/103_day7/data11

多一层for循环就可以了：
for name in os.listdir('/Users/jakob_pc/Desktop/Python_datas/103_day6/data_09'):
    ext = os.path.splitext(name)[1]
    if ext == '.xlsx':
        print(name)
        file_path =f'/Users/jakob_pc/Desktop/Python_datas/103_day6/data_09/{name}'

最后再封装一下
multi_part = MIMEMultipart()
multi_part.attach(msg_body)
multi_part['From'] = Header('测试邮箱04','utf-8')
multi_part['To'] = Header('employee04')
multi_part['Subject'] = Header('测试添加多个附件04','utf-8')

顺序：
#01 引入要用的模块
#02 登陆邮箱
#03 编辑邮件内容
#04 把正文加入multi_part(编辑格式)
#05 for循环加入附件
#06 发送邮件

### 103_day10
date = 04/05/2023
# 38 linux或os定时任务


## 未完成：
#16 word基本操作

#17 设置word样式

#18 生成通知书

#19 读取word文档

#20 通过模板生成文档

#21 word转换pdf

#22 读取pdf内容

#23 合并pdf文件

#24 拆分pdf文件

#25 加密pdf文件

#26 创建ppt与基本操作

#27 ppt增加图片

#28 ppt增加流程图

#29 ppt绘制条形图

#30 ppt绘制图表样式

#31 ppt绘制折线图与饼图

#36 zmail的使用

#37 windows定时任务（做不了，或者在surface上用）

#39 发送钉钉普通消息

#40 发送钉钉卡片消息

#41 压缩文件的操作

#42 压缩包密码破解



