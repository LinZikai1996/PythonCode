import pyautogui

from util.control_mouse_and_keyboard import left_chick
from util.image_tool import get_image_size_info, screenshot, check_image_similarity


class ArknightsAuto(object):

    def __init__(self):
        self._new_image_path = '/Volumes/mobile_hard_disk/work_temp/screenshot/now_img.png'
        self._source_image_folder = "/Volumes/mobile_hard_disk/work_temp/screenshot/"
        self._top_x = 0
        self._top_y = 0

    def prepare_for_action(self):
        print("为开始游戏做些准备 ....")
        self.go_back_to_home_page()

    def go_back_to_home_page(self):
        print("检查下是否在首页")
        if self.check_home_page() is False:
            print("返回首页")
            left_chick(x=105, y=105)
            while not self.check_home_page():
                left_chick(x=105, y=105)

    def check_home_page(self):
        if self.check_similarity_between_source_and_screenshot(
                source_image_path=f"{self._source_image_folder}home_page.png", start_position_x=826,
                start_position_y=410):
            print("在首页")
            return True
        else:
            return False

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
            left_chick(1160, 250)

            print("点击 '前往上一次作战'")
            left_chick(1370, 750)

        print("点击 '开始行动'")
        left_chick(1350, 850)
        print("检查我们是否有理智液")
        if not self.check_have_potion_or_no():
            if self.check_reason_value():
                print("Add reason value")
                self._window_util.left_click(1190, 675)
                self._window_util.left_click(1270, 780)

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
