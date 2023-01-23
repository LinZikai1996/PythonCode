import time

import pyautogui


def left_chick(x, y):
    pyautogui.click(x=x, y=y)
    time.sleep(2)
