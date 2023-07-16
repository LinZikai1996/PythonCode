import math
import time

import psutil

from tool.control_mouse_and_keyboard import ClickAction
from tool.image_util import screenshot, check_target_img_is_from_source_img_or_no, get_image_size_info
from tool.logger import Logger
from tool.run_os_command import run_command

log = Logger()


class Arknights:

    def __init__(self, operation_type):
        self.operation_type = operation_type
        self._source_image_folder = "/Volumes/mobile_hard_disk/work_temp/screenshot/"

    def start(self):
        if open_emulator():
            self.open_app_and_login()
        self.prepare_for_action()

    def open_app_and_login(self):
        pass

    def prepare_for_action(self):
        log.info("为开始游戏做些准备 ....")


def open_emulator() -> bool:
    log.info("开始运行明日方舟脚本")
    need_login = True
    if is_app_exist('qemu-system-aarch64') is False:
        log.info("打开安卓模拟器")
        run_command("screen -S emulator -d -m $HOME/Library/Android/sdk/emulator/emulator -avd Robot")

        log.info("等待 5 秒模拟器后再继续执行 ....")
        time.sleep(5)
    else:
        need_login = False

    return need_login


def is_app_exist(process_name: str) -> bool:
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return True
    return False


def confirm_position_and_click(operation_name: str, target_image_path: str, wait_time=2):
    result, x, y = contrast_image(target_image_path)
    if result:
        length, width = get_image_size_info(target_image_path)
        click_x = math.floor((x + x + length) / 2)
        click_y = math.floor((y + y + width) / 2)
        ClickAction(operation_name, click_x, click_y, wait_time=wait_time)


def continuous_check_screen(target_image_path: str):
    result, x, y = contrast_image(target_image_path)


def contrast_image(target_image_path: str) -> (bool, int, int):
    source_path = "/Volumes/mobile_hard_disk/work_temp/screenshot/screenshot_now_img.png"
    screenshot(0, 0, 1920, 1080, source_path)
    return check_target_img_is_from_source_img_or_no(
        source_path=source_path,
        target_path=target_image_path)
