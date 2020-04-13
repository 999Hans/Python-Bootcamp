import pyautogui
import time
import openpyxl
import pyperclip

workbook = openpyxl.load_workbook(
    'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.xlsx')
time.sleep(1)
sheet = workbook["Sheet1"]


i = 5

while i <= 56:

    pyautogui.click(14, 231)
    pyautogui.hotkey('end')
    time.sleep(0.5)

    # 과정
    (x, y) = pyautogui.locateCenterOnScreen(
        'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\과정.png')
    pyautogui.click(x+221, y)
    time.sleep(2)
    pyautogui.click(x+130, y)
    time.sleep(0.5)
    pyautogui.hotkey('enter')

    time.sleep(1)

    # 전공명 고르기
    (x, y) = pyautogui.locateCenterOnScreen(
        "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\전공명.png")
    pyautogui.click(x + 121, y)
    time.sleep(1.5)
    if sheet[f'A{i}'].value == "환":
        time.sleep(0.5)
        pyautogui.hotkey('down')

    elif sheet[f'A{i}'].value == "물":
        time.sleep(0.5)

    pyautogui.hotkey('enter')
    # 수강년도
    a = sheet[f'B{i}'].value
    (x, y) = pyautogui.locateCenterOnScreen(
        'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\수강년도.png')
    pyautogui.click(x+130, y)
    time.sleep(0.5)
    b = 2020-a
    print(b)
    c = 1
    while c <= b:
        pyautogui.hotkey('down')
        c += 1
        time.sleep(0.2)
    pyautogui.hotkey('enter')
    학년도 = a

    # 학기
    (x, y) = pyautogui.locateCenterOnScreen(
        'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\학기.png')
    pyautogui.click(x+130, y)
    time.sleep(0.5)
    if '1' in sheet[f'C{i}'].value:
        pass
    elif '2' in sheet[f'C{i}'].value:
        pyautogui.hotkey('down')
    else:
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
        pyautogui.hotkey('down')
    pyautogui.hotkey('enter')

    # 과목유형
    (x, y) = pyautogui.locateCenterOnScreen(
        'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\과목유형.png')
    pyautogui.click(x+130, y)
    time.sleep(1.5)
    if '전공' in sheet[f'D{i}'].value:
        pass
    else:
        pyautogui.hotkey('down')
    pyautogui.hotkey('enter')
    time.sleep(0.5)

    # 재수강
    (x, y) = pyautogui.locateCenterOnScreen(
        "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\재수강여부.png")
    pyautogui.click(x + 121, y)
    if sheet[f'E{i}'].value == "N":
        time.sleep(0.5)
        pyautogui.hotkey('down')
        pyautogui.hotkey('enter')

    elif sheet[f'E{i}'].value == "Y":
        time.sleep(0.5)
        pyautogui.hotkey('enter')

    # 과목명
    a = sheet[f'F{i}'].value
    (x, y) = pyautogui.locateCenterOnScreen(
        'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\과목명.png')
    pyautogui.click(x+130, y)
    time.sleep(1)
    pyperclip.copy(a)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(1)

    # 학점
    a = sheet[f'G{i}'].value
    (x, y) = pyautogui.locateCenterOnScreen(
        'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\취득학점.png')
    pyautogui.click(x+130, y)
    time.sleep(0.5)
    b = 1
    while b < a:
        pyautogui.hotkey('down')
        b += 1
    pyautogui.hotkey('enter')

    # 등급
    (x, y) = pyautogui.locateCenterOnScreen(
        'C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.png')
    pyautogui.click(x+130, y)
    time.sleep(1.5)
    x = sheet[f'H{i}'].value
    if x == 'A+':
        n = 0
    elif x == 'A0':
        n = 1
    elif x == 'B+':
        n = 3
    elif x == 'B0':
        n = 4
    elif x == 'C+':
        n = 6
    elif x == 'C0':
        n = 7
    else:
        n = 13
    b = 0
    while b < n:
        pyautogui.hotkey('down')
        b += 1
        time.sleep(0.5)
    pyautogui.hotkey('enter')
    time.sleep(0.5)
    # 추가누르기
    pyautogui.click(pyautogui.locateCenterOnScreen(
        "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\추가.png"))
    time.sleep(3)

    pyautogui.click(pyautogui.locateCenterOnScreen(
        "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\저장.png"))
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)
    pyautogui.hotkey('enter')
    time.sleep(1)

    i += 1
