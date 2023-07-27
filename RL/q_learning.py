import os
import pickle
import time
from itertools import product

import numpy as np

from PreadtorGames.preadtor_game import Cube
from tool.logger import Logger

log = Logger()


def init_q_table(q_table_file, size_for_map):
    q_table = {}
    if os.path.exists(q_table_file):
        try:
            with open(q_table_file, 'rb') as f:
                q_table = pickle.load(f)
        except Exception as e:
            print(f"Error in loading q_table: {e}")
    else:
        range_list = list(range(-size_for_map + 1, size_for_map))
        for state in product(product(range_list, repeat=2), repeat=2):
            q_table[state] = [0] * 9

    return q_table


def train(q_table_file='q_table_file', size=10, print_time=10000, number_of_game=3000000):
    epsilon = 0.6
    learning_rate = 0.1
    discount = 0.95
    epsilon_decay = 0.99

    rewards_detail = {
        "eat_food": 100,
        "be_caught": -300,
        "moving": -1,
    }

    q_table = init_q_table(q_table_file, size)

    number_of_game_rewards = []

    for number in range(number_of_game):

        if number % print_time == 0:
            log.info(f"游戏的次数是 {number}, 近 {print_time} 平均奖励是 {np.mean(number_of_game_rewards[-print_time:])}")

        player = Cube("player", size)
        food = Cube("food", size)
        enemy = Cube("enemy", size)

        title_reward = 0
        for i in range(1000):
            obs = (player - food, player - enemy)
            if np.random.random() > epsilon:
                action = np.argmax(q_table[obs])
            else:
                action = np.random.randint(0, 9)
            player.action(action)
            food.action()
            enemy.action()

            need_to_stop_train = False

            if player.__eq__(food):
                reward = rewards_detail.get("eat_food")
                need_to_stop_train = True
                new_q = reward
            elif player.__eq__(enemy):
                reward = rewards_detail.get("be_caught")
                need_to_stop_train = True
                new_q = reward
            else:
                reward = rewards_detail.get("moving")
                current_q_table_value = q_table[obs][action]
                max_future_q = np.argmax(q_table[(player - food, player - enemy)])
                new_q = 1 - learning_rate * current_q_table_value + learning_rate * (reward + discount * max_future_q)

            q_table[obs][action] = new_q

            title_reward += reward

            if need_to_stop_train:
                break

        log.debug(f"player 所在 {player.__str__()}, "
                  f"food 所在 {food.__str__()}, "
                  f"enemy 所在 {enemy.__str__()}, "
                  f"奖励 {title_reward}")
        number_of_game_rewards.append(title_reward)
        epsilon = epsilon * epsilon_decay

    with open(f'q_table_{int(time.time())}.pickle', 'wb') as f:
        pickle.dump(q_table, f)


if __name__ == '__main__':
    train()
