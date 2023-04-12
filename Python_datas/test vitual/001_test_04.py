# 重命名

import os
folderPath = r'/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/个人资料备份/2303'
fileList = os.listdir(folderPath)
for i in range(len(fileList)):
    old_name = os.path.join(folderPath, fileList[i])
    new_name = os.path.join(folderPath,str(i + 1) + fileList[i])
    os.rename(old_name, new_name)