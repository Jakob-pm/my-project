print('hello world!')

import pyautogui
import time
import xlrd
import pyperclip
from PIL import Image
import time
import os
import shutil
import datetime

#定义鼠标事件

#pyautogui库其他用法 https://blog.csdn.net/qingfengxd1/article/details/108270159

def mouseClick(clickTimes,lOrR,img,reTry):
    if reTry == 1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.8)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            print("未找到匹配图片,1秒后重试")
            time.sleep(1)
    elif reTry == -1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.8)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=0.8)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
                i += 1
            time.sleep(1)




# 数据检查
# cmdType.value  1.0 左键单击    2.0 左键双击  3.0 右键单击  4.0 输入  5.0 等待  6.0 滚轮
# ctype     空：0
#           字符串：1
#           数字：2
#           日期：3
#           布尔：4
#           error：5
def dataCheck(sheet4):
    checkCmd = True
    #行数检查
    if sheet4.nrows<2:
        print("没数据啊哥")
        checkCmd = False
    #每行数据检查
    i = 1
    while i < sheet4.nrows:
        # 第1列 操作类型检查
        cmdType = sheet4.row(i)[0]
        if cmdType.ctype != 2 or (cmdType.value != 1.0 and cmdType.value != 2.0 and cmdType.value != 3.0
        and cmdType.value != 4.0 and cmdType.value != 5.0 and cmdType.value != 6.0 and cmdType.value != 7.0 and cmdType.value != 8.0):
            print('第',i+1,"行,第1列数据有毛病")
            checkCmd = False
        # 第2列 内容检查
        cmdValue = sheet4.row(i)[1]
        # 读图点击类型指令，内容必须为字符串类型
        if cmdType.value ==1.0 or cmdType.value == 2.0 or cmdType.value == 3.0:
            if cmdValue.ctype != 1:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 输入类型，内容不能为空
        if cmdType.value == 4.0:
            if cmdValue.ctype == 0:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 等待类型，内容必须为数字
        if cmdType.value == 5.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        # 滚轮事件，内容必须为数字
        if cmdType.value == 6.0:
            if cmdValue.ctype != 2:
                print('第',i+1,"行,第2列数据有毛病")
                checkCmd = False
        if cmdType.value == 7.0:
            pass
        i += 1
    return checkCmd

#任务
def mainWork(img):
    i = 1
    while i < sheet4.nrows:
        #取本行指令的操作类型
        cmdType = sheet4.row(i)[0]
        if cmdType.value == 1.0:
            #取图片名称
            img = sheet4.row(i)[1].value
            print(img)
            reTry = 1
            if sheet4.row(i)[2].ctype == 2 and sheet4.row(i)[2].value != 0:
                reTry = sheet4.row(i)[2].value
            mouseClick(1,"left",img,reTry)
            print("单击左键",img)
        #2代表双击左键
        elif cmdType.value == 2.0:
            #取图片名称
            img = sheet4.row(i)[1].value
            print(img)
            #取重试次数
            reTry = 1
            if sheet4.row(i)[2].ctype == 2 and sheet4.row(i)[2].value != 0:
                reTry = sheet4.row(i)[2].value
            mouseClick(2,"left",img,reTry)
            print("双击左键",img)
        #3代表右键
        elif cmdType.value == 3.0:
            #取图片名称
            img = sheet4.row(i)[1].value
            #取重试次数
            reTry = 1
            if sheet4.row(i)[2].ctype == 2 and sheet4.row(i)[2].value != 0:
                reTry = sheet4.row(i)[2].value
            mouseClick(1,"right",img,reTry)
            print("右键",img)
        #4代表输入
        elif cmdType.value == 4.0:
            inputValue = sheet4.row(i)[1].value
            pyperclip.copy(inputValue)
            # print(inputValue)
            pyautogui.hotkey('command','v')
            time.sleep(0.5)
            print("输入:",inputValue)
        #5代表等待
        elif cmdType.value == 5.0:
            #取图片名称
            waitTime = sheet4.row(i)[1].value
            time.sleep(waitTime)
            print("等待",waitTime,"秒")
        #6代表滚轮
        elif cmdType.value == 6.0:
            #取图片名称
            scroll = sheet4.row(i)[1].value
            pyautogui.scroll(int(scroll),x = 100,y = 320)
            print("滚轮滑动",int(scroll),"距离")
        #7代表回车
        elif cmdType.value == 7.0:
            pyautogui.press('enter')
            print("回车")

        i += 1

def move_to_onedrive():

    search_dir = '/Users/jakob_pc/Desktop'
    today = datetime.datetime.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    index=yesterday.strftime('%d_%m_%Y')
    print(index)
    lst1 = []
    str1 = '.crdownload'
    str2 = '.mp4'
    target_path = f'/Users/jakob_pc/Library/CloudStorage/OneDrive-个人/个人/学习记录/德语学习材料/新闻/2023/4月/heute/heute {index}.mp4'
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            ext = os.path.splitext(file)[1]
            lst1.append(ext)

    time1 = time.time()
    while str1 in lst1:
        print('*')
        time.sleep(10)
        curr_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(curr_time, end= ' ')
        print(index, end=' ')
        print('downloading')
        lst1 = []
        for root, dirs, files in os.walk(search_dir):
            for file in files:
                ext = os.path.splitext(file)[1]
                lst1.append(ext)
    time2 = time.time()
    print('download done')
    print(round((time2-time1),2))

    for root, dirs, files in os.walk(search_dir):
        for file in files:
            file_path = f'{root}/{file}'
            ext = os.path.splitext(file)[1]
            if ext == str2:
                print('yes')
                shutil.move(file_path, target_path)





if __name__ == '__main__':
    file = 'cmd.xls'
    #打开文件
    wb = xlrd.open_workbook(filename=file)
    #通过索引获取表格sheet页
    sheet4 = wb.sheet_by_index(3)
    curr_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(curr_time)
    print('欢迎使用！')
    #数据检查
    checkCmd = dataCheck(sheet4)
    print('数据检查无误！')
    # mainWork(sheet4)
    print('waiting for download...')
    #time.sleep(20)
    move_to_onedrive()
    print('done!')


print('Goodbye!')