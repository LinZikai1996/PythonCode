import csv
import time

from pynput.mouse import Controller, Button

from tool.logger import Logger

log = Logger()


def left_click(x, y):
    mouse = Controller()
    mouse.position = (x, y)
    mouse.click(Button.left)
    time.sleep(2)


class ClickAction:
    def __init__(self, operation_name, x, y, right_or_left='L', wait_time=3):
        self.operation_name = operation_name
        self._x = x
        self._y = y
        self._right_or_left = right_or_left
        self._wait_time = wait_time

        # 对参数进行验证
        if self._x < 0 or self._y < 0:
            raise ValueError(f"Invalid coordinates: {self._x}, {self._y}")
        if self._right_or_left not in ['L', 'R']:
            raise ValueError(f"Invalid click type: {self._right_or_left}")
        if self._wait_time < 0:
            raise ValueError(f"Invalid wait time: {self._wait_time}")

    def click(self):
        mouse = Controller()  # 创建鼠标控制器对象
        mouse.position = (self._x, self._y)  # 设置鼠标位置
        time.sleep(0.1)  # 增加一个小延迟
        try:
            if self._right_or_left == 'L':
                mouse.click(Button.left)  # 左键点击
            else:
                mouse.click(Button.right)  # 右键点击
            log.info(self.operation_name)
        except Exception as e:
            log.error(f"Failed to perform operation {self.operation_name}: {str(e)}")

        time.sleep(self._wait_time)


class ActionConfigFile:
    def __init__(self, config_file_path, corrected_position_x=0, corrected_position_y=0):
        self.actions = {}

        with open(config_file_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            for row in reader:
                try:
                    action = ClickAction(row['operation_name'],
                                         int(row['x']) + corrected_position_x,
                                         int(row['y']) + corrected_position_y,
                                         row['right_or_left'],
                                         int(row['wait_time']))

                    self.actions[action.operation_name] = action
                except ValueError as e:
                    log.error(f"Invalid action in config file: {str(e)}")

    def run(self, operation_name: str):
        if operation_name in self.actions:
            self.actions[operation_name].click()
        else:
            log.error(f"不存在这个步骤")
