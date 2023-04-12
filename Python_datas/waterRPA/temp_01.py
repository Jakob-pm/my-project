import pyautogui
import time

# pyautogui.doubleClick(x=500, y=900)
# pyautogui.scroll(30, 30)
# pyautogui.press('esc')
pyautogui.moveTo(616, 853, 2)
pyautogui.leftClick()
url='www.google.com'
pyautogui.typewrite(url, 0.25)
pyautogui.press('enter')
time.sleep(2)
pyautogui.typewrite('hello world', 0.25)
pyautogui.press('enter')
time.sleep(1)
#pyautogui.moveTo(100, 320, 2)
time.sleep(3)
# pyautogui.leftClick()
# pyautogui.scroll(-300,100,320)
pyautogui.scroll(-300,x = 100,y = 320)
pyautogui.scroll(-300) #这样就不行了
pyautogui.moveTo(26, 46, 2)
time.sleep(3)
pyautogui.leftClick()


#
# pyautogui.typewrite('pyautogui', 0.25)
# pyautogui.press('enter')


