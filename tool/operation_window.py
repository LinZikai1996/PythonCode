import os
import time

from win32api import SetCursorPos, mouse_event
from win32con import HWND_TOPMOST, SWP_SHOWWINDOW, MOUSEEVENTF_LEFTUP, MOUSEEVENTF_LEFTDOWN
from win32gui import IsWindow, IsWindowEnabled, IsWindowVisible, GetWindowText, GetClassName, GetWindowRect, \
    EnumWindows, SetWindowPos


class OperationWindowUtil:

    def __init__(self, target_title: str, app_path=None,
                 top_x=0, top_y=0, window_length=1400, window_width=900):
        self._target_title = target_title
        self._top_x = top_x
        self._top_y = top_y
        self._window_length = window_length
        self._window_width = window_width
        if app_path is not None:
            self._app_path = app_path
        else:
            self._app_path = "E:\\software\\UU\\emulator\\nemu\\EmulatorShell\\NemuPlayer.exe"
        self._title = {}

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

    def left_click(self, x, y):
        x = self._top_x + x
        y = self._top_y + y
        # Move mouse to x, y
        SetCursorPos([x, y])
        # Left click
        mouse_event(MOUSEEVENTF_LEFTUP | MOUSEEVENTF_LEFTDOWN, 0, 0)
        # Wait 1 second
        time.sleep(2)

    def open_app(self):
        os.startfile(self._app_path)
