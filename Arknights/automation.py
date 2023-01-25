import time

from Util.control_mouse_and_keyboard import left_click
from Util.image_util import screenshot, check_target_img_is_from_source_img_or_no, get_image_size_info, \
    check_image_similarity


class ArknightsAuto(object):

    def __init__(self, operation_type=1):
        self._new_image_path = '/Volumes/mobile_hard_disk/work_temp/screenshot/now_img.png'
        self._source_image_folder = "/Volumes/mobile_hard_disk/work_temp/screenshot/"

        # operation_type = 1 前往上次作战活动
        # operation_type = 2 获取资源
        self._operation_type = operation_type
        self._top_x = 0
        self._top_y = 0

    def start(self):
        self.prepare_for_action()
        self.start_game()

    def prepare_for_action(self):
        print("为开始游戏做些准备 ....")
        self.go_back_to_home_page()

    def go_back_to_home_page(self):
        print("检查下是否在首页")
        if self.check_home_page() is False:
            print("返回首页")
            left_click(x=105, y=105)
            while not self.check_home_page():
                left_click(x=105, y=105)

    def check_home_page(self):
        self.screenshot_from_app()
        result, x, y = check_target_img_is_from_source_img_or_no(
            source_path=f"{self._source_image_folder}home_page.png",
            target_path=self._new_image_path)
        return result

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
            left_click(x=1160, y=250)

            print("点击 '前往上一次作战'")
            left_click(x=1350, y=750)

        print("点击 '开始行动'")
        left_click(1360, 860)

        print("检查我们是否有理智液")
        if not self.check_have_potion_or_no():
            if self.add_potion():
                print("添加理智液")
                left_click(1310, 745)
                time.sleep(5)
                left_click(1360, 860)

        else:
            print("我们没有理智液了，退出游戏")
            left_click(1360, 860)
            self.go_back_to_home_page()
            return False

        print("确认阵容，开始行动")
        left_click(1325, 675)
        return True

    def check_have_potion_or_no(self):
        self.screenshot_from_app()
        result, x, y = check_target_img_is_from_source_img_or_no(
            source_path=f"{self._source_image_folder}have_potion_or_no.png",
            target_path=self._new_image_path)
        return result

    def add_potion(self):
        self.screenshot_from_app()
        result, x, y = check_target_img_is_from_source_img_or_no(
            source_path=f"{self._source_image_folder}add_potion.png",
            target_path=self._new_image_path)
        return result

    def check_action_status(self):
        while True:
            if self.check_similarity_between_source_and_screenshot(
                    source_image_path=f"{self._source_image_folder}finish_action.png", start_position_x=55,
                    start_position_y=255):
                print("行动结束")
                left_click(1325, 675)
                left_click(1325, 675)
                time.sleep(5)
                break
            else:
                time.sleep(20)

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

    def screenshot_from_app(self, size_x=1560, size_y=920):
        screenshot(self._top_x, self._top_y, size_x, size_y, self._new_image_path)
