
import pyautogui as gui
import time
import openpyxl

exel = openpyxl.load_workbook(
    "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\성적.xlsx")
sheet = exel.get_sheet_by_name("Sheet1")

gui.click(gui.locateCenterOnScreen(
    "C:\\Users\\Han\\Desktop\\onedrive\\Dev\\hanyeongoh\\GITHUB\\Python-Bootcamp\\pyautogui\\추가.png"))
