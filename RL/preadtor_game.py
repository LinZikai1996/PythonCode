import collections
import glob
import os
import pickle

import cv2
import numpy as np
from PIL import Image
import time


class Cube:
    def __init__(self, name, size):
        self.name = name
        self._size = size
        self._x = np.random.randint(0, self._size)
        self._y = np.random.randint(0, self._size)

        self._action_array = [(1, 1), (-1, 1), (1, -1), (-1, -1), (0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]

    def __str__(self):
        return f'{self.name} :({self._x}, {self._y})'

    def __sub__(self, other: "Cube"):
        return self._x - other._x, self._y - other._y

    def __eq__(self, other: "Cube"):
        return self._x == other._x and self._y == other._y

    def action(self, choose: int = None):
        if choose:
            self._move(*self._action_array[choose])
        else:
            self._move(*self._action_array[np.random.randint(0, len(self._action_array))])

    def _move(self, x: int, y: int):
        x = x if x is not None else np.random.randint(-1, 2)
        y = y if y is not None else np.random.randint(-1, 2)
        self._x += x
        self._y += y

        if self._x < 0:
            self._x = 0
        elif self._x >= self._size:
            self._x = self._size - 1

        if self._y < 0:
            self._y = 0
        elif self._y >= self._size:
            self._y = self._size - 1

    def x(self):
        return self._x

    def y(self):
        return self._y


class EnvCubeV2:

    def __init__(self, size=10, action_space_values=9, return_image=False,
                 rewards_detail=None, total_number_of_executions=300000000, print_result=10000,
                 games_executed_per_game=200):
        self.size = size
        self.observation_space_values = (self.size, self.size, 3)
        self.action_space_values = action_space_values
        self.return_image = return_image
        self.total_number_of_executions = total_number_of_executions
        self.print_result = min(total_number_of_executions // 100, print_result)
        self.games_executed_per_game = games_executed_per_game
        self._pickle_folder = 'resource/pickle'

        if rewards_detail is None:
            rewards_detail = {
                "eat_food": 25,
                "be_caught": -300,
                "moving": -1,
            }
        self.rewards_detail = rewards_detail

        self.player = None
        self.food = None
        self.enemy = None

        self.color_map = {
            # blue
            1: (255, 0, 0),
            # green
            2: (0, 255, 0),
            # red
            3: (0, 0, 255),
        }

        self.color_for_player = self.color_map.get(1)
        self.color_for_food = self.color_map.get(2)
        self.color_for_enemy = self.color_map.get(3)

        self.execute_count = 0

        self.q_table = None
        self._init_q_table()

    def reset(self):
        self._init_position()
        return self._return_observation()

    def _init_position(self):
        self.player = Cube("player", self.size)
        self.food = Cube("food", self.size)
        while self.player.__eq__(self.food):
            self.food = Cube("food", self.size)

        self.enemy = Cube("enemy", self.size)
        while self.enemy.__eq__(self.food) or self.enemy.__eq__(self.player):
            self.enemy = Cube("enemy", self.size)

        self.execute_count = 0

    def step(self, action_value):
        self.execute_count += 1

        need_to_stop_train = False
        self.player.action(action_value)

        if self.player.__eq__(self.food):
            reward = self.rewards_detail.get("eat_food")
            need_to_stop_train = True
        elif self.enemy.__eq__(self.player):
            reward = self.rewards_detail.get("be_caught")
            need_to_stop_train = True
        else:
            reward = self.rewards_detail.get("moving")
            self.food.action()
            self.enemy.action()

        return self._return_observation(), reward, (
                need_to_stop_train or self.execute_count >= self.total_number_of_executions)

    def _return_observation(self):
        if self.return_image:
            return self._return_image()
        else:
            return (self.player - self.food) + (self.player - self.enemy)

    def _return_image(self):
        pic_info = np.zeros((self.size, self.size, 3), dtype=np.uint8)
        pic_info[self.food.x()][self.food.y()] = self.color_for_food
        pic_info[self.enemy.x()][self.enemy.y()] = self.color_for_enemy
        pic_info[self.player.x()][self.player.y()] = self.color_for_player
        return Image.fromarray(pic_info, 'RGB')

    def render(self):
        cv2.imshow('Predator', np.array(self._return_image().resize((800, 800))))
        cv2.waitKey(1)

    def _init_q_table(self, q_table_file=None):
        q_table = collections.defaultdict(lambda: [0] * 9)
        if q_table_file and os.path.exists(q_table_file):
            try:
                with open(q_table_file, 'rb') as f:
                    loaded_q_table = pickle.load(f)
                q_table.update(loaded_q_table)
            except Exception as e:
                print(f"Error in loading q_table: {e}")
        self.q_table = q_table

    def save_q_table(self):
        if not os.path.exists(self._pickle_folder):
            os.makedirs(self._pickle_folder)
        with open(f'{self._pickle_folder}/q_table_{int(time.time())}.pickle', 'wb') as f:
            pickle.dump(self.q_table, f)

        # 获取所有 pickle 文件
        pickle_files = glob.glob(f'{self._pickle_folder}/q_table_*.pickle')

        # 按文件的修改时间排序
        pickle_files.sort(key=os.path.getmtime)

        # 只保留最新的三个文件，删除其他文件
        while len(pickle_files) > 3:
            os.remove(pickle_files[0])
            del pickle_files[0]
