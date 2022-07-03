import os
import time

import cv2
import imagehash
from PIL import ImageGrab, Image
from win32api import SetCursorPos, mouse_event
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_LEFTDOWN
from win32gui import IsWindow, IsWindowEnabled, IsWindowVisible, GetWindowText, GetClassName, GetWindowRect, \
    EnumWindows, SetWindowPos


class MingRiFangZhouAuto:

    def __init__(self):
        self.target_title = "明日方舟 - MuMu模拟器"
        self.new_image_path = 'E:\\tmp\\screenshot\\now_img.jpg'
        self.source_image_folder = "E:\\tmp\\screenshot\\"
        self.top_x = 0
        self.top_y = 0
        self.title = {}

    def start(self):
        print("Get title handle")
        self.get_windows_title()
        print(
            f"target window name : {self.title['title_name']}, handle : {self.title['handle']}, size : {self.title['size']}")
        self.set_window_location()
        index = 0
        while index < 30:
            if index == 0:
                self.start_game(True)
            else:
                self.start_game()
            self.check_game_status()
            index = index + 1

    def get_windows_title(self):
        def foo(handle, mouse):
            if IsWindow(handle) and IsWindowEnabled(handle) and IsWindowVisible(handle):
                if GetWindowText(handle) == self.target_title:
                    self.title['title_name'] = GetWindowText(handle)
                    self.title['className'] = GetClassName(handle)
                    self.title['size'] = GetWindowRect(handle)
                    self.title['handle'] = handle

        EnumWindows(foo, 0)

    def set_window_location(self):
        print(f"Before set, check location {self.title['size']}")
        SetWindowPos(self.title['handle'], HWND_TOPMOST, 0, 0, 1400, 900, SWP_SHOWWINDOW)
        print(f"After set, check location {GetWindowRect(self.title['handle'])}")
        self.top_x, self.top_y = int(self.title['size'][0]), int(self.title['size'][1])

    def start_game(self, first_time=False):
        if first_time:
            print("Click '终端'")
            self.left_click(self.top_x + 1000, self.top_y + 250)

            print("Click '前往上一次作战'")
            self.left_click(self.top_x + 1225, self.top_y + 700)

        print("Click '开始行动(蓝)'")
        self.left_click(self.top_x + 1270, self.top_y + 780)
        if self.check_reason_value():
            print("Add reason value")
            self.left_click(self.top_x + 1190, self.top_y + 675)
            self.left_click(self.top_x + 1270, self.top_y + 780)

        print("Click '开始行动(红)'")
        self.left_click(self.top_x + 1200, self.top_y + 600)

    def check_game_status(self):
        left_top_x = self.top_x + 62
        left_top_y = self.top_y + 243
        bottom_right_x = left_top_x + 332
        bottom_right_y = left_top_y + 85
        continue_check = True
        while continue_check:
            self.screenshot(left_top_x, left_top_y, bottom_right_x, bottom_right_y, self.new_image_path)
            if self.check_image_similarity("E:\\tmp\\screenshot\\finish_action.jpg", self.new_image_path):
                break
            else:
                time.sleep(20)
        print("Click screen")
        self.left_click(self.top_x + 1200, self.top_y + 600)
        print("Game is finish")
        time.sleep(5)

    def check_reason_value(self):
        left_top_x = self.top_x + 666
        left_top_y = self.top_y + 534
        bottom_right_x = left_top_x + 733
        bottom_right_y = left_top_y + 195
        self.screenshot(left_top_x, left_top_y, bottom_right_x, bottom_right_y, self.new_image_path)
        return self.check_image_similarity(f"{self.source_image_folder}check_reason.jpg", self.new_image_path)

    @staticmethod
    def left_click(x, y):
        # Move mouse to x, y
        SetCursorPos([x, y])
        # Left click
        mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0)
        # Wait 1 second
        time.sleep(2)

    @staticmethod
    def screenshot(left_top_x, left_top_y, bottom_right_x, bottom_right_y, path):
        if os.path.exists(path):
            os.remove(path)
        ImageGrab.grab((left_top_x, left_top_y, bottom_right_x, bottom_right_y)).save(path)
        img = cv2.imread(path, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(path, gray)

    @staticmethod
    def check_image_similarity(source_path, target_path):
        source_img = imagehash.average_hash(Image.open(source_path), hash_size=6)
        target_img = imagehash.average_hash(Image.open(target_path), hash_size=6)

        hash_diff = 1 - (target_img - source_img) / len(target_img.hash) ** 2
        if hash_diff >= 0.9:
            print(f"Similarity is {hash_diff}")
            return True
        else:
            return False


if __name__ == '__main__':
    MingRiFangZhouAuto().start()
