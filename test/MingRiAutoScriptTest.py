from win32con import HWND_TOPMOST, SWP_SHOWWINDOW
from win32gui import SetWindowPos

from tool.MingRiAutoScript import get_windows_title, screenshot, change_img_to_gray, check_image_similarity


def test_get_windows_title():
    print(get_windows_title())


def test_change_img_to_gray():
    change_img_to_gray("E:\\tmp\\screenshot\\now_img.jpg")


def test_screenshot():
    screenshot(0 + 62, 0 + 243, 62 + 332, 243 + 85)


def test_set_window_pos():
    SetWindowPos("460086", HWND_TOPMOST, 0, 0, 1400, 900, SWP_SHOWWINDOW)


def test_check_image_similarity():
    check_image_similarity("E:\\tmp\\screenshot\\finish_action.jpg", "E:\\tmp\\screenshot\\now_img.jpg")
