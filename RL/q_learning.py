import os
import pickle
import time
from itertools import product

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from RL.preadtor_game import Cube
from tool.logger import Logger

matplotlib.use('TkAgg')
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


def show_result(number_for_game: int, frequency: int, rewards_list: list, finish_step_list: list):
    log.info(f"游戏的次数是 {number_for_game}, 近 {frequency} 平均奖励是 {np.mean(rewards_list[-frequency:])}")

    rewards_list = rewards_list[-frequency * 10:]
    finish_step_list = finish_step_list[-frequency * 10:]

    moving_avg_for_rewards = np.convolve(rewards_list,
                                         np.ones((frequency,)) / frequency,
                                         mode='valid')
    finish_game_step = np.convolve(finish_step_list,
                                   np.ones((frequency,)) / frequency,
                                   mode='valid')
    plt.figure(1)  # 创建新图

    plt.subplot(211)  # 第一个子图
    plt.plot([index for index in range(len(moving_avg_for_rewards))], moving_avg_for_rewards)
    plt.xlabel('Number of game ')
    plt.ylabel(f'Mean {frequency} reward')

    plt.subplot(212)  # 第二个子图
    plt.plot([index for index in range(len(finish_game_step))], finish_game_step)
    plt.xlabel('Number of game ')
    plt.ylabel('Finish game step')

    plt.suptitle(f'Title game {number_for_game}')
    plt.savefig('resource/temp/result.png')


def train(q_table_file='q_table_file', size=10, print_time=10000, number_of_game=300000000):
    log.info(f"开始训练")
    epsilon = 0.6
    learning_rate = 0.1
    discount = 0.9
    epsilon_decay = 0.99

    rewards_detail = {
        "eat_food": 300,
        "be_caught": -300,
        "moving": -1,
    }

    q_table = init_q_table(q_table_file, size)

    number_of_game_rewards = []
    finish_game_step = []

    for number in range(number_of_game):

        if number % print_time == 0 and number != 0:
            show_result(number, print_time, number_of_game_rewards, finish_game_step)

        player = Cube("player", size)
        food = Cube("food", size)
        enemy = Cube("enemy", size)

        title_reward = 0
        step = 0
        for step in range(500):
            obs = (player - food, player - enemy)
            if np.random.random() > epsilon:
                action = np.argmax(q_table[obs])
            else:
                action = np.random.randint(0, 9)
            player.action(action)

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
                food.action()
                enemy.action()
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
        finish_game_step.append(step)
        epsilon = epsilon * epsilon_decay

    with open(f'q_table_{int(time.time())}.pickle', 'wb') as f:
        pickle.dump(q_table, f)


if __name__ == '__main__':
    train()
