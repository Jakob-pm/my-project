# 移动到桌面
# 写操作日志到txt文档
encoding='utf-8'

print('hello world!')

def move_3_items():

    import pyautogui
    import os
    import shutil

    search_dir = '/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人资料备份/2023电影下载/2303'

    result_files = []
    for root,dirs,files in os.walk(search_dir):
        for file in files:
            file_path = f'{root}/{file}'
            ext = os.path.splitext(file)[1]
            # print(ext)
            if ext == '.mkv': # 文件类型包括.mkv和.mp4
                result_files.append(
                    (file, file_path,
                    os.path.getsize(file_path) / 1000000)) #单位转换为M
        #print(root,dirs,files)


    lst1= sorted(result_files,
           key=lambda x: x[2])[:3]
    print('本次任务：')
    print(lst1)

    # 加入log
    import datetime
    def log_w():
        log = '/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人资料备份/2023电影下载/handling_log.md'
        with open(log, 'a') as logfile:  # 'w'是写入并覆盖 'a'是保留原来的并写入新的
            curr_time = datetime.datetime.now()
            # print(curr_time )
            str_time = curr_time.strftime('%Y-%m-%d %H:%M:%S')
            # print(str_time)
            logfile.write(str_time + '\n')
            sum_value = 0
            n = 0
            for i, m, k in result_files:
                sum_value += k
                n += 1
            # print(sum_value)
            # print(n)
            sum_value = round(sum_value / 1000)  # 单位转换为G
            logfile.write('总数据量'+str(sum_value)+'G'+ '，')
            logfile.write('一共'+str(n)+'个文件'+ '，')
            logfile.write('平均每个文件'+str(round(sum_value/n,2))+'G'+ '\n')

            for file,path,amount in lst1:
                amount = str(round(amount/1000,2))
                s = ''
                line = s.join(file+'    '+amount+'G'+'    '+'ready')
                logfile.write(line + '\n')

    log_w()




    for i,m,k in lst1:
        file = i
        ori_path = m
        target_path = '/Users/jakob_pc/Desktop'
        shutil.move(ori_path, target_path)
        print('*')

        # 这里加一个检查原路径并remove的环节(需要加在move动作之后)
        # if ori_path:
            # os.remove(ori_path)
        log = '/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人资料备份/2023电影下载/handling_log.md'
        with open(log, 'a') as logfile:  # 'w'是写入并覆盖 'a'是保留原来的并写入新的
            curr_time = datetime.datetime.now()
            # print(curr_time )
            str_time = curr_time.strftime('%Y-%m-%d %H:%M:%S')
            # print(str_time)
            logfile.write(str_time + '\n')
            logfile.write('move' +i+ ' to desktop' + '\n')
        print()

for i in range(10):
    move_3_items()


print('goodbye!')