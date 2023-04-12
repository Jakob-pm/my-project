print('hello world')

# /Users/jakob_pc/Downloads/TV-20230318-2100-4800.webxxl.h264.mp4

import os
import shutil

search_dir = '/Users/jakob_pc/Downloads'
for root, dirs, files in os.walk(search_dir):
    for file in files:
        file_path = f'{root}/{file}'
        ext = os.path.splitext(file)[1]
        if ext == '.mp4':
            str = os.path.splitext(file)[0]
            print(str)
            year = str[3:7]
            month = str[7:9]
            day = str[9:11]
            print(year)
            print(month)
            print(day)
            index = f'{day}_{month}_{year}'
            target_path = f'/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/学习记录/德语学习材料/新闻/2023/3月/Tagesschau 20 Uhr/tagesschau {index}.mp4'
            shutil.move(file_path, target_path)
            print(f'{index} done!')





print('goodbye!')