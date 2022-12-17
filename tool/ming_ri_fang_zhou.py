import os
import time

from tool.image_tool import get_image_size_info, screenshot, check_image_similarity
from tool.operation_window import OperationWindowUtil


class MingRiFangZhouAuto(object):

    def __init__(self):
        self._new_image_path = 'E:\\tmp\\screenshot\\now_img.jpg'
        self._source_image_folder = "E:\\tmp\\screenshot\\"
        self._top_x = 0
        self._top_y = 0
        self._window_util = OperationWindowUtil("明日方舟 - MuMu模拟器", top_x=self._top_x, top_y=self._top_y)

    def start(self):
        self._window_util.prepare_window()
        self.prepare_for_action()
        self.start_game()

    def prepare_for_action(self):
        print("为开始游戏做些准备 ....")
        self.go_back_to_home_page()

    def go_back_to_home_page(self):
        print("检查下是否在首页")
        if self.check_home_page() is False:
            print("返回首页")
            self._window_util.left_click(95, 95)
            while not self.check_home_page():
                self._window_util.left_click(95, 95)

    def check_home_page(self):
        if self.check_similarity_between_source_and_screenshot(
                source_image_path=f"{self._source_image_folder}prepare_for_action.jpg", start_position_x=750,
                start_position_y=372):
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
            self._window_util.left_click(1000, 250)

            print("点击 '前往上一次作战'")
            self._window_util.left_click(1225, 700)

        print("点击 '开始行动'")
        self._window_util.left_click(1270, 780)
        print("检查我们是否有理智液")
        if not self.check_have_potion_or_no():
            if self.check_reason_value():
                print("Add reason value")
                self._window_util.left_click(1190, 675)
                self._window_util.left_click(1270, 780)
        else:
            print("我们没有理智液了，退出游戏")
            self._window_util.left_click(1200, 900)
            self.go_back_to_home_page()
            return False

        print("确认阵容，开始行动")
        self._window_util.left_click(1200, 600)
        return True

    def check_action_status(self):
        while True:
            if self.check_similarity_between_source_and_screenshot(
                    source_image_path=f"{self._source_image_folder}finish_action.jpg", start_position_x=62,
                    start_position_y=243):
                print("行动结束")
                self._window_util.left_click(1200, 600)
                self._window_util.left_click(1200, 600)
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


if __name__ == '__main__':
    MingRiFangZhouAuto().start()
