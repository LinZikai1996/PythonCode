import glob
import os
import pickle
import time
from itertools import product

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from RL.preadtor_game import Cube, EnvCubeV2
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
    plt.figure(number_for_game)  # 创建新图, 使用number_for_game作为唯一的标识符

    plt.subplot(211)  # 第一个子图
    plt.plot([index for index in range(len(moving_avg_for_rewards))], moving_avg_for_rewards)
    plt.xlabel('Number of game ')
    plt.ylabel(f'Mean {frequency} reward')

    plt.subplot(212)  # 第二个子图
    plt.plot([index for index in range(len(finish_game_step))], finish_game_step)
    plt.xlabel('Number of game ')
    plt.ylabel('Finish game step')

    plt.subplots_adjust(hspace=.5)  # 调整子图之间的间距
    plt.suptitle(f'Title game {number_for_game}')
    # 搜索所有的结果文件
    result_files = glob.glob('resource/temp/result_*.png')

    # 按文件的修改时间排序
    result_files.sort(key=os.path.getmtime)

    # 如果文件数量超过10个，删除最早的文件
    while len(result_files) > 10:
        os.remove(result_files[0])
        del result_files[0]

    # 保存新的结果文件
    plt.savefig(f'resource/temp/result_{number_for_game}.png')


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


def start_train_v1():
    train()


def start_train_v2():
    log.info(f"开始训练")
    env = EnvCubeV2()
    # 初始 ε
    epsilon = 1.0
    # ε 的衰减因子，每轮训练后，ε 将乘以这个因子
    epsilon_decay = 0.99
    # 初始学习率
    learning_rate = 0.5
    # 学习率的衰减因子，每轮训练后，学习率将乘以这个因子
    learning_rate_decay = 0.99
    discount = 0.9
    epsilon_decay = 0.99

    number_of_game_rewards = []
    finish_game_step = []

    max_moving_avg = 0

    for number in range(env.total_number_of_executions):
        obs = env.reset()
        done = False
        if number % env.print_result == 0 and number != 0:
            show_result(number, env.print_result, number_of_game_rewards, finish_game_step)

            if number * 10 % env.print_result == 0 and number != 0:
                moving_avg = np.mean(number_of_game_rewards[-env.print_result * 10:])
                if moving_avg > max_moving_avg:
                    max_moving_avg = moving_avg
                    env.save_q_table()

        title_reward_per_game = 0
        title_step_per_game = 0
        while not done:
            if np.random.random() > epsilon:
                action = np.argmax(env.q_table[obs])
            else:
                action = np.random.randint(0, env.action_space_values)
            new_obs, reward, done = env.step(action)

            if done:
                new_q = reward
            else:
                current_q_table_value = env.q_table[obs][action]
                max_future_q = np.argmax(env.q_table[(env.player - env.food, env.player - env.enemy)])
                new_q = 1 - learning_rate * current_q_table_value + learning_rate * (reward + discount * max_future_q)

            env.q_table[obs][action] = new_q
            obs = new_obs

            title_reward_per_game = title_reward_per_game + reward
            title_step_per_game += 1

        finish_game_step.append(title_step_per_game)
        # 在每轮训练后，衰减 ε
        epsilon *= epsilon_decay
        # 在每轮训练后，衰减学习率
        learning_rate *= learning_rate_decay


if __name__ == '__main__':
    start_train_v1()
