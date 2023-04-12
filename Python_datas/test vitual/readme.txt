根据文件后缀处理文件，包括：
1. 移动文件并删除文件夹
2. 文件重命名
3. 整理操作日志
原则：
1. 一个批次处理3个文件




可参考代码：

# 016 把电影文件夹中的电影mpk文件从文件夹取出，然后删除文件夹

# 怎样获取文件后缀名：
# os.path.splitext('/path/to/aaa/mp3')
# -->输出：('/path/to/aaa','.mp3')

# 怎样移动文件
# import shutil
# shutil.move('aaa.txt','dir/bbb/foo')

'''import os
import shutil

dir ='./arrange_dir'

for file in os.listdir(dir):
    ext = os.path.splitext(file)[1] # 使用这个函数获得后缀名
    ext = ext[1:]  #切片，index以0开始，所以去掉了第一个元素
    # print(file)
    if not os.path.isdir(f'{dir}/{ext}'):
        os.mkdir(f'{dir}/{ext}') # 这个方法可以创建目录
    # print(file,ext)
    source_path = f'{dir}/{file}'
    target_path = f'{dir}/{ext}/{file}'
    shutil.move(source_path, target_path)'''


# 017 递归搜索目录找出最大文件
# 路径位置：/Users/jakob_pc/Desktop/Python实践

# 方法：
# for root,dirs,files in os.walk('python/Lib/email'):
# root  代表当前目录
# dirs  代表当前目录下的子目录
# files 代表当前目录下普通文件

'''import os
search_dir = '/Users/jakob_pc/Desktop/Python实践'

result_files = []
for root,dirs,files in os.walk(search_dir):
    for file in files:
        file_path = f'{root}/{file}'
        result_files.append(
            (file_path,
            os.path.getsize(file_path) / 1000))
    #print(root,dirs,files)

print(sorted(result_files,
       key=lambda x: x[1],
       reverse=True)[:3])'''

批量删除空文件夹
import os
var='Wind'
##Psur，Qair，SWdown，Tair，Wind
for i in range(2000,2022):
    year=i
    global g_path
    g_path=r"H:\GLDAS\3jing_GLDAS\wind_2m\%s" %year

    def d_RemoveDir():
        for v_root,v_dirs,v_files in os.walk(g_path):
            #通过listdir判断文件夹是否为空.
            if not os.listdir(v_root):
                os.rmdir(v_root)
            #查看删除后的结果.
            for v_file in v_files:
                v_rf=os.path.join(v_root+r'\\'+v_file)
                print(v_rf)
        return
    d_RemoveDir()


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



