import os
import time

import psutil
from pynput.mouse import Controller, Button

from tool.image_util import screenshot, check_target_img_is_from_source_img_or_no, get_image_size_info, is_same_image
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

    def start_auto(self):
        open_emulator()
        if confirm_position_and_click(target_image_path=f'{self._source_image_folder}/home_page.png',
                                      need_click=False,
                                      behavior_interpretation="检查是否在主页") is False:
            self.open_app_and_login()

        self.start_last_battle()

    def open_app_and_login(self):
        confirm_position_and_click(target_image_path=f'{self._source_image_folder}/emulator_home.png',
                                   behavior_interpretation="检查模拟器是否准备好",
                                   need_click=False,
                                   need_continuous_monitoring=True,
                                   need_continuous_monitoring_interval_time=5)
        log.info("模拟器已经准备完毕")

        confirm_position_and_click(target_image_path=f'{self._source_image_folder}/app.png',
                                   behavior_interpretation="点击明日方舟图标")

        confirm_position_and_click(target_image_path=f'{self._source_image_folder}/interlude_animation.png',
                                   behavior_interpretation="跳过过场动画",
                                   need_continuous_monitoring=True,
                                   click_x=(1540 // 2),
                                   click_y=(900 // 2))

        confirm_position_and_click(target_image_path=f'{self._source_image_folder}/login_button.png',
                                   behavior_interpretation="点击登录按钮",
                                   need_continuous_monitoring=True,
                                   after_click_wait_time=10)

        confirm_position_and_click(target_image_path=f'{self._source_image_folder}/login_button.png',
                                   behavior_interpretation="检查并且点击关闭公告栏",
                                   click_x=1444,
                                   click_y=130)

    def start_last_battle(self):
        result = self.start_action(True)
        # result = True
        # index = 0
        # while result:
        #     log.info("开始重复最近作战 ... ")
        #     if index == 0:
        #         result = self.start_action(True)
        #     else:
        #         result = self.start_action()
        #     self.check_action_status()
        #     index = index + 1
        #
        # self.go_back_to_home_page()
        # log.info("行动结束，退出")

    def start_action(self, first_time=False):
        if first_time:
            confirm_position_and_click(target_image_path=f'{self._source_image_folder}/terminal.png',
                                       behavior_interpretation="点击 '终端'", )
            confirm_position_and_click(target_image_path=f'{self._source_image_folder}/last_battle_button.png',
                                       behavior_interpretation="点击 '前往上一次作战'", )
        confirm_position_and_click(target_image_path=f'{self._source_image_folder}/start_action_blue_button.png',
                                   behavior_interpretation="点击 '开始行动'", )
        if confirm_position_and_click(target_image_path=f'{self._source_image_folder}/have_potion_or_no.png',
                                      need_click=False,
                                      behavior_interpretation="是否还有理智液") is True:
            log.info("我们没有理智液了，退出游戏")
        else:
            log.info("我们还有理智液")


def open_emulator():
    log.info("开始运行明日方舟脚本")
    if is_app_exist('qemu-system-aarch64') is False:
        log.info("打开安卓模拟器")
        run_command("screen -S emulator -d -m $HOME/Library/Android/sdk/emulator/emulator -avd Robot")

        log.info("等待 5 秒模拟器后再继续执行 ....")
        time.sleep(5)
    else:
        log.info("模拟器已经启动")

    log.info("移动模拟器归位")
    run_command('osascript script/set_position.scpt')

    log.info("使得窗口活跃")
    run_command('osascript script/set_activate.scpt')


def is_app_exist(process_name: str) -> bool:
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return True
    return False


def confirm_position_and_click(target_image_path: str,
                               behavior_interpretation: str,
                               after_click_wait_time: int = 3,
                               need_click: bool = True,
                               right_or_left: str = 'L',
                               need_continuous_monitoring=False,
                               need_continuous_monitoring_interval_time: int = 2,
                               click_x: int = None,
                               click_y: int = None) -> bool:
    log.info(behavior_interpretation)

    if right_or_left not in ['L', 'R']:
        raise ValueError("Parameter right_or_left must be 'L' or 'R'")
    result, x, y = _contrast_image(target_image_path,
                                   need_continuous_monitoring=need_continuous_monitoring,
                                   interval_time=need_continuous_monitoring_interval_time)

    if result and need_click:
        if click_x is not None and click_y is not None:
            _click(click_x, click_y, right_or_left=right_or_left)
        else:
            length, width = get_image_size_info(target_image_path)
            _click(x + length // 2, y + width // 2, right_or_left=right_or_left)
        time.sleep(after_click_wait_time)

    return result


def _click(x: int, y: int, right_or_left: str = 'L'):
    mouse = Controller()  # 创建鼠标控制器对象
    mouse.position = (x, y)  # 设置鼠标位置
    time.sleep(0.1)  # 增加一个小延迟
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
            log.info(f"发现目标图片 {target_image_path} ")
            break
        log.info(f'等待 {interval_time}s 继续检查')
        time.sleep(interval_time)
    return result, x, y


if __name__ == '__main__':
    Arknights().start_auto()
