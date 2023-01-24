import time

import pyautogui


def left_click(x, y):
    pyautogui.click(x=x, y=y)
    time.sleep(2)
