# date 20230325
# author Jakob
# print hello world
print('hello world!')


import os
import shutil

# dir ='/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人 资料备份/2023电影下载'
def filterfile(file_dir,save_dir,suffix):
    '''
    该函数实现从文件夹中根据文件后缀名提取文件，并存储在新的文件夹中
    file_dir指读的文件目录；save_dir为保存文件的目录
    suffix用于存放打算提取文件的后缀名；
    '''
    if os.path.exists(save_dir):
       shutil.rmtree(save_dir)  #如果已经存在该文件夹，移除
    if not os.path.exists(save_dir):
        os.makedirs(save_dir) #如果不存在该文件夹，则创建，用于储存后续提取出来的文件
    filelist = []  #存储要copy的文件全名
    for dirpath,dirnames,filenames in os.walk(file_dir):#根据路径执行树状的遍历，分别遍历根目录，根目录下的文件夹，文件夹下的文件
        for file in filenames:#遍历文件夹中的文件
            file_type = file.split('.')[-1]#对文件名根据.进行分隔，实现文件名，后缀名的分离
            if(file_type in suffix):#下面根据后缀名是否在列表中，提取文件
                file_fullname = os.path.join(dirpath, file) #文件全名
                filelist.append(file_fullname)#将符合要求的文件存放在列表中
    for file in filelist:
        shutil.copy(file, save_dir)#将列表中的文件复制到新的文件夹
        print('*')

if __name__ == "__main__":
    file_dir = '/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人资料备份/2023电影下载'
    save_dir = '/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人资料备份/2023电影下载/2303'
    suffix = 'mkv'
    filterfile(file_dir,save_dir,suffix)

print('goodbye!')

