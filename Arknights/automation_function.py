import math
import sys
import time

import psutil

from tool.control_mouse_and_keyboard import left_click, ActionConfigFile
from tool.image_util import screenshot, check_target_img_is_from_source_img_or_no, get_image_size_info, \
    check_image_similarity
from tool.logger import Logger
from tool.run_os_command import run_command

log = Logger()


class ArknightsAuto:
    def __init__(self, operation_type=1):
        # operation_type = 1 前往上次作战活动
        # operation_type = 2 日常任务
        # operation_type = 3 生息演算
        self.operation_type = operation_type

        self._new_image_path = '/Volumes/mobile_hard_disk/work_temp/screenshot/now_img.png'
        self._source_image_folder = "/Volumes/mobile_hard_disk/work_temp/screenshot/"
        self._top_x = 0
        self._top_y = 0

        self._action = ActionConfigFile(
            config_file_path="/Volumes/mobile_hard_disk/project/PythonCode/Arknights/resource/click_position.csv",
            corrected_position_x=0,
            corrected_position_y=0)

    def start(self):
        if open_emulator():
            self.open_app_and_login()
        self.prepare_for_action()
        if self.operation_type == 1:
            self.to_last_battle()

    def open_app_and_login(self):

        def check_emulator_home():
            return self._check_image_in_screenshot_or_no("emulator_home.png")

        def check_interlude_animation():
            return self._check_image_in_screenshot_or_no("interlude_animation.png")

        def check_login_page():
            return self._check_image_in_screenshot_or_no("login_page.png")

        def check_announcement():
            return not any(self._check_image_in_screenshot_or_no(image) for image in
                           ["announcement_1.png", "announcement_2.png", "announcement_3.png"])

        self._action.run("使模拟器活跃")
        self.check_screen_status(check_emulator_home, "模拟器主页面还未打开，等待 10s 继续检查", "打开明日方舟")
        self.check_screen_status(check_interlude_animation, "明日方舟还未打开，等待 10s 继续检查", "跳过过场")
        self.check_screen_status(check_login_page, "登录页面还未打开，等待 10s 继续检查", "登录明日方舟")
        self.check_screen_status(check_announcement, "检查公告栏", "关闭公告栏")

        log.info("登录完成")

    def check_screen_status(self, condition, log_msg, action_name=None, interval=10):
        while not condition():
            log.info(log_msg)
            time.sleep(interval)

        if action_name:
            self._action.run(action_name)

    def prepare_for_action(self):
        log.info("为开始游戏做些准备 ....")
        self._action.run("使模拟器活跃")
        self.go_back_to_home_page()

    def go_back_to_home_page(self):
        log.info("检查下是否在首页")
        while not self._check_image_in_screenshot_or_no("home_page.png"):
            self._action.run("返回首页")

    def to_last_battle(self):
        result = True
        index = 0
        while result:
            log.info("开始行动 ... ")
            if index == 0:
                result = self.start_action(True)
            else:
                result = self.start_action()
            self.check_action_status()
            index = index + 1

        self.go_back_to_home_page()
        log.info("行动结束，退出")

    def start_action(self, first_time=False):
        if first_time:
            self._action.run("点击 '终端'")
            self._action.run("点击 '前往上一次作战'")
        self._action.run("点击 '开始行动'")

        log.info("检查我们是否有理智液")
        if not self._check_image_in_screenshot_or_no("have_potion_or_no.png"):
            if self._check_image_in_screenshot_or_no("add_potion.png"):
                log.info("添加理智液")
                self._action.run("添加理智液")
                self._action.run("点击 '开始行动'")

        else:
            self._action.run("我们没有理智液了，退出游戏")
            return False

        self._action.run("确认阵容，开始行动")
        return True

    def check_action_status(self):
        def check_action_end_or_no():
            return self._check_image_in_screenshot_or_no("finish_action.png")

        self.check_screen_status(check_action_end_or_no, "作战还未结束，等待 10s 继续检查", "行动结束，确认成果")
        self._action.run("行动结束，关闭")

    def _check_image_in_screenshot_or_no(self, image_name: str) -> bool:
        screenshot(self._top_x, self._top_y, 1560, 920, self._new_image_path)
        result, x, y = check_target_img_is_from_source_img_or_no(
            source_path=self._new_image_path,
            target_path=f"{self._source_image_folder}{image_name}")
        return result


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
