from RL.preadtor_game import EnvCubeV1


def test():
    env = EnvCubeV1()
    print(env.q_table[(1, 1, 1, 1)])
