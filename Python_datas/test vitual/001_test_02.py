# 批量删除空文件夹

import os


def d_RemoveDir():
    for v_root,v_dirs,v_files in os.walk(file_path):
        #通过listdir判断文件夹是否为空.
        if not os.listdir(v_root):
            os.rmdir(v_root)
        #查看删除后的结果.
        for v_file in v_files:
            v_rf=os.path.join(v_root+r'\\'+v_file)
            print(v_rf)
    return
file_path= '/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人资料备份/2023电影下载'
d_RemoveDir()