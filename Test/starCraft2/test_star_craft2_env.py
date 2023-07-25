import StarCraft2
from StarCraft2.star_craft2_env import StarCraft2Env


def test_class():
    sc2 = StarCraft2Env()

    print(sc2.observation_space.sample())
