# 017 递归搜索目录找出最大文件
# 路径位置：/Users/jakob_pc/Desktop/Python实践

# 方法：
# for root,dirs,files in os.walk('python/Lib/email'):
# root  代表当前目录
# dirs  代表当前目录下的子目录
# files 代表当前目录下普通文件

import os
import shutil

search_dir = '/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人资料备份/2023电影下载'

result_files = []
for root,dirs,files in os.walk(search_dir):
    for file in files:
        file_path = f'{root}/{file}'
        ext = os.path.splitext(file)[1]
        # print(ext)
        if ext == '.mp4':
            result_files.append(
                (file_path,
                os.path.getsize(file_path) / 1000000)) #单位转换为M
    #print(root,dirs,files)

sum =0
n = 0
for i,k in result_files:
    sum += k
    n+=1

sum = round(sum/1000) #单位转换为G
print(sum)
print(n)
print(round(sum/n,2))

lst1= sorted(result_files,
       key=lambda x: x[1])[:3]

for i,k in lst1:
    ori_path = i
    target_path = '/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人资料备份/2303'
    shutil.move(ori_path,target_path)
    print('*')
