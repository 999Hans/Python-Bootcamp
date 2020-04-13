
import pyautogui
import time
import openpyxl
import pyperclip


workbook = openpyxl.load_workbook(
    'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.xlsx')
time.sleep(1)
sheet = workbook["Sheet1"]


i = 2

a = sheet[f'F{i}'].value
(x, y) = pyautogui.locateCenterOnScreen(
    'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\과목명.png')
pyautogui.click(x+130, y)
time.sleep(1)
pyperclip.copy(a)
time.sleep(1)
pyautogui.hotkey("ctrl", "v")
time.sleep(1)
