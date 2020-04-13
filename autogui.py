
import pyautogui as gui
import time
import openpyxl


# gui.click(30, 400)
# gui.hotkey('end')
# time.sleep(1)
# a = gui.locateCenterOnScreen(
#     "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\과정.png")
# gui.moveTo(a)
# gui.moveRel(121, 0)
# gui.click()
# gui.hotkey('enter')


# a = gui.locateCenterOnScreen(
#     "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\전공명.png")
# gui.moveTo(a)
# gui.moveRel(121, 0)
# gui.click()
# time.sleep(1)
# gui.hotkey('down')
# gui.hotkey('enter')


exel = openpyxl.load_workbook(
    "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.xlsx")
sheet = exel.get_sheet_by_name("Sheet1")

i = 2

while i <= 68:

    # 학년도
    sheet[f'B{i}'].value

    # 학기
    sheet[f'C{i}'].value

    # 교양
    sheet[f'D{i}'].value

    # 재수강
    if sheet[f'E{i}'].value == "N":
    (x, y) = gui.locateCenterOnScreen(
        "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\재수강여부.png")
    gui.click(x + 121, y)
    time.sleep(0.5)
    gui.hotkey('down')
    gui.hotkey('enter')

    elif sheet[f'E{i}'].value == "Y":
    (x, y) = gui.locateCenterOnScreen(
        "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\재수강여부.png")
    gui.click(x + 121, y)
    time.sleep(0.5)
    gui.hotkey('enter')

    # 교과목
    sheet[f'F{i}'].value

    # 학점
    if sheet['f'G{i}'].value == "4":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\취득학점.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        i = 3
        while i == 0:
            gui.hotkey('down')
            i -= 1
        gui.hotkey('enter')

    elif sheet['f'G{i}'].value == "3":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\취득학점.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        i = 2
        while i == 0:
            gui.hotkey('down')
            i -= 1
        gui.hotkey('enter')

    elif sheet['f'G{i}'].value == "2":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\취득학점.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        i = 1
        while i == 0:
            gui.hotkey('down')
            i -= 1

        gui.hotkey('enter')

    elif sheet['f'G{i}'].value == "1":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\취득학점.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        i = 0
        while i == 0:
            gui.hotkey('down')
            i -= 1
        gui.hotkey('enter')
    # 등급
    if sheet['f'H{i}'].value == "A+":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.png")
        gui.click(x + 121, y)
        time.sleep(0.5)

        gui.hotkey('enter')
    elif sheet['f'H{i}'].value == "A0":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        gui.hotkey('down')
        gui.hotkey('enter')

    elif sheet['f'H{i}'].value == "B+":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')

        gui.hotkey('enter')

    elif sheet['f'H{i}'].value == "B0":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('enter')

    elif sheet['f'H{i}'].value == "C+":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('enter')

    elif sheet['f'H{i}'].value == "C0":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('down')
        gui.hotkey('enter')

    elif sheet['f'H{i}'].value == "S":
        (x, y) = gui.locateCenterOnScreen(
            "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.png")
        gui.click(x + 121, y)
        time.sleep(0.5)
        gui.hotkey('up')
        gui.hotkey('up')
        gui.hotkey('up')
        gui.hotkey('enter')

    gui.click(gui.locateCenterOnScreen(
        "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\추가.png"))
    time.sleep(3)
    i += 1
