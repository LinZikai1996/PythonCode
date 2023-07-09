import csv
import time

import pyautogui

from tool.logger import Logger

log = Logger()


def left_click(x, y):
    pyautogui.click(x=x, y=y)
    time.sleep(2)


class ClickAction:

    def __init__(self, operation_name: str, x: int, y: int, right_or_left: str = 'left', wait_time: int = 3):
        self.operation_name = operation_name
        self._x = x
        self._y = y
        self._right_or_left = right_or_left
        self._wait_time = wait_time

    def click(self):
        if self._right_or_left == 'left':
            log.info(f"左击 {self._x}, {self._y}")
            pyautogui.click(x=self._x, y=self._y)
        else:
            log.info(f"右击 {self._x}, {self._y}")
            pyautogui.rightClick(x=self._x, y=self._y)

        time.sleep(self._wait_time)


class ActionConfigFile:

    def __init__(self, config_file_path: str):
        self.actions = []

        with open(config_file_path, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',', quotechar='"')
            for row in reader:
                self.actions.append(
                    ClickAction(row['operation_name'],
                                int(row['x']),
                                int(row['y']),
                                row['right_or_left'],
                                int(row['wait_time'])))

    def run(self):
        for action in self.actions:
            log.info(f"执行: {action.operation_name}")
            action.click()
