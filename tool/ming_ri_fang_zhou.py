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
        self._target_title = "明日方舟 - MuMu模拟器"
        self._new_image_path = 'E:\\tmp\\screenshot\\now_img.jpg'
        self._source_image_folder = "E:\\tmp\\screenshot\\"
        self._top_x = 0
        self._top_y = 0
        self._window_length = 1400
        self._window_width = 900
        self._title = {}

    def start(self):
        self.prepare_window()
        self.start_game()

    def prepare_window(self):
        self.get_windows_title()
        print(
            f"目标窗口的名字 : {self._title['title_name']}, "
            f"handle的数值 : {self._title['handle']}, "
            f"窗口大小 : {self._title['size']}")
        self.set_window_location()

    def get_windows_title(self):
        def foo(handle, mouse):
            if IsWindow(handle) and IsWindowEnabled(handle) and IsWindowVisible(handle):
                if GetWindowText(handle) == self._target_title:
                    self._title['title_name'] = GetWindowText(handle)
                    self._title['className'] = GetClassName(handle)
                    self._title['size'] = GetWindowRect(handle)
                    self._title['handle'] = handle

        EnumWindows(foo, 0)

    def set_window_location(self):
        print(f"设置前, 检查位置信息 {self._title['size']}")
        SetWindowPos(self._title['handle'], HWND_TOPMOST, self._top_x, self._top_y, self._window_length,
                     self._window_width,
                     SWP_SHOWWINDOW)
        print(f"设置后, 检查位置信息 {GetWindowRect(self._title['handle'])}")
        if int(self._title['size'][0]) != self._top_x and int(self._title['size'][1]) != self._top_y and int(
                self._title['size'][2]) != self._window_length and int(self._title['size'][3]) != self._window_width:
            print("位置信息设置失败，重新设置")
            SetWindowPos(self._title['handle'], HWND_TOPMOST, self._top_x, self._top_y, self._window_length,
                         self._window_width, SWP_SHOWWINDOW)

            if int(self._title['size'][0]) != self._top_x and int(self._title['size'][1]) != self._top_y and int(
                    self._title['size'][2]) != self._window_length and int(
                self._title['size'][3]) != self._window_width:
                print("设置失败，推出程序")
                exit(1)

    def start_game(self):
        stat_action_or_no = True
        index = 0
        while stat_action_or_no:
            print("开始行动 ... ")
            if index == 0:
                self.start_action(True)
            else:
                self.start_action()
            self.check_action_status()
            index = index + 1

    def start_action(self, first_time=False):
        if first_time:
            print("点击 '终端'")
            self.left_click(1000, 250)

            print("点击 '前往上一次作战'")
            self.left_click(1225, 700)

        print("点击 '开始行动'")
        self.left_click(1270, 780)
        print("检查我们是否有理智液")
        if not self.check_have_potion_or_no():
            if self.check_reason_value():
                print("Add reason value")
                self.left_click(1190, 675)
                self.left_click(1270, 780)
        else:
            print("我们没有理智液了，退出游戏")
            return False

        print("确认阵容，开始行动")
        self.left_click(1200, 600)
        return True

    def check_action_status(self):
        while True:
            if self.check_similarity_between_source_and_screenshot(
                    source_image_path=f"{self._source_image_folder}finish_action.jpg", start_position_x=62,
                    start_position_y=243):
                print("行动结束")
                self.left_click(1200, 600)
                time.sleep(5)
                break
            else:
                time.sleep(20)

    def check_have_potion_or_no(self):
        return self.check_similarity_between_source_and_screenshot(
            source_image_path=f"{self._source_image_folder}have_potion_or_no.jpg", start_position_x=666,
            start_position_y=132)

    def check_reason_value(self):
        return self.check_similarity_between_source_and_screenshot(
            source_image_path=f"{self._source_image_folder}check_reason.jpg", start_position_x=666,
            start_position_y=534)

    def check_similarity_between_source_and_screenshot(self, source_image_path, start_position_x, start_position_y):
        length, width = get_image_size_info(source_image_path)
        left_top_x, left_top_y, bottom_right_x, bottom_right_y = self.get_location(start_position_x, start_position_y,
                                                                                   length, width)
        screenshot(left_top_x, left_top_y, bottom_right_x, bottom_right_y, self._new_image_path)
        return check_image_similarity(source_image_path, self._new_image_path)

    def get_location(self, tl_x, tl_y, length, width):
        tl_x = self._top_x + tl_x
        tl_y = self._top_y + tl_y
        br_x = tl_x + length
        br_y = tl_y + width
        return tl_x, tl_y, br_x, br_y

    def left_click(self, x, y):
        x = self._top_x + x
        y = self._top_y + y
        # Move mouse to x, y
        SetCursorPos([x, y])
        # Left click
        mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0)
        # Wait 1 second
        time.sleep(2)


def screenshot(left_top_x, left_top_y, bottom_right_x, bottom_right_y, path):
    if os.path.exists(path):
        os.remove(path)
    ImageGrab.grab((left_top_x, left_top_y, bottom_right_x, bottom_right_y)).save(path)
    img = cv2.imread(path, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path, gray)


def check_image_similarity(source_path, target_path):
    source_img = imagehash.average_hash(Image.open(source_path), hash_size=6)
    target_img = imagehash.average_hash(Image.open(target_path), hash_size=6)

    hash_diff = 1 - (target_img - source_img) / len(target_img.hash) ** 2
    if hash_diff >= 0.9:
        print(f"图片的相似度是 {format(hash_diff, '.0%')}")
        return True
    else:
        return False


def get_image_size_info(path):
    image = Image.open(path)
    return image.size


if __name__ == '__main__':
    MingRiFangZhouAuto().start()
