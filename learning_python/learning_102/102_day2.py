# date = 03052023
# author = Jakob
# 学习python最好的方式，是大量的做实践练习！
import datetime

print('hello world!')

# 021 统计每个兴趣的学生人数

'''like_count = {} # like_count的class是字典

with open('student_like.txt') as fin:
    for line in fin:
        line = line[:-1]   # line的class是string
        field = line.split(' ') # field的class就是list
        sname,likes = line.split(' ') # sname和likes的class也是string
        like_list = likes.split('，') # like_list的class是list
        for like in like_list: #like的class也是string
            if like not in like_count:
                like_count[like] = 0  #初始化操作不理解
            like_count[like] += 1'''
# print(like_count)
'''print(type(line))
print(type(sname))
print(type(likes))
print(type(field))
print(type(like_list))
print(type(like))
print(type(like_count))'''

# 按兴趣爱好统计学生名单

# 第一步：按兴趣爱好整理名单，以datas接收数据
# 用什么接收单行数据？data是一个元组，每个元素是string，可能会超过2个元素，所以只能用元组
# 用什么接收所有的数据？datas是一个list
# 逻辑应该是按照字典遍历原始文档，加到list里面

'''like_count = {} # like_count的class是字典
like_total = []
datas = []
snames = []

with open('student_like.txt') as fin:
    for line in fin:
        line = line[:-1]   # line的class是string
        field = line.split(' ') # field的class就是list
        sname,likes = line.split(' ') # sname和likes的class也是string
        snames.append(sname)
        like_list = likes.split('，') # like_list的class是list
        for like in like_list: #like的class也是string
            if like not in like_count:
                like_count[like] = 0  #初始化操作不理解
            like_count[like] += 1
            like_total.append(like)

like_total_1 =[]
for i in like_total:
    if i not in like_total_1 :
        like_total_1.append(i)
# print(like_total_1)
# print(snames)

something = []
data = ()
with open('student_like.txt') as fin:
    for line in fin:
        line = line[:-1]   # line的class是string
        field = line.split(' ') # field的class就是list
        sname,likes = line.split(' ') # sname和likes的class也是string
        snames.append(sname)
        like_list = likes.split('，')
# 这时针对每一个出现的like，需要生成一个元组，元组里包含like和sname
        for like in like_list:
            data = (like, sname)
            # for data in something:
            # 这里有没有什么办法？
            something.append(data)

# 先妥协一下



# print(something)



# 需要加一步：data的生成
# 两个可能性：一是直接生成最终结果
# 二是先按照原始数据的line结构，生成key=like，value=sname的字典
# 然后再从字典当中遍历，得出元组

# 先尝试第一种
# 初始化一个元组 data
with open('./student_like_output.txt','w') as fout:
    for like in like_total_1:
        #遍历所有的fields，如果出现like，就把sname加到元组里
        #print(like,':',end=' ')
        datas = []
        datas.append(like)
        for data2 in something:
            if like in data2:
                # print(data2[1],end = ' ')
                datas.append(data2[1])
        fout.write(' '.join(datas) + '\n')
        # print(datas)'''

# 直接输出

# 022 获得当前的日期时间

'''import datetime

current_datetime = datetime.datetime.now()

print(current_datetime,type(current_datetime))

# 格式化时间为字符串形式
str_time = current_datetime.strftime('%Y-%M-%D %H:%M:%S')
print(str_time)

# 分别获取当前年月日和时分
print('year',current_datetime.year)
print('month',current_datetime.month)
print('day',current_datetime.day)
print('hour',current_datetime.hour)
print('minute',current_datetime.minute)
print('second',current_datetime.second)'''

# 023 计算2个日期相隔的天数

'''import datetime

birthday = '1990-08-10'
birthday_date = datetime.datetime.strptime(birthday, '%Y-%m-%d')
print(birthday_date,type(birthday_date))

current_datetime =datetime.datetime.now()

minus_datetime = current_datetime - birthday_date
print(minus_datetime)
print(minus_datetime.days)
print(minus_datetime.days/365)'''

# 024 计算任意日期7天前的日期

'''import datetime

def get_diff_days(pdate, days):
    pdate_obj = datetime.datetime.strptime(pdate, '%Y-%m-%d')
    time_gap = datetime.timedelta(days=days)
    pdate_result = pdate_obj - time_gap
    return pdate_result.strftime('%Y-%m-%d')

print(get_diff_days('2022-12-9',7))
print(get_diff_days('2022-10-8',7))
print(get_diff_days('2023-3-5',7))'''

# 025 计算开始和结束范围内的所有日期

'''import datetime

res = []
def get_date_range(begin_date,end_date):
    while begin_date <= end_date:
        begin_date = datetime.datetime.strptime(begin_date, '%Y-%m-%d')
        days1_timedelta = datetime.timedelta(days=1)
        begin_date = (begin_date + days1_timedelta).strftime('%Y-%m-%d')
        res.append(begin_date)


begin_date = '2023-02-24'
end_date = '2023-03-05'
date_list = get_date_range(begin_date, end_date)
print(res)'''

# 026 unix时间戳转换为日期格式字符串

'''import datetime

unix_time = 1620747647

datetime_obj = datetime.datetime.fromtimestamp(unix_time)
datetime_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
print(datetime_str)'''

# 027 计算日期数据周同比

date_sale = {}

is_first_line = True

with open('date_sale_data.txt') as fin:
    for line in fin:
        if is_first_line:
            is_first_line = False
            continue
        line = line[:-1]
        # print(line)
        date, sale_number = line.split(' ')   # \t是空格键????
        date_sale[date] = float(sale_number)
# print(type(date_sale))

def get_diff_days(date,days):
    current_date = datetime.datetime.strptime(date,'%Y-%m-%d')
    timedelta = datetime.timedelta(days=days)
    return(current_date - timedelta).strftime('%Y-%m-%d')


with open('date_sale_data_output.txt', 'w') as fout:
    datas = []
    for date, sale_number in date_sale.items():
        date_minus_7 = get_diff_days(date,7)
        sale_number_minus_7 = date_sale.get(date_minus_7, 0)
        if sale_number_minus_7 == 0:
            # print(date, round(sale_number),0)
            datas = [date, str(round(sale_number)),'0']
        else:
            week_diff = (sale_number-sale_number_minus_7)/sale_number_minus_7
            datas = [date,str(round(sale_number)),'percent:{:.2%}'.format(week_diff)]
            # print(date,round(sale_number),'percent:{:.2%}'.format(week_diff))
        fout.write(' '.join(datas) + '\n') # 注意惯例，这里是list形式，并且list中每个元素都是string的格式
# print(type(datas))

print('Goodbye')