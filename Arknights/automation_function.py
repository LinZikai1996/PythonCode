import sys
import time

import psutil

from tool.control_mouse_and_keyboard import left_click
from tool.image_util import screenshot, check_target_img_is_from_source_img_or_no, get_image_size_info, \
    check_image_similarity
from tool.logger import Logger
from tool.run_os_command import run_command

log = Logger()


class ArknightsAuto:
    def __init__(self, operation_type=1):
        # operation_type = 1 前往上次作战活动
        # operation_type = 2 获取资源
        # operation_type = 3 生息演算
        self.operation_type = operation_type

        self._new_image_path = '/Volumes/mobile_hard_disk/work_temp/screenshot/now_img.png'
        self._source_image_folder = "/Volumes/mobile_hard_disk/work_temp/screenshot/"
        self._top_x = 0
        self._top_y = 0

    def start(self):
        if open_emulator():
            self.open_app_and_login()
        self.prepare_for_action()
        self.start_game()

    def open_app_and_login(self):

        log.info("检查下模拟器主页面")
        while self._check_image_in_screenshot("emulator_home.png") is False:
            log.info("还未打开，等待 10s 继续检查")
            time.sleep(10)

        log.info("打开明日方舟")
        self._left_click(x=660, y=730)
        time.sleep(10)

        log.info("跳过过场")
        self._left_click(x=760, y=580)
        time.sleep(5)

        log.info("登录明日方舟")
        self._left_click(x=760, y=666)
        time.sleep(20)

        if self._check_image_in_screenshot("announcement_1.png") is False \
                and \
                self._check_image_in_screenshot("announcement_2.png") is False:
            log.info("登录无公告栏")
        else:
            log.info("关闭公告栏")
            self._left_click(x=1480, y=120)

        log.info("登录完成")

    def prepare_for_action(self):
        log.info("为开始游戏做些准备 ....")
        self.go_back_to_home_page()

    def go_back_to_home_page(self):
        log.info("检查下是否在首页")
        while self._check_image_in_screenshot("home_page.png") is False:
            log.info("返回首页")
            self._left_click(x=105, y=105)

    def start_game(self):
        stat_action_or_no = True
        index = 0
        while stat_action_or_no:
            log.info("开始行动 ... ")
            if index == 0:
                result = self.start_action(True)
            else:
                result = self.start_action()
            if result is False:
                log.info("退出")
                sys.exit(0)
            self.check_action_status()
            index = index + 1

    def start_action(self, first_time=False):
        if first_time:
            log.info("点击 '终端'")
            self._left_click(x=1160, y=250)

            log.info("点击 '前往上一次作战'")
            self._left_click(x=1350, y=750)

        log.info("点击 '开始行动'")
        self._left_click(1360, 860)

        log.info("检查我们是否有理智液")
        if not self._check_image_in_screenshot("have_potion_or_no.png"):
            if self._check_image_in_screenshot("add_potion.png"):
                log.info("添加理智液")
                self._left_click(1310, 745)
                time.sleep(5)
                self._left_click(1360, 860)

        else:
            log.info("我们没有理智液了，退出游戏")
            self._left_click(1360, 860)
            self.go_back_to_home_page()
            return False

        log.info("确认阵容，开始行动")
        self._left_click(1325, 675)
        return True

    def check_action_status(self):
        while True:
            if self.check_image_similarity_at_position(
                    source_image_path=f"{self._source_image_folder}finish_action.png", start_position_x=55,
                    start_position_y=255):
                log.info("行动结束")
                self._left_click(1325, 675)
                self._left_click(1325, 675)
                time.sleep(5)
                break
            else:
                time.sleep(20)

    def check_image_similarity_at_position(self, source_image_path, start_position_x, start_position_y):
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

    def _left_click(self, x, y):
        left_click(x=x + self._top_x, y=y + self._top_y)

    def _check_image_in_screenshot(self, image_name: str) -> bool:
        screenshot(self._top_x, self._top_y, 1560, 920, self._new_image_path)
        result, x, y = check_target_img_is_from_source_img_or_no(
            source_path=f"{self._source_image_folder}{image_name}",
            target_path=self._new_image_path)
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

    log.info("使模拟器活跃")
    left_click(x=760, y=37)

    return need_login


def is_app_exist(process_name: str) -> bool:
    for proc in psutil.process_iter():
        if proc.name() == process_name:
            return True
    return False
