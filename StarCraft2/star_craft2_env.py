import pickle
import time
from typing import Optional, Union, List, Tuple

import gym
import numpy as np
from gym.core import RenderFrame, ActType, ObsType

from tool.logger import Logger

log = Logger()


class StarCraft2Env(gym.Env):

    def __init__(self):
        super(StarCraft2Env, self).__init__()

        self._transaction_file = 'transaction.pkl'
        # 在这里定义你的观察空间
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(224, 224, 3), dtype=np.uint8)
        # 在这里定义你的行动空间
        self.action_space = gym.spaces.Discrete(6)

    def step(self, action: ActType) -> Tuple[ObsType, float, bool, bool, dict]:
        while True:
            try:
                transaction = self._load_transaction()

                if transaction['action'] is None:
                    transaction['action'] = action
                    self._save_transaction(transaction)
                    break

            except Exception as e:
                log.error(e)
                time.sleep(0.1)

    def render(self) -> Optional[Union[RenderFrame, List[RenderFrame]]]:
        pass

    def reset(self, *, seed: Optional[int] = None, options: Optional[dict] = None, ) -> Tuple[ObsType, dict]:
        print('Rest the environment')
        observation = np.zeros((224, 224, 3), dtype=np.uint8)
        transaction = {'observation': observation, 'reward': 0, 'action': None, 'done': False}
        self._save_transaction(transaction)
        return observation

    def _save_transaction(self, transaction):
        with open(self._transaction_file, 'wb') as f:
            pickle.dump(transaction, f)

    def _load_transaction(self):
        with open(self._transaction_file, 'rb') as f:
            return pickle.load(f)
