# datetime string的正确写法

# import datetime
# curr_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(curr_time)


# 关闭Chrome浏览器

import pyautogui
import time
# from PIL import Image
# import pyperclip

def mouseClick(clickTimes,lOrR,img,confi,reTry):
    if reTry == 1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=confi)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                break
            print("未找到匹配图片,1秒后重试")
            time.sleep(1)
    elif reTry == -1:
        while True:
            location=pyautogui.locateCenterOnScreen(img,confidence=confi)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
            time.sleep(1)
    elif reTry > 1:
        i = 1
        while i < reTry + 1:
            location=pyautogui.locateCenterOnScreen(img,confidence=confi)
            if location is not None:
                pyautogui.click(location.x,location.y,clicks=clickTimes,interval=0.2,duration=0.2,button=lOrR)
                print("重复")
                i += 1
            time.sleep(1)


pyautogui.moveTo(616, 853, 0.1)
pyautogui.leftClick()

time.sleep(1)

url='www.baidu.com'
pyautogui.typewrite(url, 0.1)
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('hello world', 0.1)
pyautogui.press('enter')
time.sleep(1)
#pyautogui.moveTo(100, 320, 2)
# time.sleep(3)
# pyautogui.leftClick()
# pyautogui.scroll(-300,100,320)
i = 0
while i <19:
    pyautogui.scroll(-3,x = 100,y = 320)
    time.sleep(0.5)
    i+=1
# pyautogui.scroll(-300) #这样就不行了
time.sleep(3)


img = './tc_12.png'
confi =0.9
location=pyautogui.locateCenterOnScreen(img,confidence=confi)
print(location)
pyautogui.click(location.x,location.y,clicks=1,interval=0.2,duration=0.2,button='left')
# mouseClick(1,"left",img,confi=0.9,reTry=1)