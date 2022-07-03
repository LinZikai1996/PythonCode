import os
import time
from win32gui import *
from win32con import *
from win32api import *
from PIL import Image, ImageGrab
import imagehash
import cv2


def get_windows_title():
    titles = []

    def foo(hwnd):
        title = {}
        if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
            title['title_name'] = GetWindowText(hwnd)
            title['className'] = GetClassName(hwnd)
            title['size'] = GetWindowRect(hwnd)
            title['handle'] = hwnd
            if title['title_name'] != "" and title['title_name'] is not None:
                titles.append(title)

    EnumWindows(foo, 0)
    return titles


def get_handle_from_list(title_name, title_list):
    for title in title_list:
        if title['title_name'] == title_name:
            return title['handle']
    return None


def start_game(topx, topy, first_time=False):
    if first_time:
        print("Click '终端'")
        left_click(topx + 1000, topy + 250)

        print("Click '前往上一次作战'")
        left_click(topx + 1225, topy + 700)

    print("Click '开始行动(蓝)'")
    left_click(topx + 1270, topy + 780)

    print("Click '开始行动(红)'")
    left_click(topx + 1200, topy + 600)


def left_click(x, y):
    # Move mouse to x, y
    SetCursorPos([x, y])
    # Left click
    mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0)
    # Wait 1 second
    time.sleep(1.5)


def check_game_is_done(topx, topy):
    left_top_x = topx + 62
    left_top_y = topy + 243
    bottom_right_x = topx + 62 + 332
    bottom_right_y = topy + 243 + 85
    new_image_path = 'E:\\tmp\\screenshot\\now_img.jpg'
    continue_check = True
    while continue_check:
        screenshot(left_top_x, left_top_y, bottom_right_x, bottom_right_y, new_image_path)
        change_img_to_gray(new_image_path)
        if check_image_similarity("E:\\tmp\\screenshot\\finish_action.jpg", new_image_path):
            break
        else:
            time.sleep(20)


def screenshot(left_top_x, left_top_y, bottom_right_x, bottom_right_y, path):
    if os.path.exists(path):
        os.remove(path)
    ImageGrab.grab((left_top_x, left_top_y, bottom_right_x, bottom_right_y)).save(path)


def change_img_to_gray(path):
    img = cv2.imread(path, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path, gray)


def check_image_similarity(source_path, target_path):
    source_img = imagehash.average_hash(Image.open(source_path), hash_size=6)
    target_img = imagehash.average_hash(Image.open(target_path), hash_size=6)

    hash_diff = 1 - (target_img - source_img) / len(target_img.hash) ** 2
    if hash_diff >= 0.9:
        print(f"Similarity is {hash_diff}")
        return True
    else:
        return False


def finish_game(topx, topy):
    print("Click screen")
    left_click(topx + 1200, topy + 600)
    time.sleep(5)


if __name__ == '__main__':
    target_title = "明日方舟 - MuMu模拟器"

    print("Start to get all window title")
    title_list = get_windows_title()
    print(f"Get all title, size is {len(title_list)}")
    print(title_list)

    print("Get title handle from list")
    title_handle = get_handle_from_list(target_title, title_list)
    if title_handle is None:
        # TODO Auto open app ...
        print("Windows don't open, please check again!")
        exit(1)
    print(f"target window name : {target_title}, handle : {title_handle}")

    # Remember that the emulator must not be minimized
    print(f"Before set, check location {GetWindowRect(title_handle)}")
    SetWindowPos(title_handle, HWND_TOPMOST, 0, 0, 1400, 900, SWP_SHOWWINDOW)
    title_rect = GetWindowRect(title_handle)
    print(f"After set, check location {title_rect}")

    index = 0
    while index < 3:
        print("Start play game")
        if index == 0:
            start_game(title_rect[0], title_rect[1], True)
        else:
            start_game(title_rect[0], title_rect[1])

        print("Check game is done or no")
        check_game_is_done(title_rect[0], title_rect[1])

        print("Game is finish")
        finish_game(title_rect[0], title_rect[1])

        index = index + 1
