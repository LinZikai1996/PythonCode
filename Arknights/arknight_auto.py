import os
import time

import psutil
from pynput.mouse import Controller, Button

from tool.image_util import screenshot, check_target_img_is_from_source_img_or_no, get_image_size_info
from tool.logger import Logger
from tool.run_os_command import run_command

log = Logger()


class Arknights:

    def __init__(self, operation_type=1):
        self.operation_type = operation_type
        self._temp_folder = 'resource/temp'
        if not os.path.exists(self._temp_folder):
            os.makedirs(self._temp_folder)
        self._source_image_folder = "resource/image"

    def start(self):
        if open_emulator():
            self.open_app_and_login()
        self.prepare_for_action()

    def open_app_and_login(self):

        confirm_position(target_image_path=f'{self._source_image_folder}/emulator_home.png',
                         need_click=True,
                         need_continuous_monitoring=True,
                         need_continuous_monitoring_interval_time=5)
        log.info("模拟器已经开启，并且已是活跃")

        log.info(f'打开明日方舟app')
        confirm_position(target_image_path=f'{self._source_image_folder}/app.png', need_click=True)

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

    log.info("移动模拟器归位")
    run_command('osascript script/set_position.scpt')

    return need_login


def is_app_exist(process_name: str) -> bool:
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return True
    return False


def confirm_position(target_image_path: str,
                     after_click_wait_time: int = 2,
                     need_click: bool = False,
                     double_click: bool = False,
                     double_click_interval: float = 0.5,
                     right_or_left: str = 'L',
                     need_continuous_monitoring=False,
                     need_continuous_monitoring_interval_time: int = 2) -> bool:
    if right_or_left not in ['L', 'R']:
        raise ValueError("Parameter right_or_left must be 'L' or 'R'")
    result, x, y = _contrast_image(target_image_path,
                                   need_continuous_monitoring=need_continuous_monitoring,
                                   interval_time=need_continuous_monitoring_interval_time)

    if result and need_click:
        length, width = get_image_size_info(target_image_path)
        _click(x + length // 2, y + width // 2, right_or_left=right_or_left)
        if double_click:
            time.sleep(double_click_interval)
            _click(x + length // 2, y + width // 2, right_or_left=right_or_left)
        time.sleep(after_click_wait_time)

    return result


def confirm_click_effect(target_image_path: str,
                         after_click_wait_time: int = 2,
                         double_click: bool = False,
                         double_click_interval: float = 0.5,
                         right_or_left: str = 'L',
                         need_continuous_monitoring=False,
                         need_continuous_monitoring_interval_time: int = 2) -> bool:
    if right_or_left not in ['L', 'R']:
        raise ValueError("Parameter right_or_left must be 'L' or 'R'")
    result, x, y = _contrast_image(target_image_path,
                                   need_continuous_monitoring=need_continuous_monitoring,
                                   interval_time=need_continuous_monitoring_interval_time)

    if result:
        length, width = get_image_size_info(target_image_path)
        before_click_image_path = "resource/temp/before_click.png"
        after_click_image_path = "resource/temp/after_click.png"
        screenshot(0, 0, 1920, 1080, before_click_image_path)
        _click(x + length // 2, y + width // 2, right_or_left=right_or_left)
        if double_click:
            time.sleep(double_click_interval)
            _click(x + length // 2, y + width // 2, right_or_left=right_or_left)
        time.sleep(after_click_wait_time)
        screenshot(0, 0, 1920, 1080, after_click_image_path)
        if is_same_image(before_click_image_path, after_click_image_path):
            return False  # 如果点击前后屏幕没有变化，则需要重新点击

    return True


def _click(x: int, y: int, right_or_left):
    mouse = Controller()  # 创建鼠标控制器对象
    mouse.position = (x, y)  # 设置鼠标位置
    if right_or_left == 'L':
        mouse.click(Button.left)  # 左键点击
    else:
        mouse.click(Button.right)  # 右键点击


def _contrast_image(target_image_path: str, need_continuous_monitoring: bool, interval_time: int) -> (bool, int, int):
    source_path = "resource/temp/screenshot_now_img.png"
    while True:
        screenshot(0, 0, 1920, 1080, source_path)
        result, x, y = check_target_img_is_from_source_img_or_no(
            source_path=source_path,
            target_path=target_image_path)
        if not need_continuous_monitoring or result:
            break
        log.info(f'等待 {interval_time} s 继续检查')
        time.sleep(interval_time)
    return result, x, y


if __name__ == '__main__':
    Arknights().start()
